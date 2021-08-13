async def merge_attendance(attendance_rows, extra_attendance_rows):
    present = attendance_rows["present"]
    absent = attendance_rows["absent"]

    for date, sessions in extra_attendance_rows["sessions"].items():
        session_on_day = attendance_rows["sessions"].get(date, sessions)
        if session_on_day == sessions:
            present += sessions["present"]
            absent += sessions["absent"]
            for period in sessions["classes"]:
                subject = attendance_rows["subjects"].get(period["subject"], {"present": 0, "absent": 0})
                subject["present"] += period["did_attend"]
                subject["absent"] -= not period["did_attend"]
                attendance_rows["subjects"][period["subject"]] = subject
        else:
            for period in sessions["classes"]:
                merged = False
                for period_on_day in session_on_day["classes"]:
                    if (
                        period["subject"] == period_on_day["subject"]
                        and period["start"] == period_on_day["start"]
                        and period["end"] == period_on_day["end"]
                    ):
                        if period["did_attend"] != period_on_day["did_attend"] and period_on_day["did_attend"] is False:
                            present += 1
                            absent -= 1
                            period_on_day["did_attend"] = True
                            subject = attendance_rows["subjects"].get(period["subject"], {"present": 0, "absent": 0})
                            subject["present"] += 1
                            subject["absent"] -= 1
                            attendance_rows["subjects"][period["subject"]] = subject

                        merged = True

                if not merged:
                    present += period["did_attend"]
                    absent += not period["did_attend"]
                    subject = attendance_rows["subjects"].get(period["subject"], {"present": 0, "absent": 0})
                    subject["present"] += period["did_attend"]
                    subject["absent"] -= not period["did_attend"]
                    attendance_rows["subjects"][period["subject"]] = subject
                    session_on_day["classes"].append(period)

        attendance_rows["sessions"][date] = session_on_day

    total = present + absent
    percent = round((present / total) * 100, 2)

    total_attendance_stats = {
        "present": present,
        "absent": absent,
        "total": total,
        "percent": percent,
        "subjects": attendance_rows["subjects"],
        "sessions": attendance_rows["sessions"],
    }
    return total_attendance_stats
