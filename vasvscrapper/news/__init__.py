"""
News scrapper which extract information from news page
and return information in dictionary.
"""

from .news_scrapper import get_news, get_news_in_range

__all__ = ["get_news", "get_news_in_range"]
