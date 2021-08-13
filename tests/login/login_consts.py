from bs4 import BeautifulSoup

login_soup = BeautifulSoup(
    """
<!DOCTYPE html>
<html lang="en">
<head>
<title></title>
<!-- Basic Page Needs
    ================================================== -->
<meta charset="utf-8"/>
<title>Vasavi College of Engineering, Hyderabad, India.</title>
<meta content="index, follow" name="robots"/>
<meta content="" name="keywords"/>
<meta content="" name="description"/>
<meta content="" name="author"/>
<!-- Mobile Specific Metas
    ================================================== -->
<meta content="width=device-width, initial-scale=1, maximum-scale=1" name="viewport"/>
<!-- CSS
    ================================================== -->
<link href="http://fonts.googleapis.com/css?family=Ubuntu:400,700,500,300,400italic,300italic" rel="stylesheet" type="text/css"/>
<link href="styles/style.css" rel="stylesheet"/>
<link href="styles/inner.css" rel="stylesheet"/>
<link href="styles/layout.css" rel="stylesheet"/>
<link href="styles/layerslider.css" rel="stylesheet"/>
<link href="styles/color.css" rel="stylesheet"/>
<!--[if lt IE 9]>
        <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->
<!-- Favicons
    ================================================== -->
<link href="images/favicon.ico" rel="shortcut icon"/>
<script language="JavaScript" type="text/javascript">
          function popUp(URL) {
              eval("page" + " = window.open(URL, '" + "', 'toolbar=0,scrollbars=1,location=0,statusbar=1,menubar=0,resizable=1,width=995,height=495,');");
          }

    </script>
<style>
        td {text-align:left;}
    </style>
</head>
<body>
<form action="./student_info.aspx" id="studForm" method="post">
<input id="__VIEWSTATE" name="__VIEWSTATE" type="hidden" value="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"/>
<input id="__VIEWSTATEGENERATOR" name="__VIEWSTATEGENERATOR" type="hidden" value="637939EB"/>
<input id="__EVENTVALIDATION" name="__EVENTVALIDATION" type="hidden" value="keDN/awMJtX3I1hIobfGHGw39etfpSyb2ikhBPCn4/PnAMpLgXWPfm69sKi5e5znqq6HCmj+3nhmJGt0g9+FHM0td9B6SMJX5KMEvk9CXgxFCHkBEcrKBmKC15jvWNH4"/>
<div id="bodychild">
<div id="outercontainer">
<div id="outermain">
<div class="container">
<div class="row">
<section class="twelve columns" id="maincontent">
<table>
<tr>
<td> <h2>Student Information</h2></td>
<!--<td width="55%">
<a href="/Technical_Skills/TS_2019.aspx" target="_blank">
    <h3 style="color:mediumvioletred; font-weight:bold">
        <img src="New.gif" alt="new" />Proposal for Technical Training and CRT for VI Semester Students (2019-2020)</h3>
</a>
&nbsp;</td>-->
<td> <input id="ibLogOut" name="ibLogOut" src="img/logout_button.png" type="image"/></td>
</tr>
<tr>
</tr>
</table>
<div id="divStudInfo"><table><tr><td></td><td></td></tr><tr><td>Hall Ticket No.</td><td>1602-17-737-046</td></tr><tr><td scope="col">Name</td><td>PODDUTURI SOUMITH REDDY</td></tr><tr><td>Date of Birth</td><td>21-May-1999</td></tr><tr><td>Father Name</td><td>PODDUTURI SRINIVAS REDDY</td></tr><tr><td>Admission Date</td><td>05-Aug-2017</td></tr><tr><td>Branch </td><td>BE - Information Technology</td></tr><tr><td>Year</td><td>4</td></tr><tr><td>Semester</td><td>8</td></tr><tr><td>Section</td><td>A</td></tr></table></div>
<div id="divAttSummary"><table><tr><th> Year</th><th>Sem.</th><th>Academic Year</th><th>Status</th><th>Class Start Date</th><th>Class End Date</th><th>Att. %</th> <th> Marks</th></tr><tr><td align="center">4</td><td align="center">8</td><td align="center">2020 - 2021</td><td align="center">-</td><td align="center">15-Mar-2021</td><td align="center">01-Jul-2021</td><td align="center"><a href="javascript:void(0)" id="showattendencepercentage&lt;a" onclick="popUp('http://erp.vce.ac.in/studentservicenew/ShowSemWiseAttendanceDetails.aspx?sem8')">View</a></td><td><a href="javascript:void(0)" onclick="popUp('http://erp.vce.ac.in/studentservicenew/StudentSemWiseMarks.aspx?sem8')">View</a></td></tr><tr><td align="center">4</td><td align="center">7</td><td align="center">2020 - 2021</td><td align="center">-</td><td align="center">31-Aug-2020</td><td align="center">15-Dec-2020</td><td align="center"><a href="javascript:void(0)" id="showattendencepercentage&lt;a" onclick="popUp('http://erp.vce.ac.in/studentservicenew/ShowSemWiseAttendanceDetails.aspx?sem7')">View</a></td><td><a href="javascript:void(0)" onclick="popUp('http://erp.vce.ac.in/studentservicenew/StudentSemWiseMarks.aspx?sem7')">View</a></td></tr><tr><td align="center">3</td><td align="center">6</td><td align="center">2019 - 2020</td><td align="center">-</td><td align="center">06-Jan-2020</td><td align="center">16-May-2020</td><td align="center"><a href="javascript:void(0)" id="showattendencepercentage&lt;a" onclick="popUp('http://erp.vce.ac.in/studentservicenew/ShowSemWiseAttendanceDetails.aspx?sem6')">View</a></td><td><a href="javascript:void(0)" onclick="popUp('http://erp.vce.ac.in/studentservicenew/StudentSemWiseMarks.aspx?sem6')">View</a></td></tr><tr><td align="center">3</td><td align="center">5</td><td align="center">2019 - 2020</td><td align="center">-</td><td align="center">22-Jul-2019</td><td align="center">23-Nov-2019</td><td align="center"><a href="javascript:void(0)" id="showattendencepercentage&lt;a" onclick="popUp('http://erp.vce.ac.in/studentservicenew/ShowSemWiseAttendanceDetails.aspx?sem5')">View</a></td><td><a href="javascript:void(0)" onclick="popUp('http://erp.vce.ac.in/studentservicenew/StudentSemWiseMarks.aspx?sem5')">View</a></td></tr><tr><td align="center">2</td><td align="center">4</td><td align="center">2018 - 2019</td><td align="center">-</td><td align="center">31-Dec-2018</td><td align="center">24-Apr-2019</td><td align="center"><a href="javascript:void(0)" id="showattendencepercentage&lt;a" onclick="popUp('http://erp.vce.ac.in/studentservicenew/ShowSemWiseAttendanceDetails.aspx?sem4')">View</a></td><td><a href="javascript:void(0)" onclick="popUp('http://erp.vce.ac.in/studentservicenew/StudentSemWiseMarks.aspx?sem4')">View</a></td></tr><tr><td align="center">2</td><td align="center">3</td><td align="center">2018 - 2019</td><td align="center">-</td><td align="center">23-Jul-2018</td><td align="center">17-Nov-2018</td><td align="center"><a href="javascript:void(0)" id="showattendencepercentage&lt;a" onclick="popUp('http://erp.vce.ac.in/studentservicenew/ShowSemWiseAttendanceDetails.aspx?sem3')">View</a></td><td><a href="javascript:void(0)" onclick="popUp('http://erp.vce.ac.in/studentservicenew/StudentSemWiseMarks.aspx?sem3')">View</a></td></tr><tr><td align="center">1</td><td align="center">2</td><td align="center">2017 - 2018</td><td align="center">-</td><td align="center">16-Jan-2018</td><td align="center">05-May-2018</td><td align="center"><a href="javascript:void(0)" id="showattendencepercentage&lt;a" onclick="popUp('http://erp.vce.ac.in/studentservicenew/ShowSemWiseAttendanceDetails.aspx?sem2')">View</a></td><td><a href="javascript:void(0)" onclick="popUp('http://erp.vce.ac.in/studentservicenew/StudentSemWiseMarks.aspx?sem2')">View</a></td></tr><tr><td align="center">1</td><td align="center">1</td><td align="center">2017 - 2018</td><td align="center">-</td><td align="center">05-Aug-2017</td><td align="center">01-Dec-2017</td><td align="center"><a href="javascript:void(0)" id="showattendencepercentage&lt;a" onclick="popUp('http://erp.vce.ac.in/studentservicenew/ShowSemWiseAttendanceDetails.aspx?sem1')">View</a></td><td><a href="javascript:void(0)" onclick="popUp('http://erp.vce.ac.in/studentservicenew/StudentSemWiseMarks.aspx?sem1')">View</a></td></tr></table><p></p><center><span style="color:red"><em>This information is provided to the candidate on his/her online request and is only a prototype list</em></span></center></div>
<br/><br/>
<div>
</div>
<div id="divStudySummary">
</div>
<div id="divNavigation">
</div>
</section>
</div>
</div>
</div>
<!-- END MAIN CONTENT -->
<div class="clear"></div><!-- clear float -->
</div><!-- end outercontainer -->
</div><!-- end bodychild -->
</form>
</body>
</html>""",
    "lxml",
)

