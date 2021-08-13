from enum import Enum

from yarl import URL


class ConstEnum(Enum):
    @classmethod
    def keys(cls):
        return list(map(lambda x: x.name, cls))

    @classmethod
    def as_dict(cls):
        key_val = {}
        for item in cls:
            key_val[item.name] = item.value

        return key_val

    @classmethod
    def values(cls):
        return list(map(lambda x: x.value, cls))


class BranchesEnum(ConstEnum):
    """
    Enum representing various Branches in VCE.
    """

    CIVIL = {"name": "Civil Engineering", "branch_code": "732"}
    CSE = {"name": "Computer Science and Engineering", "branch_code": "733"}
    EEE = {"name": "Electrical and Electronics Engineering", "branch_code": "734"}
    ECE = {"name": "Electronics and Communication Engineering", "branch_code": "735"}
    MECH = {"name": "Mechanical Engineering", "branch_code": "736"}
    IT = {"name": "Information Technology", "branch_code": "737"}

    @classmethod
    def branch_name_map(cls):
        branches = {}
        for branch in cls.values():
            branches[branch["branch_code"]] = branch["name"]

        return branches


class NewsPatternsEnum(ConstEnum):
    """
    News patterns to categorize news.
    pattern repr

    - Outer parenthesis is important ()
    - If you want "time" and "table" both words to be in a news then we represent it as "time&table"
    - If you want "suppl" and "backlog" either of the word to be in news, we represent it as "suppl|backlog"
    - Group the works using parenthesis "((suppl|backlog)&(time&table))" to represent "Supplementary TimeTable" category
    """

    SUPPLEMENTARY = {"pattern": "(suppl|backlog|makeup)", "key": "Supplementary"}
    EXAMINATION = {"pattern": "(exam|test|internal)", "key": "Examination"}
    TIMETABLE = {"pattern": "(time&table)", "key": "Timetable"}
    REVALUATION = {"pattern": "(revaluation)", "key": "Revaluation"}
    RESULT = {"pattern": "(result)", "key": "Result"}
    ADMISSION = {"pattern": "(admission)", "key": "Admission"}
    FEE = {"pattern": "(fee)", "key": "Fee"}
    OPEN_ELECTIVE = {"pattern": "(open&elective)", "key": "Open Elective"}
    INFORMATION = {"pattern": "$REMAINING", "key": "Information"}

    @classmethod
    def get_news_keys(cls):
        return list(map(lambda x: x.value["key"], cls))


class LoginUrlEnum(ConstEnum):
    """
    Enum representing success and failure urls in VCE.
    """

    SUCCESS = URL("https://vce.ac.in/student_info.aspx")
    FAIL = URL("https://vce.ac.in/")
