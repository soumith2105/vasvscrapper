"""
    Makes a network request and returns status
    and BeautifulSoup object of the request.
    """
from .async_requests import get_attendance_html, get_login_html, get_news_html, get_results_html

__all__ = ["get_login_html", "get_news_html", "get_attendance_html", "get_results_html"]