expected_login_result = {
    "roll_number": "1602-17-737-046",
    "name": "Podduturi Soumith Reddy",
    "dob": "21-May-1999",
    "fathers_name": "PODDUTURI SRINIVAS REDDY",
    "admission_date": "05-Aug-2017",
    "branch": "Information Technology",
    "current_year": 4,
    "current_status": "",
    "current_sem": 8,
    "section": "A",
    "semesters": [
        {
            "sem": 8,
            "year": "2020 - 2021",
            "status": "-",
            "start_date": "2021-03-15",
            "end_date": "2021-07-01",
            "attendance_link": "http://erp.vce.ac.in/studentservicenew/ShowSemWiseAttendanceDetails.aspx?sem8",
            "result_link": "http://erp.vce.ac.in/studentservicenew/StudentSemWiseMarks.aspx?sem8",
        },
        {
            "sem": 7,
            "year": "2020 - 2021",
            "status": "-",
            "start_date": "2020-08-31",
            "end_date": "2020-12-15",
            "attendance_link": "http://erp.vce.ac.in/studentservicenew/ShowSemWiseAttendanceDetails.aspx?sem7",
            "result_link": "http://erp.vce.ac.in/studentservicenew/StudentSemWiseMarks.aspx?sem7",
        },
        {
            "sem": 6,
            "year": "2019 - 2020",
            "status": "-",
            "start_date": "2020-01-06",
            "end_date": "2020-05-16",
            "attendance_link": "http://erp.vce.ac.in/studentservicenew/ShowSemWiseAttendanceDetails.aspx?sem6",
            "result_link": "http://erp.vce.ac.in/studentservicenew/StudentSemWiseMarks.aspx?sem6",
        },
        {
            "sem": 5,
            "year": "2019 - 2020",
            "status": "-",
            "start_date": "2019-07-22",
            "end_date": "2019-11-23",
            "attendance_link": "http://erp.vce.ac.in/studentservicenew/ShowSemWiseAttendanceDetails.aspx?sem5",
            "result_link": "http://erp.vce.ac.in/studentservicenew/StudentSemWiseMarks.aspx?sem5",
        },
        {
            "sem": 4,
            "year": "2018 - 2019",
            "status": "-",
            "start_date": "2018-12-31",
            "end_date": "2019-04-24",
            "attendance_link": "http://erp.vce.ac.in/studentservicenew/ShowSemWiseAttendanceDetails.aspx?sem4",
            "result_link": "http://erp.vce.ac.in/studentservicenew/StudentSemWiseMarks.aspx?sem4",
        },
        {
            "sem": 3,
            "year": "2018 - 2019",
            "status": "-",
            "start_date": "2018-07-23",
            "end_date": "2018-11-17",
            "attendance_link": "http://erp.vce.ac.in/studentservicenew/ShowSemWiseAttendanceDetails.aspx?sem3",
            "result_link": "http://erp.vce.ac.in/studentservicenew/StudentSemWiseMarks.aspx?sem3",
        },
        {
            "sem": 2,
            "year": "2017 - 2018",
            "status": "-",
            "start_date": "2018-01-16",
            "end_date": "2018-05-05",
            "attendance_link": "http://erp.vce.ac.in/studentservicenew/ShowSemWiseAttendanceDetails.aspx?sem2",
            "result_link": "http://erp.vce.ac.in/studentservicenew/StudentSemWiseMarks.aspx?sem2",
        },
        {
            "sem": 1,
            "year": "2017 - 2018",
            "status": "-",
            "start_date": "2017-08-05",
            "end_date": "2017-12-01",
            "attendance_link": "http://erp.vce.ac.in/studentservicenew/ShowSemWiseAttendanceDetails.aspx?sem1",
            "result_link": "http://erp.vce.ac.in/studentservicenew/StudentSemWiseMarks.aspx?sem1",
        },
    ],
}


