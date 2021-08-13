from asyncio.exceptions import TimeoutError

from vasvscrapper.network_requests import get_results_html
from vasvscrapper.results.utilities import result_scrapper
from vasvscrapper.status_codes.results import RESULT_SCRAPPER_FAILED, RESULT_SUCCESS, RESULT_VCE_CRASHED


async def get_result(link: str) -> dict:
    """
    Extracts the results information and return a dictionary.

    PARAMETERS
    ----------
    link    : str
        Link of the result page

    RETURNS
    -------
    obj : dict
        Extracted information for a given page
    """

    results = {}
    try:
        status, result_details_soup = await get_results_html(link, 120)
        if status >= 400:
            results["status"] = RESULT_VCE_CRASHED

        else:
            subject_marks, semester_marks = await result_scrapper(result_details_soup)
            results["subjects"] = subject_marks
            results["total"] = semester_marks
            results["status"] = RESULT_SUCCESS

        return results

    except TimeoutError:
        results["status"] = RESULT_VCE_CRASHED
        return results

    except Exception:
        results["status"] = RESULT_SCRAPPER_FAILED
        return results
