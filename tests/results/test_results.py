import asyncio

from tests.results.result_consts import final_result, headings, headings_main, mark_rows, result_soup
from vasvscrapper.results.utilities import result_scrapper
from vasvscrapper.results.utilities.result_scrapper import semester_marks_scrapper, subject_marks_scrapper


def test_result_scrapper():
    result = asyncio.run(result_scrapper(result_soup))
    assert result == final_result


def test_subject_marks_scrapper():
    news = asyncio.run(subject_marks_scrapper(mark_rows, headings))
    assert news == final_result[0]


def test_semester_marks_scrapper():
    news = asyncio.run(semester_marks_scrapper(mark_rows, headings, headings_main))
    assert news == final_result[1]
