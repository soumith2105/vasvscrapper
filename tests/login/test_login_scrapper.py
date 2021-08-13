import asyncio

from tests.login.login_consts import (
    after_curate,
    after_get_value,
    before_curate,
    before_get_value,
    expected_login_result,
    login_soup,
)
from vasvscrapper.login import login_student
from vasvscrapper.login.utilities import login_scrapper
from vasvscrapper.login.utilities.login_scrapper import curate_values, get_values_by_labels
from vasvscrapper.status_codes.login import LOGIN_CREDENTIALS_INVALID


def test_login_student_fail():
    roll_number = "1602-17-737-046"
    password = "abcdef"
    user = asyncio.run(login_student(roll_number, password))
    assert user["status"] == LOGIN_CREDENTIALS_INVALID


def test_login_scrapper():
    user = asyncio.run(login_scrapper(login_soup))
    assert user == expected_login_result


def test_get_values_by_labels():
    result = get_values_by_labels(before_get_value)
    assert result == after_get_value


def test_curate_values():
    result = curate_values(before_curate)
    assert result == after_curate