before_get_value = map(
    lambda x: BeautifulSoup(x, "html.parser"),
    [
        "<tr><td>Hall Ticket No.</td><td>1602-17-737-046</td></tr>",
        'r><td scope="col">Name</td><td>PODDUTURI SOUMITH REDDY</td></tr>',
        "<tr><td>Date of Birth</td><td>21-May-1999</td></tr>",
        "<tr><td>Father Name</td><td>PODDUTURI SRINIVAS REDDY</td></tr>",
        "<tr><td>Admission Date</td><td>05-Aug-2017</td></tr>",
        "<tr><td>Branch </td><td>BE - Information Technology</td></tr>",
        "<tr><td>Year</td><td>4</td></tr>",
        "<tr><td>Semester</td><td>8</td></tr>",
        "<tr><td>Section</td><td>A</td></tr>",
    ],
)

after_get_value = {
    "roll_number": "1602-17-737-046",
    "name": "Podduturi Soumith Reddy",
    "dob": "21-May-1999",
    "fathers_name": "PODDUTURI SRINIVAS REDDY",
    "admission_date": "05-Aug-2017",
    "branch": "Information Technology",
    "current_year": 4,
    "current_status": "",
    "current_sem": 8,
    "section": "A",
}

before_curate = {
    "roll_number": "1602-17-737-046",
    "name": "PODDUTURI SOUMITH REDDY",
    "dob": "21-May-1999",
    "fathers_name": "PODDUTURI SRINIVAS REDDY",
    "admission_date": "05-Aug-2017",
    "branch": "BE - Information Technology",
    "current_year": "4",
    "current_status": "",
    "current_sem": "8",
    "section": "A",
}

after_curate = {
    "roll_number": "1602-17-737-046",
    "name": "Podduturi Soumith Reddy",
    "dob": "21-May-1999",
    "fathers_name": "PODDUTURI SRINIVAS REDDY",
    "admission_date": "05-Aug-2017",
    "branch": "Information Technology",
    "current_year": 4,
    "current_status": "",
    "current_sem": 8,
    "section": "A",
}
