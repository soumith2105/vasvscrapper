from vasvscrapper.enums.scrapper_enums import LoginUrlEnum
from vasvscrapper.login.utilities import login_scrapper
from vasvscrapper.network_requests import get_login_html
from vasvscrapper.status_codes.login import (
    LOGIN_CREDENTIALS_INVALID,
    LOGIN_SCRAPPER_FAILED,
    LOGIN_SUCCESS,
    LOGIN_VCE_CRASHED,
)


async def login_student(roll_number, password) -> dict:
    """
    Extracts the student information of a student
    and return it in a dictionary.

    PARAMETERS
    ----------
    roll_number    : str
        Roll number of the student in vce.
    password       : str
        Password of the student in vce portal.

    RETURNS
    -------
    obj : dict
        Extracted information of a given student.
    """

    user = {}
    try:
        status_code, profile_page_soup, url = await get_login_html(roll_number, password)

        if url == LoginUrlEnum.FAIL.value:
            user["status"] = LOGIN_CREDENTIALS_INVALID

        elif len(profile_page_soup("span")) == 0 or status_code > 400:
            user["status"] = LOGIN_VCE_CRASHED

        else:
            user = await login_scrapper(profile_page_soup)
            user["status"] = LOGIN_SUCCESS

        return user
    except TimeoutError:
        user["status"] = LOGIN_VCE_CRASHED

    except Exception:
        user["status"] = LOGIN_SCRAPPER_FAILED
