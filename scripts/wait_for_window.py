#!/usr/bin/env python3
"""Wait for the publish window before fetching.

GitHub's `schedule` trigger fires late — measured over 144 runs of this repo
(2026-05 ~ 2026-10): median +4.3h, fastest +1.4h, slowest +11h after the cron
time. The workflow therefore triggers early (UTC 18:00 = 02:00 Beijing) and
this script sleeps until UTC 00:20 (08:20 Beijing) before Horizon runs, so the
daily digest is published before 09:00 Beijing while still covering the latest
news (including the US day).

The wait is capped at 5h30m because a GitHub job is killed after 6 hours; the
cap leaves room for the fetch and deploy. If the trigger was so early that
reaching the window would exceed the cap, we sleep the cap and run; if the
window was just missed (GitHub was only minutes late), we run immediately —
late is better than a missing digest.
"""

from __future__ import annotations

import argparse
import sys
import time
from datetime import datetime, timedelta, timezone

DEFAULT_TARGET = "00:20"  # UTC, i.e. 08:20 Beijing
DEFAULT_MAX_WAIT_SECONDS = 5 * 3600 + 30 * 60  # 5h30m, bounded by GitHub's 6h job limit
# A target more than half a day away means we just missed it (rather than
# arriving early), so there is nothing to wait for.
STALE_TARGET_SECONDS = 12 * 3600


def plan_wait(
    now_epoch: int,
    target: str = DEFAULT_TARGET,
    max_wait_seconds: int = DEFAULT_MAX_WAIT_SECONDS,
) -> tuple[int, int, str]:
    """Decide how long to wait before Horizon runs.

    Args:
        now_epoch: Current time as a Unix timestamp (seconds).
        target: Target time of day, "HH:MM" (UTC).
        max_wait_seconds: Upper bound on a single wait.

    Returns:
        (wait_seconds, run_epoch, reason) — how long to sleep, when Horizon
        should start, and why: "wait" (sleep until the window), "capped"
        (arrived far too early, sleep the cap), "late" (window just missed,
        run now).
    """
    now = datetime.fromtimestamp(now_epoch, tz=timezone.utc)
    hour, minute = (int(part) for part in target.split(":"))
    target_at = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
    if target_at <= now:
        target_at += timedelta(days=1)  # today's target already passed, take the next one

    wait = int((target_at - now).total_seconds())
    if wait <= max_wait_seconds:
        return wait, now_epoch + wait, "wait"
    if wait <= STALE_TARGET_SECONDS:
        return max_wait_seconds, now_epoch + max_wait_seconds, "capped"
    return 0, now_epoch, "late"


def _format(epoch: int) -> str:
    utc = datetime.fromtimestamp(epoch, tz=timezone.utc)
    beijing = utc.astimezone(timezone(timedelta(hours=8)))
    return f"{utc:%Y-%m-%d %H:%M} UTC / {beijing:%Y-%m-%d %H:%M} Beijing"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Sleep until the publish window (default 00:20 UTC / 08:20 Beijing)"
    )
    parser.add_argument("--target", default=DEFAULT_TARGET, help='time of day "HH:MM" (UTC)')
    parser.add_argument(
        "--max-wait-seconds", type=int, default=DEFAULT_MAX_WAIT_SECONDS, help="wait cap in seconds"
    )
    args = parser.parse_args(argv)

    now_epoch = int(time.time())
    wait, run_epoch, reason = plan_wait(now_epoch, args.target, args.max_wait_seconds)

    print(f"Triggered at: {_format(now_epoch)}")
    if reason == "wait":
        print(f"Sleeping {wait // 60} min, Horizon starts at {_format(run_epoch)}")
        time.sleep(wait)
    elif reason == "capped":
        print(
            f"::warning::Triggered earlier than expected (reaching {args.target} UTC would exceed "
            f"the {args.max_wait_seconds // 60} min cap), sleeping the cap instead: {_format(run_epoch)}"
        )
        time.sleep(wait)
    else:
        print(f"::warning::Publish window already passed, running now: {_format(run_epoch)}")
    print(f"Horizon starts at: {_format(int(time.time()))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
