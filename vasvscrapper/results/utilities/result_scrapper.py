import asyncio


async def semester_marks_scrapper(marks_rows, headings, headings_main):
    total = {}
    for heading in headings:
        total[heading] = 0

    for heading in headings_main:
        total[heading] = 0

    marks_row = marks_rows[-2].find_all("td")
    p = 0
    for j in marks_row[1:-3]:
        if j.text == "-":
            inner_entry = 0
        elif j.text == "Ab" or j.text == "A":
            inner_entry = -1
        else:
            inner_entry = j.text
        total[f"{headings[p]}"] = float(inner_entry)
        p += 1
    total["ext_sub_credits"] = int(marks_row[-2].text)
    total["ext_grade_pts"] = int(marks_row[-1].text)
    marks_row = marks_rows[-1].find_all("td")
    p = 0
    for j in marks_row[1:-1]:
        if j.text == "-":
            inner_entry = 0
        elif j.text == "Ab" or j.text == "A":
            inner_entry = -1
        else:
            inner_entry = j.text
        total[f"{headings_main[p]}"] = float(inner_entry)
        p += 1

    if marks_row[-1].text.split()[-1] != "-":
        total["sgpa"] = float(marks_row[-1].text.split()[-1])
    else:
        total["sgpa"] = None

    return total


async def subject_marks_scrapper(marks_rows, headings):
    subjects = {}
    for mark in marks_rows[3:-2]:
        marks_row = mark.find_all("td")
        sub = {}
        for heading in headings:
            sub[heading] = 0
        p = 0
        for j in marks_row[2:-3]:
            if j.text == "-":
                inner_entry = 0
            elif j.text == "Ab" or j.text == "A":
                inner_entry = -1
            else:
                inner_entry = j.text
            sub[f"{headings[p]}"] = float(inner_entry)
            p += 1
        if marks_row[-3].text != "-":
            sub["ext_grade"] = marks_row[-3].text
        else:
            sub["ext_grade"] = "NA"
        sub["ext_sub_credits"] = int(marks_row[-2].text)
        sub["ext_grade_pts"] = int(marks_row[-1].text)
        subjects[marks_row[1].text.split("(")[0]] = sub

    return subjects


async def result_scrapper(result_details_soup):
    result_inner = result_details_soup.find(id="pnlContents")
    subject_marks_soup = result_inner.find_all(class_="tableclass")[1]
    headings = []
    headings_main = []
    marks_rows = subject_marks_soup.find_all("tr")
    for marks_row in marks_rows[1].find_all("td")[2:-2]:
        for i in range(1, 3):
            if marks_row.text.split()[0] == f"Int{i}":
                headings.append(f"int{i}_max")
                headings.append(f"int{i}")
                headings_main.append(f"int{i}_per")

        for i in range(1, 4):
            if marks_row.text.split()[0] == f"Asst{i}":
                headings.append(f"assn{i}_max")
                headings.append(f"assn{i}")
                headings_main.append(f"assn{i}_per")

            if marks_row.text.split()[0] == f"Quiz{i}":
                headings.append(f"quiz{i}_max")
                headings.append(f"quiz{i}")
                headings_main.append(f"quiz{i}_per")
    headings.append("sess_max")
    headings.append("sess")
    headings_main.append("sess_per")
    result = await asyncio.gather(
        subject_marks_scrapper(marks_rows=marks_rows, headings=headings),
        semester_marks_scrapper(marks_rows=marks_rows, headings=headings, headings_main=headings_main),
    )
    return result
