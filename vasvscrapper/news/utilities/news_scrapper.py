import re
from datetime import datetime

from vasvscrapper.enums import NewsPatternsEnum


async def checker(obj):
    ret_obj = obj
    count = 0

    categories = []

    description = obj["content"].lower()  # noqa: F841
    for news_pattern in NewsPatternsEnum.values():
        pattern, key = news_pattern["pattern"], news_pattern["key"]

        condition = re.sub(r"(?P<name>[a-z]+)", r"'\1'", pattern)
        condition = re.sub(r"&", f" in description and ", condition)
        condition = re.sub(r"\|", f" in description or ", condition)
        condition = re.sub(r"\) in description", f")", condition)
        condition = re.sub(r"(?P<name>[a-z])\'\)", fr"\1' in description)", condition)
        condition = re.sub(r"\$REMAINING", "count == 0", condition)

        if eval(condition):
            categories.append(key)
            count += 1

    ret_obj["categories"] = str(categories)
    return ret_obj


async def news_scrapper(news_page_soup):
    news_table = news_page_soup.find(id="tblGrid")
    news_block = news_table("tbody")[0]("tr")
    news_objs = []
    for news_row in news_block:
        news_obj = {}
        news_date = datetime.strptime(news_row.find(class_="date").text, "%d-%b-%Y").strftime("%Y-%m-%d")

        news_link = news_row.find("a").attrs.get("href")
        news_category = news_row.find("a").find("em").text
        news_content = (
            news_row.find("a")
            .text[len(news_category) + 1 :]
            .replace("\u201c", "'")
            .replace("\u201d", "'")
            .replace('"', "'")
            .replace("\u2018", "'")
            .replace("\u2019", "'")
            .replace("\u2013", "-")
        )

        news_obj["date"] = news_date
        news_obj["link"] = news_link
        news_obj["content"] = news_content
        news_obj["index"] = news_category[1:-1]

        news_objs.append(await checker(news_obj))

    return news_objs
