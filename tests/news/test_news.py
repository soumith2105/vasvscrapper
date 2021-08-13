import asyncio

from tests.news.news_consts import after_checker, before_checker, expected_news_result, news_soup
from vasvscrapper.news.utilities import news_scrapper
from vasvscrapper.news.utilities.news_scrapper import checker


def test_login_student_fail():
    news = asyncio.run(news_scrapper(news_soup))
    assert news == expected_news_result


def test_checker():
    news = asyncio.run(checker(before_checker))
    assert news == after_checker
