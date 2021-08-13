import asyncio

from tests.attendance.attendance_const import (
    attendance_soup,
    attendance_stats,
    extra_attendance_stats,
    merge_attendance_stats,
)
from vasvscrapper.attendance.utilities import attendance_scrapper, merge_attendance


def test_attendance_scrapper():
    res = asyncio.run(attendance_scrapper(attendance_soup, True))
    assert res == attendance_stats


def test_manage_attendance():
    res = asyncio.run(merge_attendance(attendance_stats, extra_attendance_stats))
    assert res == merge_attendance_stats
