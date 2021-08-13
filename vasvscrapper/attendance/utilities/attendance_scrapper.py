import datetime

from vasvscrapper.attendance.utilities.curate_attendance import curate_attendance


async def get_timestamps(date_row):
    timestamps = {}
    timestamps_rows = date_row("tr")[0]
    timestamps_count = 0
    for i in timestamps_rows("td")[3:-1]:
        timestamps_count += 1
        timestamps[f"time_{timestamps_count}"] = [k.strip() for k in i.text.split("-")]
    return timestamps, timestamps_count


async def attendance_scrapper(attendance_table, current=False, extra=False):
    row_split = 2
    col_split = -3

    if extra:
        row_split = 1
        col_split = -1

    stats = {
        "present": 0,
        "absent": 0,
        "subjects": {},
        "sessions": {},
    }
    if attendance_table is not None and (current or extra):
        classes_rows = attendance_table("tr")[row_split:]
        subjects = {}

        present = 0
        absent = 0

        timestamps, timestamps_count = await get_timestamps(attendance_table)

        attendance_rows = {}
        for i in classes_rows:

            if int(i("td")[-1].text) != 0:
                current_date = datetime.datetime.strptime(i("td")[2].text, "%d-%b-%Y").date()
                attendance_row = {"present": 0, "absent": 0, "total": 0, "classes": []}
                attendance = {}

                k = 0
                for j in i("td")[3:col_split]:
                    colspan = int(j.attrs.get("colspan", 1))
                    if colspan in [1, 2, 3, 4, 5, 6]:
                        for _ in range(colspan):
                            k += 1
                            attendance[f"class_{k}"] = j.text.strip().split("(")[0]
                            if j.attrs.get("bgcolor") == "Dodgerblue" or j.attrs.get("bgcolor") == "Green":
                                attendance[f"status_{k}"] = False
                            else:
                                attendance[f"status_{k}"] = True

                attendance_row = await curate_attendance(
                    attendance, attendance_row, k, subjects, timestamps_count, timestamps
                )
                present += attendance_row["present"]
                absent += attendance_row["absent"]
                attendance_rows[current_date] = attendance_row

        total = present + absent
        if total > 0:
            stats = {
                "present": present,
                "absent": absent,
                "subjects": subjects,
                "sessions": attendance_rows,
            }

    return stats
