from datetime import datetime

from vasvscrapper.enums import BranchesEnum

labels_map = {
    "Hall Ticket No.": "roll_number",
    "Name": "name",
    "Date of Birth": "dob",
    "Father Name": "fathers_name",
    "Admission Date": "admission_date",
    "Branch": "branch",
    "Year": "current_year",
    "Status": "current_status",
    "Semester": "current_sem",
    "Section": "section",
}


def curate_values(result: dict):
    branches = BranchesEnum.branch_name_map()

    for label, value in result.items():
        if label in ["current_year", "current_sem"]:
            result[label] = int(value)

        elif label in ["name"]:
            result[label] = value.title()

        elif label == "branch":
            result[label] = branches.get(result["roll_number"][8:11], result["branch"])

        elif value == "-":
            result[label] = ""

    return result


def get_values_by_labels(student_obj):
    result = dict.fromkeys(labels_map.values(), "")

    for obj in student_obj:
        label = labels_map[obj("td")[0].text.strip()]
        value = obj("td")[1].text.strip()

        result[label] = value

    return curate_values(result)


async def login_scrapper(profile_page_soup):
    semesters = []
    student_details_block = profile_page_soup.find(id="divStudInfo")
    student_details_links = profile_page_soup.find(id="divAttSummary")

    student_info = student_details_block("tr")[1:]
    attendance_links_rows = student_details_links("tr")

    user = get_values_by_labels(student_info)

    for i in attendance_links_rows[1:]:
        semesters.append(
            {
                "sem": int(i("td")[1].text),
                "year": i("td")[2].text,
                "status": i("td")[3].text,
                "start_date": datetime.strptime(i("td")[4].text, "%d-%b-%Y").strftime("%Y-%m-%d"),
                "end_date": datetime.strptime(i("td")[5].text, "%d-%b-%Y").strftime("%Y-%m-%d"),
                "attendance_link": i("td")[-2]("a")[0].attrs.get("onclick", "href")[7:-2],
                "result_link": i("td")[-1]("a")[0].attrs.get("onclick", "href")[7:-2],
            }
        )

    user["semesters"] = semesters
    return user
