import aiohttp
from bs4 import BeautifulSoup
from yarl import URL


async def get_login_html(roll_number, password, timeout=20) -> tuple[int, BeautifulSoup, URL]:
    """
    Logs in the student and returns status
    and BeautifulSoup object of the request.

    PARAMETERS
    ----------
    roll_number    : str
        Roll number of the student in vce.
    password       : str
        Password of the student in vce portal.
    timeout        : int
        Timeout of the page before it terminates fetching (default is 20 seconds).

    RETURNS
    -------
    obj: tuple
        HTTP status of a given page, BeautifulSoup object of the response, url of the response.
    """

    params = {"LoginID": roll_number, "Password": password}
    async with aiohttp.ClientSession() as session:
        async with session.post("https://vce.ac.in/", data=params, ssl=False, timeout=timeout) as resp:
            return resp.status, BeautifulSoup(await resp.text(), "lxml"), resp.url


async def get_news_html(page_number) -> tuple[int, BeautifulSoup]:
    """
    Fetches the News webpage and returns status
    and BeautifulSoup object of the request.

    PARAMETERS
    ----------
    page_number    : int
        Page number in vce website.

    RETURNS
    -------
    obj: tuple
        HTTP status of a given page, BeautifulSoup object of the response.
    """

    payload = {"page": page_number}
    async with aiohttp.ClientSession() as session:
        async with session.get("https://vce.ac.in/News_Events", params=payload, ssl=False) as resp:
            return resp.status, BeautifulSoup(await resp.text(), "lxml")


async def get_attendance_html(link, timeout=120):
    """
    Fetches the Attendance webpage and returns status
    and BeautifulSoup object of the request.

    PARAMETERS
    ----------
    link    : str
        Link of attendance page in vce website.
    timeout: int
        Timeout of the page before it terminates fetching (default is 120 seconds).

    RETURNS
    -------
    obj: tuple
        HTTP status of a given page, BeautifulSoup object of the response.
    """

    async with aiohttp.ClientSession() as session:
        async with session.get(link, ssl=False, timeout=timeout) as resp:
            return resp.status, BeautifulSoup(await resp.text(), "html.parser")


async def get_results_html(link, timeout=120):
    """
    Fetches the Results webpage and returns status
    and BeautifulSoup object of the request.

    PARAMETERS
    ----------
    link    : str
        Link of attendance page in vce website.
    timeout: int
        Timeout of the page before it terminates fetching (default is 120 seconds).

    RETURNS
    -------
    obj: tuple
        HTTP status of a given page, BeautifulSoup object of the response.
    """

    async with aiohttp.ClientSession() as session:
        async with session.get(link, ssl=False, timeout=timeout) as resp:
            return resp.status, BeautifulSoup(await resp.text(), "html.parser")
