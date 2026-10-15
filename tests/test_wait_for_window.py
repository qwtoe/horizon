"""Tests for the publish-window wait helper (scripts/wait_for_window.py)."""

from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path

import pytest

from scripts.wait_for_window import DEFAULT_MAX_WAIT_SECONDS, plan_wait

UTC = timezone.utc
WORKFLOW = Path(__file__).resolve().parents[1] / ".github" / "workflows" / "daily-summary.yml"

# Measured GitHub schedule drift for this repo: 144 runs from 2026-05 to 2026-10,
# expressed as hours after the cron time. Median 4.3h; the two >7h days are outliers
# covered by test_drift_outliers_still_run.
OBSERVED_DRIFT_HOURS = [1.41, 2.04, 3.37, 4.32, 4.70, 5.56, 6.43]


def _epoch(day: int, hour: int, minute: int = 0) -> int:
    """Unix timestamp for 2026-10-<day> HH:MM UTC."""
    return int(datetime(2026, 10, day, hour, minute, tzinfo=UTC).timestamp())


def _cron_utc() -> tuple[int, int]:
    """The (hour, minute) the daily workflow's cron actually fires, read from the workflow."""
    match = re.search(r"cron:\s*'(\d+)\s+(\d+)", WORKFLOW.read_text(encoding="utf-8"))
    assert match, "no cron entry found in .github/workflows/daily-summary.yml"
    minute, hour = (int(group) for group in match.groups())
    return hour, minute


def test_median_drift_sleeps_until_the_window():
    # cron 18:00 UTC + 4.3h drift -> 22:18, sleep until 00:20 UTC the next day.
    wait, run_epoch, reason = plan_wait(_epoch(16, 22, 18))

    assert reason == "wait"
    assert run_epoch == _epoch(17, 0, 20)
    assert wait == 2 * 3600 + 2 * 60


def test_fastest_observed_drift_still_waits():
    # cron 18:00 UTC + 1.41h drift -> 19:24; the wait must stay within the cap.
    wait, run_epoch, reason = plan_wait(_epoch(16, 19, 24))

    assert reason == "wait"
    assert run_epoch == _epoch(17, 0, 20)
    assert wait <= DEFAULT_MAX_WAIT_SECONDS


def test_early_trigger_sleeps_the_cap():
    # 18:30 is too early to reach 00:20 within the cap, so sleep the cap (and still
    # publish during the Beijing morning) rather than waiting past the 6h job limit.
    wait, run_epoch, reason = plan_wait(_epoch(16, 18, 30))

    assert reason == "capped"
    assert wait == DEFAULT_MAX_WAIT_SECONDS
    assert run_epoch == _epoch(17, 0, 0)


def test_slowest_observed_drift_runs_immediately():
    # cron 18:00 UTC + 6.43h drift -> 00:26, five minutes past the window.
    wait, run_epoch, reason = plan_wait(_epoch(17, 0, 26))

    assert reason == "late"
    assert (wait, run_epoch) == (0, _epoch(17, 0, 26))


def test_landing_exactly_on_the_window_counts_as_missed():
    wait, _, reason = plan_wait(_epoch(17, 0, 20))

    assert (wait, reason) == (0, "late")


def test_drift_outliers_still_run():
    """2026-08-27/28 saw 9.6h and 11.1h drift; nothing repo-side fixes that, but the
    digest must still go out the same morning instead of being skipped."""
    cron_hour, cron_minute = _cron_utc()

    for drift_hours in (9.56, 11.09):
        triggered = _epoch(16, cron_hour, cron_minute) + int(drift_hours * 3600)
        wait, run_epoch, reason = plan_wait(triggered)

        assert (wait, reason) == (0, "late")
        assert run_epoch == triggered


@pytest.mark.parametrize("drift_hours", OBSERVED_DRIFT_HOURS)
def test_observed_drift_publishes_in_the_morning_window(drift_hours: float):
    """For every drift the repo has actually seen, the run must start inside the
    00:00-00:50 UTC window: Horizon plus deploy takes ~10 min, so a later start
    would miss 09:00 Beijing."""
    cron_hour, cron_minute = _cron_utc()
    triggered = _epoch(16, cron_hour, cron_minute) + int(drift_hours * 3600)

    _, run_epoch, _ = plan_wait(triggered)

    assert _epoch(17, 0, 0) <= run_epoch <= _epoch(17, 0, 50)
