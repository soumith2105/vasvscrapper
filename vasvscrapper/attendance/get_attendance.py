from asyncio.exceptions import TimeoutError

from vasvscrapper.attendance.utilities import attendance_scrapper, merge_attendance
from vasvscrapper.network_requests import get_attendance_html
from vasvscrapper.status_codes.attendance import ATTENDANCE_SCRAPPER_FAILED, ATTENDANCE_SUCCESS, ATTENDANCE_VCE_CRASHED


async def get_attendance(link, current=True, extra=True):
    """
    Extracts the attendance information and return a dictionary.

    PARAMETERS
    ----------
    link    : str
        Link of the result page
    current : bool
        If the attendance has to include current running attendance (default if True).
    extra   : bool
        If the attendance has to include extra attendance (default is True).

    RETURNS
    -------
    obj : dict
        Extracted information for a given page
    """

    attendance = {}
    try:
        status, attendance_details_soup = await get_attendance_html(link, 120)

        if status >= 400:
            attendance["status"] = ATTENDANCE_VCE_CRASHED

        else:
            attendance_table = attendance_details_soup.find(id="TdDispAttInfo")
            extra_attendance_table = attendance_details_soup.find(id="TdDispAdditionalAttInfo")

            attendance_stats = await attendance_scrapper(attendance_table, current)
            extra_attendance_stats = await attendance_scrapper(extra_attendance_table, extra)

            attendance = await merge_attendance(attendance_stats, extra_attendance_stats)
            attendance["status"] = ATTENDANCE_SUCCESS

        return attendance

    except TimeoutError:
        attendance["status"] = ATTENDANCE_VCE_CRASHED

    except Exception:
        attendance["status"] = ATTENDANCE_SCRAPPER_FAILED
