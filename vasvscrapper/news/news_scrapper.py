import asyncio

from vasvscrapper.network_requests import get_news_html
from vasvscrapper.news.utilities import news_scrapper
from vasvscrapper.status_codes.news import NEWS_SCRAPPER_FAILED, NEWS_SUCCESS, NEWS_VCE_CRASHED


async def get_news(page_number):
    """
    Extracts the news information of a given page
    number and return it in a dictionary.

    PARAMETERS
    ----------
    page_number    : int
        Page number in vce website

    RETURNS
    -------
    obj : dict
        Extracted information for a given page
    """

    news = {"page_number": page_number}
    try:
        status, news_page_soup = await get_news_html(page_number)

        if status >= 400:
            news["status"] = NEWS_VCE_CRASHED

        else:
            news_objs = await news_scrapper(news_page_soup)

            news["news"] = news_objs
            news["status"] = NEWS_SUCCESS

        return news

    except Exception:
        news["status"] = NEWS_SCRAPPER_FAILED
        return news


async def get_news_in_range(start_page, end_page, limit=25) -> dict:
    """
    Extracts the news information of a given page numbers
    range and return it in a dictionary.

    PARAMETERS
    ----------
    start_page    : int
        Starting page number of vce website
    end_page      : int
        Ending page number of vce website
    limit         : int, optional
        Limit the ending page to certain page (default is 25)

    RETURNS
    -------
    obj : dict
        Extracted information for a all the pages in given range
    """

    if end_page > limit:
        end_page = limit
    tasks = []
    for page_number in range(start_page, end_page + 1):
        tasks.append(asyncio.create_task(get_news(page_number)))

    all_news = await asyncio.gather(*tasks)

    result_news_objs = {
        "news": [],
        "status": {
            NEWS_SUCCESS: [],
            NEWS_VCE_CRASHED: [],
            NEWS_SCRAPPER_FAILED: [],
        },
    }

    for news in all_news:
        status = news["status"]
        if news["status"] in (NEWS_VCE_CRASHED, NEWS_SCRAPPER_FAILED):
            result_news_objs["status"][status].append(news["page_number"])

        else:
            result_news_objs["status"][status].append(news["page_number"])
            result_news_objs["news"].extend(news["news"])

    return result_news_objs
