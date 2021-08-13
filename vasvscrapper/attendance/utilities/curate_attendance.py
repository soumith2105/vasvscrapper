async def curate_attendance(attendance, attendance_row, session_row_count, subjects, timestamps_count, timestamps):
    day_present = 0
    day_absent = 0

    #  - - in series then remove one - and shift left
    if session_row_count > timestamps_count:
        for obj_index in range(1, session_row_count):
            if attendance[f"class_{obj_index}"] == attendance[f"class_{obj_index + 1}"] == "-":
                for new_index in range(obj_index, session_row_count):
                    attendance[f"class_{new_index}"] = attendance[f"class_{new_index + 1}"]
                    attendance[f"status_{new_index}"] = attendance[f"status_{new_index + 1}"]

                del attendance[f"class_{session_row_count}"]
                del attendance[f"status_{session_row_count}"]
                session_row_count -= 1
                if session_row_count == timestamps_count:
                    break

    # only - is available then shift left
    rem = 0
    if session_row_count > timestamps_count:
        for obj_index in range(1, session_row_count + 1):
            if attendance[f"class_{obj_index - rem}"] == "-":
                for new_index in range(obj_index - rem, session_row_count - rem):
                    attendance[f"class_{new_index}"] = attendance[f"class_{new_index + 1}"]
                    attendance[f"status_{new_index}"] = attendance[f"status_{new_index + 1}"]
                del attendance[f"class_{session_row_count - rem}"]
                del attendance[f"status_{session_row_count - rem}"]
                rem += 1
                if session_row_count - rem == timestamps_count:
                    break

    for obj_index in range(1, session_row_count - 1):
        if (
            float(timestamps[f"time_{obj_index}"][1]) > float(timestamps[f"time_{obj_index + 1}"][0])
            and attendance[f"class_{obj_index}"] != "-"
            and attendance[f"class_{obj_index + 1}"] != "-"
        ):
            req = -1
            for i in range(obj_index + 1, session_row_count):
                if attendance[f"class_{i}"] == "-":
                    req = i
                    break

            for j in range(req, obj_index, -1):
                attendance[f"class_{j + 1}"], attendance[f"class_{j}"] = (
                    attendance[f"class_{j}"],
                    attendance[f"class_{j + 1}"],
                )
                attendance[f"status_{j + 1}"], attendance[f"status_{j}"] = (
                    attendance[f"status_{j}"],
                    attendance[f"status_{j + 1}"],
                )

    sessions = []
    for obj_index in range(1, session_row_count + 1):
        if attendance[f"class_{obj_index}"] != "-":
            end = f'{float(timestamps[f"time_{obj_index}"][1]) + 0.1:.2f}'
            if end[-2:] == "60":
                end = f"{float(end) + 0.4:.2f}"

            obj = {
                "subject": attendance[f"class_{obj_index}"],
                "did_attend": attendance[f"status_{obj_index}"],
                "start": timestamps[f"time_{obj_index}"][0],
                "end": end,
            }
            subjects[obj["subject"]] = subjects.get(obj["subject"], {"present": 0, "absent": 0})
            subjects[obj["subject"]]["present"] = subjects[obj["subject"]]["present"] + int(obj["did_attend"])
            subjects[obj["subject"]]["absent"] = subjects[obj["subject"]]["absent"] + int(not obj["did_attend"])
            day_present += int(obj["did_attend"])
            day_absent += int(not obj["did_attend"])
            sessions.append(obj)

    attendance_row["classes"] = sessions
    attendance_row["present"] = day_present
    attendance_row["absent"] = day_absent
    attendance_row["total"] = day_present + day_absent
    return attendance_row
