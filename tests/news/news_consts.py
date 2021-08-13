from bs4 import BeautifulSoup

news_soup = BeautifulSoup(
    """
<!DOCTYPE html>
<!--[if lt IE 7 ]><html class="ie ie6" lang="en"> <![endif]--><!--[if IE 7 ]><html class="ie ie7" lang="en"> <![endif]--><!--[if IE 8 ]><html class="ie ie8" lang="en"> <![endif]--><!--[if (gte IE 9)|!(IE)]><!--><html lang="en">
<!--<![endif]-->
<head>
<!-- Basic Page Needs
================================================== -->
<meta charset="utf-8"/>
<title>Vasavi College of Engineering, Hyderabad, India.</title>
<meta content="index, follow" name="robots"/>
<meta content="" name="keywords"/>
<meta content="" name="description"/>
<meta content="" name="author"/>
<meta content="public" http-equiv="Cache-control"/>
<!-- Mobile Specific Metas
================================================== -->
<meta content="width=device-width, initial-scale=1, maximum-scale=1" name="viewport"/>
<!-- CSS  ================================================== -->
<link href="https://fonts.googleapis.com/css?family=Ubuntu:400,700,500,300,400italic,300italic" rel="stylesheet" type="text/css"/>
<link href="../../styles/style.css" rel="stylesheet"/>
<link href="https://vce.ac.in/styles/inner.css" rel="stylesheet"/>
<link href="../../styles/layout.css" rel="stylesheet"/>
<link href="https://vce.ac.in/styles/layerslider.css" rel="stylesheet"/>
<link href="https://vce.ac.in/styles/color.css" rel="stylesheet"/>
<link href="https://vce.ac.in/styles/prettyPhoto.css" media="screen" rel="stylesheet"/>
<link href="/styles/responsive-tables.css" rel="stylesheet"/>
<!--[if lt IE 9]>
<script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
<![endif]-->
<!-- Favicons
================================================== -->
<link href="https://vce.ac.in/images/favicon.ico" rel="shortcut icon"/>
<script src="https://vce.ac.in/js/jquery-1.7.1.min.js" type="text/javascript"></script>
<link href="https://vce.ac.in/src/material-scrolltop.css" rel="stylesheet" type="text/css"/>
</head>
<body>
<div id="bodychild">
<!-- HEADER -->
<style>
.header {
font-family: 'Oswald', sans-serif;
color: darkblue;
}

.subheader {
font-family: 'Nunito', sans-serif;
color: #838586;
font-size: 80%;
}

.validation-summary-errors {
border: 2px solid red;
color: red;
font-weight: bold;
margin: 6px;
width: 30%;
}

.field-validation-error {
color: red;
font-weight: bold;
/* background-color: yellow;*/
}

.input-validation-error {
color: red;
font-weight: bold;
background-color: pink;
}

/* newshow */

#newsshow {
position: relative;
z-index: 10;
margin: 25px 0;
padding: 10px;
}
/*border:1px solid #efefef;*/
</style>
<link href="https://fonts.googleapis.com/css?family=Oswald:700" rel="stylesheet" type="text/css"/>
<link href="https://fonts.googleapis.com/css?family=Nunito" rel="stylesheet" type="text/css"/>
<div id="outerheader">
<header>
<div id="top">
<div class="container">
<div class="row">
<div class="twelve columns" id="topmenu">
</div>
</div>
</div>
</div>
<div id="logo-wrapper">
<div class="container">
<div class="row">
<div class="six columns" id="logo" style="text-align:center;">
<img alt="Vasavi College of Engineering" src="/img/vlogo.gif" width="90"/>
<h1 style="font-family: 'oswd', sans-serif; font-weight:bold; font-size:25px;">   Vasavi College of Engineering</h1>
<em> (Private Un-aided Non-minority Autonomous Institution)<br/>
<span style="color:red; font-weight:bold;"> ACCREDITED BY NAAC WITH 'A++' GRADE</span><br/>
        Affiliated to Osmania University and Approved by AICTE.</em><br/>
</div>
<div class="right five columns">
<form action="#" id="loginForm" method="post">
<div class="header-wrapper">
<h2 style="font-weight:bold;">Student/Parent Login</h2><span></span>
<div class="clear"></div>
</div>
<input class="text-input" id="LoginID" name="LoginID" onblur="if (this.value == '')this.value = 'LoginID';" onfocus="if (this.value == 'LoginID')this.value = '';" type="text" value="LoginID"/>
<input class="text-input" id="Password" name="Password" onblur="if (this.value == '')this.value = 'PassWord';" onfocus="if (this.value == 'Password')this.value = '';" type="password" value="Password"/>
<span class="field-validation-valid" data-valmsg-for="LoginID" data-valmsg-replace="true"></span>
<span class="field-validation-valid" data-valmsg-for="PassWord" data-valmsg-replace="true"></span>
<input class="button field" type="submit" value="Login"/>
</form>
<span style="color:red;"><strong></strong></span>
<div class="clear"></div>
</div>
</div>
</div>
</div>
<section id="navigation">
<script crossorigin="anonymous" src="https://kit.fontawesome.com/18f1ba0b5e.js"></script>
<div class="container">
<div class="row">
<nav class="twelve columns" id="nav-wrap">
<ul class="sf-menu" id="sf-nav">
<li><a href="../../Default.cshtml">Home</a></li>
<li>
<a href="#">About</a>
<ul>
<li><a href="../../About/Founder.cshtml">Founder</a></li>
<li><a href="../../About/Academy.cshtml">Vasavi Academy of Education</a></li>
<li><a href="../../About/College/About_College.cshtml">College</a></li>
<li><a href="../../About/Organogram.cshtml">Organogram</a></li>
<li><a class="dropdown" href="../../About/Bog.cshtml">Board of Governors</a></li>
<li><a href="../../About/Principal.cshtml">Principal</a></li>
<li><a class="dropdown" href="/About/Strategic_Plan.cshtml">Strategic Plan</a></li>
<li><a class="dropdown" href="/About/Annaul_Report.cshtml">Annual Reports</a></li>
</ul>
</li>
<li>
<a href="#">Academics</a>
<ul>
<li><a class="dropdown" href="../../Academics/Academic_Council.cshtml">Academic Council</a></li>
<li>
<a href="/Academics/Almanac.cshtml?Branch=BE">Almanac</a>
</li>
<li><a href="/Academics/Activity_Calendar.cshtml">Activity Calendar</a></li>
<li><a href="/Academics/Administrative_Manual.cshtml">Administrative Manual</a></li>
<li><a href="/Academics/Examination_Cell/COE.cshtml">Examinations (CIE &amp; SEE)</a></li>
<li><a class="dropdown" href="../../Academics/Courses_Offered.cshtml">Courses Offered</a></li>
<li>
<a class="dropdown" href="#">ME Programmes</a>
<ul>
<li><a class="dropdown" href="../../Academics/ME_ESVLSI.cshtml">Embedded Systems &amp; VLSI Design</a></li>
<li><a class="dropdown" href="../../Academics/ME_CESP.cshtml">Comm. Engg. &amp; Signal Processing</a></li>
<li><a class="dropdown" href="../../Academics/ME_ADM.cshtml">Advanced Design &amp; Manufacturing</a> </li>
<li><a class="dropdown" href="../../Academics/ME_CSE.cshtml">Computer Science &amp; Engineering</a> </li>
<li><a class="dropdown" href="../../Academics/ME_PSPE.cshtml">Power Systems &amp; Power Electronics</a></li>
</ul>
</li>
<li><a href="/Academics/Public_Holidays.cshtml">Public holidays-2021</a></li>
<li><a href="../../Academics/Syllabus/Syllabus">Syllabus</a></li>
<li>
<a class="dropdown" href="../../Academics/VAC.cshtml">Value-Added Courses</a>
</li>
<li><a href="/Roll_of_Honour.cshtml">Roll of Honour</a></li>
<li><a href="/Academics/University_Ranks.cshtml">University Ranks</a></li>
<li><a href="/BOS/BOS.cshtml">Board of Studies</a></li>
<li>
<a href="/Academics/Commitees/Admissions_Committee.cshtml">Committees</a>
</li>
<li>
<a href="/Academics/CO_PO_Mapping_Mech.cshtml">PO and PSO attainment</a>
</li>
</ul>
</li>
<li>
<a href="#">Admissions</a>
<ul>
<li><a href="/Admissions/Downloads/Admission_Manual.pdf">Admissions Manual</a></li>
<li><a href="/Admissions/Admissions_Analysis.cshtml?ay=2018-2019">Admission Analysis</a></li>
<li>
<a class="dropdown" href="/Admissions/EAMCET_Cutoff.cshtml?ay=2019">TSEAMCET cutoff Ranks</a>
</li>
<li>
<a class="dropdown" href="/Admissions/JEE_Cutoff.cshtml"> JEE (Mains) AIR cutoff Ranks (Category B)</a>
</li>
</ul>
</li>
<li><a href="http://www.vcealumni.org/">Alumni</a></li>
<li>
<a href="#">Campus Life</a>
<ul>
<li><a href="../../CampusLife/Acumen.cshtml">Acumen - Technical Symposium </a></li>
<li><a href="../../CampusLife/Extramural.cshtml">Extramural Engagements</a></li>
<li><a href="../../CampusLife/ECA_Clubs.cshtml">Extra Curricular Activities [Clubs] </a></li>
<li><a href="../../CampusLife/Euphoria.cshtml">Euphoria - Cultural Fete</a></li>
<li><a href="https://edu.ieee.org/in-vce/">IEEE - Student Branch</a></li>
<li><a href="../../CampusLife/ISTE.cshtml">ISTE Chapter  </a></li>
<li><a href="../../CampusLife/Kriti.cshtml">Kriti - Annual Art Exhibition </a></li>
<li><a href="../../NSS/ABout_NSS.cshtml">National Service Scheme [NSS] </a></li>
<li><a href="../../CampusLife/Street_Cause.cshtml">Street Cause </a></li>
<li><a href="../../CampusLife/Swayam.cshtml">Swayam - Entrepreneurship Cell</a></li>
<li><a href="/CampusLife/GENDER_EQUITY_PROGRAMS.cshtml">Gender Equity</a></li>
<li><a href="../../CampusLife/DownLoads/EQUITY_ACTION_PLAN.pdf">Equity Action Plan</a></li>
<li>
<a href="/CampusLife/Professional_Bodies/About_Professional_Bodies.cshtml">Professional Bodies</a>
</li>
<li> <a href="/CampusLife/Women_Development_Cell.cshtml">Women Development Cell</a></li>
<li><a href="../../CampusLife/Traditional_Day.cshtml">Traditional Day</a></li>
</ul>
</li>
<li>
<a href="#">Facilities</a>
<ul>
<li><a href="../../Facilities/Bank.cshtml">Bank</a></li>
<li><a href="../../Facilities/cafeteria.cshtml">Cafeteria</a></li>
<li><a href="../../Facilities/CC/About_CC.cshtml">Computer Center</a></li>
<li><a href="../../Facilities/Divyangjan.cshtml">Divyangjan Facilities </a></li>
<li><a href="../../Facilities/Media_center.cshtml">Media Center (e-content) </a></li>
<li><a href="../../Facilities/Common_Rooms.cshtml">Common Rooms </a></li>
<li><a href="../../Facilities/ICT_Class_Rooms.cshtml">Smart, ICT enabled classrooms and seminar halls</a></li>
<li>
<a href="#">Green Initiatives </a>
<ul style="top: 31px; visibility: visible; left: 0px; width: 250px; display: none;">
<li><a class="dropdown" href="/Facilities/Green_Practices.cshtml">Green Practices</a></li>
<li><a class="dropdown" href="/Facilities/Solar/Solar.cshtml">Solar Panels</a></li>
<li><a class="dropdown" href="/Facilities/LED.cshtml">LED</a></li>
<li><a class="dropdown" href="/Facilities/Waste_Management/Solid_Waste.cshtml">Waste Management</a></li>
<li><a class="dropdown" href="/Facilities/Rain_Water.cshtml">Rain Water Harvesting Pits</a></li>
</ul>
</li>
<li><a href="/Facilities/GamesnSports/About_GamesnSports.cshtml">Games and Sports</a></li>
<li><a href="../../Facilities/Language_Labs.cshtml">Language Labs</a></li>
<li><a href="../../Facilities/Library/About_Library.cshtml">Library</a></li>
<li>
<a href="../../Facilities/Maintenance_Cell.cshtml">
                Maintenance cell
            </a>
</li>
<li><a href="../../Facilities/Medical_Facility.cshtml">Medical Facility</a></li>
<li>
<a href="#"> Counseling</a>
<ul style="top: 31px; visibility: visible; left: 0px; width: 250px; display: none;">
<li><a class="dropdown" href="/Counselling/Mentorship_Cell/About_Mentorship.cshtml">Mentorship cell</a></li>
<li><a class="dropdown" href="/Facilities/Career_Counseling.cshtml">Career Counseling</a></li>
<li><a class="dropdown" href="/Facilities/#">Personal Counseling</a></li>
</ul>
</li>
<li><a href="../../Facilities/Transport.cshtml">Transport</a></li>
<li>
<a href="#">Safety Measures</a>
<ul style="top: 31px; visibility: visible; left: 0px; width: 250px; display: none;">
<li><a class="dropdown" href="/Facilities/Fire_Safety.cshtml">Fire Safety</a></li>
<li><a class="dropdown" href="/Facilities/Earthing.cshtml">Earthing</a></li>
<li><a class="dropdown" href="/Facilities/Drive_Safely.cshtml">Drive Safely</a></li>
</ul>
</li>
</ul>
</li>
<li>
<a href="#">Departments</a>
<ul>
<li><a href="../../Departments/Civil/About_Civil_Dept.cshtml">Civil Engineering</a></li>
<li><a href="../../Departments/CSE/About_CSE_Dept.cshtml">Computer Science &amp; Engg.</a></li>
<li><a href="../../Departments/ECE/About_ECE_Dept.cshtml">Electronics &amp; Communication </a></li>
<li><a href="../../Departments/EEE/About_EEE_Dept.cshtml">Electrical &amp; Electronics Engg.</a></li>
<li><a href="../../Departments/MECH/About_MECH_Dept.cshtml">Mechanical Engineering</a></li>
<li><a href="../../Departments/IT/About_IT_Dept.cshtml">Information Tech.</a></li>
<li><a href="../../Departments/MCA/About_MCA_Dept.cshtml">Computer Applications <!--[MCA]--> </a></li>
<li>
<a href="#">Humanities &amp; Basic Sci.</a>
<ul style="top: 31px; visibility: visible; left: 0px; width: 250px; display: none;">
<li><a class="dropdown" href="../../Departments/Chemistry/About_Chemistry_Dept.cshtml">Chemistry</a></li>
<li><a class="dropdown" href="../../Departments/HSS/About_HSS_Dept.cshtml">HSS</a></li>
<li><a class="dropdown" href="../../Departments/Physics/About_Physics_Dept.cshtml">Physics</a></li>
<li><a class="dropdown" href="../../Departments/Maths/About_Maths_Dept.cshtml">Mathematics</a></li>
</ul>
</li>
</ul>
</li>
<li><a href="../../TEQIP.cshtml">TEQIP</a></li>
<li>
<a href="#">Placements</a>
<ul>
<li><a href="../../Placements/Placements_Dept.cshtml">Placements Dept.</a></li>
<li><a href="../../Placements/Placements_Info?ay=2020-2021">Placements Information</a></li>
<li><a href="/Placements/Placements_Info_Student_Wise.cshtml?ay=2019-2020">Studentwise Placements Information </a></li>
<li><a href="/Placements/Placements_offcampus.cshtml">Placements Info. Offcampus</a></li>
<li><a href="/Placements/Recruiters.cshtml">Recruiters</a></li>
<li><a href="/Placements/Placements_Training.cshtml">Training</a></li>
<li><a href="/Placements/Internships.cshtml?Branch=Civil">Internships</a></li>
<li><a href="/Placements/stud_Competitive_Exams.cshtml?ay=2018-2019">Student - Competitive Exams</a></li>
<li><a href="/Placements/Industry_Linkages.cshtml">Industry Linkages</a></li>
</ul>
</li>
<li>
<a href="/RnD/About_RnD.cshtml">Research</a>
</li>
<li>
<a href="#">Staff</a>
<ul>
<li><a href="../../Staff_List.cshtml?Department=Civil">Civil Engineering</a></li>
<li><a href="../../Staff_List.cshtml?Department=CSE">Computer Science &amp; Engg.</a></li>
<li><a href="../../Staff_List.cshtml?Department=ECE">Electronics &amp; Communication </a></li>
<li><a href="../../Staff_List.cshtml?Department=EEE">Electrical &amp; Electronics Engg.</a></li>
<li><a href="../../Staff_List.cshtml?Department=Mech.">Mechanical Engineering</a></li>
<li><a href="../../Staff_List.cshtml?Department=IT">Information Technology</a></li>
<li>
<a href="#">Humanities &amp; Basic Sci.</a>
<ul>
<li><a class="dropdown" href="../../Staff_List.cshtml?Department=Chemistry">Chemistry</a></li>
<li><a class="dropdown" href="../../Staff_List.cshtml?Department=HSS">HSS</a></li>
<li><a class="dropdown" href="../../Staff_List.cshtml?Department=Physics">Physics</a></li>
<li><a class="dropdown" href="../../Staff_List.cshtml?Department=Maths">Mathematics</a></li>
</ul>
</li>
<li>
<a href="#">Functional Units &amp; Others</a>
<ul>
<li><a class="dropdown" href="../../Staff_List.cshtml?Department=Accounts">Accounts</a></li>
<li><a class="dropdown" href="../../Staff_List.cshtml?Department=aeb">Academic &amp; Exam Branch</a></li>
<li><a class="dropdown" href="../../Staff_List.cshtml?Department=Admn.">Administration</a></li>
<li><a class="dropdown" href="../../Staff_List.cshtml?Department=Campus">Campus Maintainance</a></li>
<li><a class="dropdown" href="../../Staff_List.cshtml?Department=CC">Computer Center</a></li>
<li><a class="dropdown" href="../../Staff_List.cshtml?Department=COE">Examinations Cell</a></li>
<li><a class="dropdown" href="../../Staff_List.cshtml?Department=dsw">DSW Office</a></li>
<li><a class="dropdown" href="../../Staff_List.cshtml?Department=Sports">Games &amp; Sports</a></li>
<li><a class="dropdown" href="../../Staff_List.cshtml?Department=Library">Library</a></li>
<li><a class="dropdown" href="../../Staff_List.cshtml?Department=HRD">Placement Cell [HR]</a></li>
<li><a class="dropdown" href="../../Staff_List.cshtml?Department=Medical">Medical Center</a></li>
<li><a class="dropdown" href="../../Staff_List.cshtml?Department=TEQIP">TEQIP</a></li>
</ul>
</li><li>
<a href="/Staff/Staff_Achievements.cshtml?ay=2018-2019">Staff Achivements</a>
</li>
</ul>
</li><li>
<a href="/Feedback/About_Feedback.cshtml">Feedback</a>
</li>
<li><a href="../../contact.cshtml">Contact</a></li>
<li><a href="../../search.cshtml"><i class="fas fa-search"></i></a> </li>
</ul><!-- topnav -->
</nav><!-- nav -->
</div>
</div>
</section>
<div class="clear"></div>
</header>
</div>
<!-- END HEADER -->
<!-- MAIN CONTENT -->
<div id="outermain">
<div class="container">
<div class="row">
<section class="twelve columns" id="maincontent">
<style>
td {text-align:left;}
.date {
width: 85px;
}
</style>
<!-- MAIN CONTENT -->
<div id="outermain">
<div class="container">
<div class="row">
<section class="twelve columns" id="maincontent">
<section class="content">
<div class="breadcrumb"><a href="http://vce.ac.in/">Home</a>  /  News &amp; Events</div>
<h1 class="pagetitle">News &amp; Events</h1>
<div class="table" id="tblGrid">
<script type="text/javascript">
(function($) {
$.fn.swhgLoad = function(url, containerId, callback) {
url = url + (url.indexOf('?') == -1 ? '?' : '&') + '__swhg=' + new Date().getTime();

$('<div/>').load(url + ' ' + containerId, function(data, status, xhr) {
    $(containerId).replaceWith($(this).html());
    if (typeof(callback) === 'function') {
        callback.apply(this, arguments);
    }
});
return this;
}

$(function() {
$('table[data-swhgajax="true"],span[data-swhgajax="true"]').each(function() {
    var self = $(this);
    var containerId = '#' + self.data('swhgcontainer');
    var callback = getFunction(self.data('swhgcallback'));

    $(containerId).parent().delegate(containerId + ' a[data-swhglnk="true"]', 'click', function() {
        $(containerId).swhgLoad($(this).attr('href'), containerId, callback);
        return false;
    });
})
});

function getFunction(code, argNames) {
argNames = argNames || [];
var fn = window, parts = (code || "").split(".");
while (fn && parts.length) {
    fn = fn[parts.shift()];
}
if (typeof (fn) === "function") {
    return fn;
}
argNames.push(code);
return Function.constructor.apply(null, argNames);
}
})(jQuery);
</script>
<table class="grid" data-swhgajax="true" data-swhgcallback="" data-swhgcontainer="tblGrid">
<thead>
<tr class="head">
<th scope="col">
<a data-swhglnk="true" href="/News_Events?sort=Date&amp;sortdir=ASC">Date Published</a> </th>
<th scope="col">
<a data-swhglnk="true" href="/News_Events?sort=Description&amp;sortdir=ASC">Description</a> </th>
</tr>
</thead>
<tfoot>
<tr>
<td colspan="2">1 <a data-swhglnk="true" href="/News_Events?page=2">2</a> <a data-swhglnk="true" href="/News_Events?page=3">3</a> <a data-swhglnk="true" href="/News_Events?page=4">4</a> <a data-swhglnk="true" href="/News_Events?page=5">5</a> <a data-swhglnk="true" href="/News_Events?page=2">&gt;</a> </td>
</tr>
</tfoot>
<tbody>
<tr>
<td class="date">13-Aug-2021</td>
<td> <img alt="new" src="/new.gif"/> <a href="https://vce.ac.in/Downloads/Administration/2021/Routine_Orders_Independence_Day_13-08-2021.pdf"><em>[ROUTINE ORDERS]</em> On the occasion of Independence Day, the National Flag will be hoisted on 15th August, 2021 at 10.00 a.m. in the College premises by Dr.S.V.Ramana, Principal, VCE.</a></td>
</tr>
<tr class="alt">
<td class="date">12-Aug-2021</td>
<td> <img alt="new" src="/new.gif"/> <a href="https://erp.vce.ac.in/BEOnlineEaf/Automation/ExamBranch/ExamBranchProcess/StudentWiseEAFProcessLatest/StudentLoginFormForEAFLatest.aspx"><em>[Online EAF]</em> BE - VIII-Semester and M.E./M.Tech (CBCS) I-Semester Makeup Examinations OnlineEAF</a></td>
</tr>
<tr>
<td class="date">12-Aug-2021</td>
<td> <img alt="new" src="/new.gif"/> <a href="https://erp.vce.ac.in/BEOnlineRevaluation/Automation/ExamBranch/ExamBranchProcess/StudentWiseRevaluationProcess/StudentLoginFormForRevaluation.aspx"><em>[Online Revaluation and Photocopy]</em> Online Registration Form For Revaluation and Photocopy of the Answer scripts : BE I Semester Regular and Supplementary held in July-2021</a></td>
</tr>
<tr class="alt">
<td class="date">10-Aug-2021</td>
<td> <img alt="new" src="/new.gif"/> <a href="https://vce.ac.in/Downloads_AEB/2021/CIRCULAR-133-REVISED-LIBRARY-BOOKS_10-08-2021.pdf"><em>[Circular]</em> Arrangement made for return as well as collection of text books by the students from the library in respect of Book-lending Scheme and SC/ST Book-bank</a></td>
</tr>
<tr>
<td class="date">10-Aug-2021</td>
<td> <img alt="new" src="/new.gif"/> <a href="https://sis.vce.ac.in/BE_I_Sem_Results_10082021/"><em>[Online Results]</em> B.E. (CBCS) I Semester Main and backlog Examinations held in July 2021</a></td>
</tr>
<tr class="alt">
<td class="date">10-Aug-2021</td>
<td> <img alt="new" src="/new.gif"/> <a href="https://vce.ac.in/Downloads_COE/2021/08_21_BE_I_Sem_RV_Notice_10-08-2021.pdf"><em>[Notice]</em> B.E. (CBCS) I Semester Main and backlog Examinations held in July 2021 - Revaluation </a></td>
</tr>
<tr>
<td class="date">10-Aug-2021</td>
<td> <img alt="new" src="/new.gif"/> <a href="https://vce.ac.in/Downloads_COE/2021/08_21_BE_I_Sem_Result_Sheet_10-08-2021.pdf"><em>[Result Sheet]</em> B.E. (CBCS) I Semester Main and backlog Examinations held in July 2021</a></td>
</tr>
<tr class="alt">
<td class="date">09-Aug-2021</td>
<td> <img alt="new" src="/new.gif"/> <a href="https://vce.ac.in/Downloads_AEB/2021/132-ME-IISEM-II-INTERNAL-TEST-TIME-TABLE_09-08-2021.pdf"><em>[Time Table]</em> Online Mode - II-Internal Test Time-Table for M.E./M.Tech. II-Semester course for the year 2020-2021</a></td>
</tr>
<tr>
<td class="date">09-Aug-2021</td>
<td> <img alt="new" src="/new.gif"/> <a href="https://vce.ac.in/Downloads_COE/2021/01_ME_MTech_I_Sem_Makeup_Notification_09-08-2021.pdf"><em>[Notification]</em> M.E./M.Tech (CBCS) I-Semester Makeup Examinations will be conducted in September 2021</a></td>
</tr>
<tr class="alt">
<td class="date">09-Aug-2021</td>
<td> <img alt="new" src="/new.gif"/> <a href="https://vce.ac.in/Downloads_COE/2021/02_ME_MTech_I_Sem_Makeup_Titmetable_09-08-2021.pdf"><em>[Time Table]</em> M.E./M.Tech (CBCS) I-Semester Makeup Examinations will be conducted in September 2021</a></td>
</tr>
<tr>
<td class="date">09-Aug-2021</td>
<td> <img alt="new" src="/new.gif"/> <a href="https://vce.ac.in/Downloads_COE/2021/01_BE_VIII_Sem_Makeup_notification_09-08-2021.pdf"><em>[Notification]</em> B.E. VIII Semester Examinations will be conducted in September 2021</a></td>
</tr>
<tr class="alt">
<td class="date">09-Aug-2021</td>
<td> <img alt="new" src="/new.gif"/> <a href="https://vce.ac.in/Downloads_COE/2021/02_BE_VIII_Sem_Makeup_Timetable_09-08-2021.pdf"><em>[Time Table]</em> B.E. VIII Semester Examinations will be conducted in September 2021</a></td>
</tr>
<tr>
<td class="date">09-Aug-2021</td>
<td> <img alt="new" src="/new.gif"/> <a href="https://vce.ac.in/Downloads_AEB/2021/Tranport_Facility_circular_09-08-2021.pdf"><em>[Circular]</em> Transport facility on “Payment basis” arranged through college buses for the interested students of B.E. II Semester who will be attending the Semester End Examinations.</a></td>
</tr>
<tr class="alt">
<td class="date">06-Aug-2021</td>
<td> <img alt="new" src="/new.gif"/> <a href="https://vce.ac.in/Downloads_COE/2021/BE_VIII_semester_revaluation_results_06-08-2021.pdf"><em>[Result Sheet]</em> Revaluation Result of B.E. (CBCS) VIII-Semester Main &amp; Backlog and IV Year II-Semester (Backlog) Examinations, July 2021 </a></td>
</tr>
<tr>
<td class="date">04-Aug-2021</td>
<td> <img alt="new" src="/new.gif"/> <a href="https://sis.vce.ac.in/ME_1sem_Results_04082021/"><em>[Online Results]</em> ME/M.Tech (CBCS) I Semester Main Examinations  held in July 2021</a></td>
</tr>
<tr class="alt">
<td class="date">04-Aug-2021</td>
<td> <img alt="new" src="/new.gif"/> <a href="https://vce.ac.in/Downloads_COE/Results_04-08-2021/RV_Notice_ME_I_Sem_Main.pdf"><em>[Notice]</em> REQUEST FOR REVALUATION AND PHOTOCOPY OF THE ANSWER SCRIPTS ONLINE : ME/M.Tech (CBCS) I Semester Main Examinations  held in July 2021</a></td>
</tr>
<tr>
<td class="date">04-Aug-2021</td>
<td> <img alt="new" src="/new.gif"/> <a href="https://vce.ac.in/Downloads_COE/Results_04-08-2021/RS_ME_I_Sem_Main_July_21.pdf"><em>[Result Sheet]</em> ME/M.Tech (CBCS) I Semester Main Examinations  held in July 2021</a></td>
</tr>
<tr class="alt">
<td class="date">04-Aug-2021</td>
<td> <img alt="new" src="/new.gif"/> <a href="https://sis.vce.ac.in/BE_367sem_Results_04082021/"><em>[Online Results]</em> BE III, V &amp; VII Semesters Supplementary Examinations held in July 2021</a></td>
</tr>
<tr>
<td class="date">04-Aug-2021</td>
<td> <img alt="new" src="/new.gif"/> <a href="https://vce.ac.in/Downloads_COE/Results_04-08-2021/RV_Notice_BE_III_V_VII_Supply.pdf"><em>[Notice]</em> REQUEST FOR REVALUATION AND PHOTOCOPY OF THE ANSWER SCRIPTS ONLINE : BE III, V &amp; VII Semesters Supplementary Examinations held in July 2021</a></td>
</tr>
<tr class="alt">
<td class="date">04-Aug-2021</td>
<td> <img alt="new" src="/new.gif"/> <a href="https://vce.ac.in/Downloads_COE/Results_04-08-2021/RS_BE_III_V_VII_Suppli_July_21.pdf"><em>[Result Sheet]</em> BE III, V &amp; VII Semesters Supplementary Examinations held in July 2021</a></td>
</tr>
<tr>
<td class="date">03-Aug-2021</td>
<td> <img alt="new" src="/new.gif"/> <a href="https://erp.vce.ac.in/BEOnlineEaf/Automation/ExamBranch/ExamBranchProcess/StudentWiseEAFProcessLatest/StudentLoginFormForEAFLatest.aspx"><em>[Online EAF]</em> ME/MTECH. (CBCS) II semester main Examinations Online EAF</a></td>
</tr>
<tr class="alt">
<td class="date">31-Jul-2021</td>
<td> <img alt="new" src="/new.gif"/> <a href="https://erp.vce.ac.in/BEOnlineEaf/Automation/ExamBranch/ExamBranchProcess/StudentWiseEAFProcessLatest/StudentLoginFormForEAFLatest.aspx"><em>[Online EAF]</em> B.E. (CBCS) II semester main Examinations Online EAF</a></td>
</tr>
<tr>
<td class="date">31-Jul-2021</td>
<td> <img alt="new" src="/new.gif"/> <a href="https://vce.ac.in/Downloads_AEB/2021/129-BE-IISEM-II-INTERNAL-TIMETABLE_31-07-2021.pdf"><em>[Time Table]</em> Online II - Internal Test Time-Table for B.E. II Semester for the year 2020-2021</a></td>
</tr>
<tr class="alt">
<td class="date">30-Jul-2021</td>
<td> <img alt="new" src="/new.gif"/> <a href="https://vce.ac.in/Downloads_COE/2021/No_172_ME-MTech_II-Sem_Notification_30-07-2021.pdf"><em>[Notification]</em> ME/M.Tech (CBCS) II-Semester Main Examinations Notification and Time Table</a></td>
</tr>
<tr>
<td class="date">30-Jul-2021</td>
<td> <img alt="new" src="/new.gif"/> <a href="https://vce.ac.in/Downloads_COE/2021/No_173_ME-Mtech_II-Sem_Exam-TT_30-07-2021.pdf"><em>[Time Table]</em> ME/M.Tech (CBCS) II-Semester Main Examinations Notification and Time Table</a></td>
</tr>
<tr class="alt">
<td class="date">30-Jul-2021</td>
<td> <img alt="new" src="/new.gif"/> <a href="https://vce.ac.in/Downloads_AEB/2021/128-BE-IISEM-3RD-QUIZ-TEST-TIMETABLE_30-07-2021.pdf"><em>[Time Table]</em> Third Quiz Test Online Time-Table for B.E. II Semester for the year 2020-2021</a></td>
</tr>
<tr>
<td class="date">28-Jul-2021</td>
<td> <img alt="new" src="/new.gif"/> <a href="https://vce.ac.in/Downloads_COE/2021/No_174_BE_II-Sem_Notification_28-07-2021.pdf"><em>[Notification]</em> BE (CBCS) II-Semester Main Examinations Notification and Time Table of BE (CBCS)II-Semester Main &amp; Backlog Examinations - Aug/Sep-2021</a></td>
</tr>
<tr class="alt">
<td class="date">28-Jul-2021</td>
<td> <img alt="new" src="/new.gif"/> <a href="https://vce.ac.in/Downloads_COE/2021/No_175_BE_II-Sem_Exam-TT_28-07-2021.pdf"><em>[Time Table]</em> BE (CBCS) II-Semester Main Examinations Notification and Time Table of BE (CBCS)II-Semester Main &amp; Backlog Examinations - Aug/Sep-2021</a></td>
</tr>
<tr>
<td class="date">26-Jul-2021</td>
<td> <img alt="new" src="/new.gif"/> <a href="https://erp.vce.ac.in/BEOnlineRevaluation/Automation/ExamBranch/ExamBranchProcess/StudentWiseRevaluationProcess/StudentLoginFormForRevaluation.aspx"><em>[Online Revaluation and Photocopy]</em> Online Registration Form For Revaluation and Photocopy of the Answer scripts online : BE VIII Semester(CBCS) Main Examinations held in July 2021</a></td>
</tr>
<tr class="alt">
<td class="date">23-Jul-2021</td>
<td> <img alt="new" src="/new.gif"/> <a href="https://vce.ac.in/Downloads_COE/Results_23-07-2021/RV_Notice_23-07-2021.pdf"><em>[Notice]</em> Request for Revaluation and Photocopy of the Answer scripts online : BE VIII Semester(CBCS) Main Examinations held in July 2021</a></td>
</tr>
<tr>
<td class="date">23-Jul-2021</td>
<td> <img alt="new" src="/new.gif"/> <a href="https://vce.ac.in/Downloads_COE/Results_23-07-2021/Result_Sheet_23-07-2021.pdf"><em>[Result Sheet]</em> BE VIII Semester(CBCS) Main Examinations held in July 2021</a></td>
</tr>
<tr class="alt">
<td class="date">23-Jul-2021</td>
<td> <img alt="new" src="/new.gif"/> <a href="https://sis.vce.ac.in/results_be_23072021/"><em>[Online Results]</em> BE VIII Semester(CBCS) Main Examinations held in July 2021</a></td>
</tr>
<tr>
<td class="date">19-Jul-2021</td>
<td> <img alt="new" src="/new.gif"/> <a href="https://vce.ac.in/Downloads_COE/BE_VI_Sem_Updates_19-07-2021.pdf"><em>[Time Table]</em> BE VI Semester Main and Backlog Examinations-Change of time in Skill Development -IV (SS &amp; TS)</a></td>
</tr>
<tr class="alt">
<td class="date">19-Jul-2021</td>
<td> <img alt="new" src="/new.gif"/> <a href="https://erp.vce.ac.in/BEOnlineEaf/Automation/ExamBranch/ExamBranchProcess/StudentHallTicketDownLoad/StudentLoginFormForDownloadHtno.aspx"><em>[Hall Tickets]</em> B.E. IV Sem. and VI Sem. Regular and Backlogs,  II-II sem., III-II sem., Backlogs Hall ticket download</a></td>
</tr>
<tr>
<td class="date">16-Jul-2021</td>
<td> <a href="https://vce.ac.in/Departments/Mech/Downloads/FDP_RATE_2021_Brochure_16-07-2021.pdf"><em>[FDP]</em> Online Faculty Development Programme on “Research Avenues in Thermal Engineering” [RATE - 2021]   26th July – 30th July 2021  Department of Mechanical Engineering, VCE.</a></td>
</tr>
</tbody>
</table>
</div>
</section>
</section>
</div>
</div>
</div>
<!-- END MAIN CONTENT -->
</section>
</div>
</div>
</div>
<!-- END MAIN CONTENT -->
<!-- FOOTER -->
<footer id="footer">
<!-- FOOTER SIDEBAR -->
<div class="clear"></div>
<div id="outerfootersidebar" style="background-color:#2471A3;">
<div class="outercontainer">
<div class="bottom" style="padding-bottom:20px;">
</div>
<div class="container">
<!-- container-->
<div class="row" id="footersidebar">
<div class="one_fourth columns" id="footcol1">
<h2 class="widget-title" style="color:#fff">Anti-Ragging Policy</h2>
<p style="color:#fff">
<img alt="say-no-to-ragging" class="frame alignleft" src="/img/say-no-to-ragging.gif" width="35%"/>
        Vasavi College of Engineering, in strict compliance with UGC Regulations on Curbing the Menace of Ragging in Higher Educational Institutions, 2009, AICTE Notification, 2009, Supreme Court directives, 2007 and Andhra Pradesh Prohibition of Ragging Act, 1997 as adopted by the
        State Govt. of Telangana, has decided to frame a Policy to Prohibit and Prevent Ragging Activities in its Campus.<br/>
        Ragging - A violation of Human Rights. ."
        <br/><br/> <a href="/Anti_Ragging_Policy" style="float:right;">+ Read More</a>
</p></div>
<div class="one_fourth columns" id="footcol2">
<ul>
<li class="widget-container">
<h2 class="widget-title" style="color:#fff">Downloads</h2>
<ul class="list">
<li><a href="/Downloads/Exam_Fee_Form_New_01-10-2020.pdf">Exam Fee Form (Accounts Dept.)</a></li>
<li><a href="/Downloads/36AAATV1119R1Z2.pdf">VCE GST No. 36AAATV1119R1Z2</a></li>
<li><a href="Downloads/Others/NO_DUES_CERTIFICATE.pdf">Student No Dues Certificate</a></li>
<li><a href="Downloads/Others/SWIFTT-CODE-FOR-WEBSITE.pdf">Online fee payment - Bank a/c. details</a></li>
<li><a href="/Downloads_COE/Forms/Application_Form_for_Revaluation.pdf"> Application Form: Revaluation of Answer Scripts</a></li>
<li><a href="/Downloads_COE/Forms/Application_Form_for_obtaining_Photocopy_of_Answer_Script.pdf">Application Form: Obtaining Photocopy of Answer Script</a></li>
<li>
<a href="/Downloads_COE/Forms/Application_Form_for_BE_Main_Suppli_Exams.pdf">
                        Application Form : Registration to B.E. (Main/Suppli./Adv. Suppli) Examinations
                    </a>
</li>
<li>
<a href="/Downloads_COE/Forms/Application_Form_for_MCA_Main_Suppli_Exams.pdf">
                        Application Form : Registration to M.C.A. (Main/Suppli./Adv. Suppli) Examinations
                    </a>
</li>
<li>
<a href="/Downloads_COE/Forms/Application_Form_for_ME_MTECH_Main_Makeup_Exams.pdf">
                        Application Form : Registration to M.E./M.Tech. (Main/Makeup) Examinations.
                    </a>
</li>
</ul>
</li>
</ul>
</div>
<div class="one_fourth columns" id="footcol3">
<ul>
<li class="widget-container">
<h2 class="widget-title" style="color:#fff">Useful Links</h2>
<ul class="list">
<li><a href="http://www.osmania.ac.in/" style="color:#fff;">Osmania university</a></li>
<li><a href="http://www.aicte-india.org/">AICTE</a></li>
<li><a href="http://www.nbaind.org/">NBA</a></li>
<li><a href="http://www.ugc.ac.in/">UGC</a></li>
<li><a href="https://tseamcet.nic.in/">TS EAMCET</a></li>
<li><a href="http://spoken-tutorial.org/">Spoken Tutorials (IIT Bombay)</a></li>
<li><a href="http://nptel.ac.in/">NPTEL (E-learning)</a></li>
<li><a href="http://www.pilot.edureform.iitm.ac.in/overview.php">QEEE</a></li>
<li><a href="https://www.youth4work.com/onlinetalenttest">youth4work [Online Skill Test]</a></li>
<li><a href="https://swayam.gov.in/">SWAYAM [Free online Education]</a></li>
<li><a href="https://in.udacity.com/">UDACITY</a></li>
<li><a href="https://infytq.infosys.com/">infytq - Infosys [Online Learning]</a></li>
<li><a href="https://www.ncs.gov.in/Pages/default.aspx">National Career Service [NCS]</a></li>
</ul>
</li>
</ul>
</div>
<div class="one_fourth columns" id="footcol5">
<ul>
<li class="widget-container">
<h2 class="widget-title" style="color:#fff">Contact Us</h2>
<div class="textwidget" style="color:#fff">
                Vasavi College of Engineering<br/>
<em style="color:white;"><small> (Private Un-aided Non-minority Autonomous Institution)<br/></small></em>
                Affiliated to Osmania University, Hyderabad <br/>
                Approved by AICTE, New Delhi<br/>
                9-5-81, Ibrahimbagh<br/>
                Hyderabad - 500 031<br/>
                Telangana, India<br/><br/>

                Tel: +91 40 23146003<br/>
                Fax: +91 40 23146090<br/> <br/>
<a href="mailto:principal@vce.ac.in">principal@staff.vce.ac.in</a><br/>
<a href="http://vce.ac.in">www.vce.ac.in</a>
</div>
</li>
</ul>
</div>
<div class="clear"></div>
</div>
</div>
</div>
</div>
<!-- END FOOTER SIDEBAR -->
<!-- COPYRIGHT -->
<div id="outercopyright" style="background-color:#1F618D;">
<div class="container" style="background-color:#1F618D;">
<div id="copyright" style="color:white; font-size:14px;">
Copyright ©2021. Vasavi College of Engineering, Ibrahimbagh, Hyderabad, India. All Rights Reserved.
</div>
</div>
</div>
<!-- END COPYRIGHT -->
<script type="text/javascript">
/*
var _gaq = _gaq || [];
_gaq.push(['_setAccount', 'UA-34758308-1']);
_gaq.push(['_trackPageview']);
(function () {
var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
})();
*/
</script>
</footer>
<!-- Material button -->
<button class="material-scrolltop" type="button"></button>
<!-- Include js plugin -->
<script src="https://vce.ac.in/src/material-scrolltop.js"></script>
<!-- Initialize -->
<script>
$(document).ready(function() {
$('body').materialScrollTop({
revealElement: 'header',
revealPosition: 'bottom',
onScrollEnd: function() {
    console.log('Scrolling End');
}
});
});
</script>
<!-- END FOOTER -->
<div class="clear"></div>
<!-- end outercontainer -->
</div><!-- end bodychild -->
<!-- ////////////////////////////////// -->
<!-- //      Javascript Files        // -->
<!-- ////////////////////////////////// -->
<!-- jQuery Superfish -->
<script src="https://vce.ac.in/js/hoverIntent.js" type="text/javascript"></script>
<script src="https://vce.ac.in/js/superfish.js" type="text/javascript"></script>
<script src="https://vce.ac.in/js/supersubs.js" type="text/javascript"></script>
<!-- jQuery Carosel Slider -->
<script src="https://vce.ac.in/js/jquery.elastislide.js" type="text/javascript"></script>
<script type="text/javascript">
jQuery('#carousel').elastislide({
imageW: 135,
margin: 12
});
</script>
<!-- jQuery Dropdown Mobile -->
<script src="https://vce.ac.in/js/tinynav.min.js" type="text/javascript"></script>
<!-- Custom Script -->
<script src="https://vce.ac.in/js/custom.js" type="text/javascript"></script>
<!-- jQuery Layerslider -->
<script src="https://vce.ac.in/js/jquery-easing-1.3.js" type="text/javascript"></script>
<script src="https://vce.ac.in/js/layerslider.js" type="text/javascript"></script>
<script type="text/javascript">
jQuery(window).load(function () {
jQuery('#layerslider.slideritems').layerSlider({
skinsPath: '~/images/layerslider-skins/',
skin: 'lastore',
autoStart: true
});
jQuery('.ls-nav-prev').fadeOut();
jQuery('.ls-nav-next').fadeOut();
jQuery('#layerslider.slideritems').mouseleave(function () {
jQuery('.ls-nav-prev').fadeOut();
jQuery('.ls-nav-next').fadeOut();
});
jQuery('#layerslider.slideritems').mouseenter(function () {
jQuery('.ls-nav-prev').fadeIn();
jQuery('.ls-nav-next').fadeIn();
});
});
</script>
</body>
</html>""",
    "html.parser",
)


expected_news_result = [
    {
        "date": "2021-08-13",
        "link": "https://vce.ac.in/Downloads/Administration/2021/Routine_Orders_Independence_Day_13-08-2021.pdf",
        "content": "On the occasion of Independence Day, the National Flag will be hoisted on 15th August, 2021 at 10.00 a.m. in the College premises by Dr.S.V.Ramana, Principal, VCE.",
        "index": "ROUTINE ORDERS",
        "categories": "['Information']",
    },
    {
        "date": "2021-08-12",
        "link": "https://erp.vce.ac.in/BEOnlineEaf/Automation/ExamBranch/ExamBranchProcess/StudentWiseEAFProcessLatest/StudentLoginFormForEAFLatest.aspx",
        "content": "BE - VIII-Semester and M.E./M.Tech (CBCS) I-Semester Makeup Examinations OnlineEAF",
        "index": "Online EAF",
        "categories": "['Supplementary', 'Examination']",
    },
    {
        "date": "2021-08-12",
        "link": "https://erp.vce.ac.in/BEOnlineRevaluation/Automation/ExamBranch/ExamBranchProcess/StudentWiseRevaluationProcess/StudentLoginFormForRevaluation.aspx",
        "content": "Online Registration Form For Revaluation and Photocopy of the Answer scripts : BE I Semester Regular and Supplementary held in July-2021",
        "index": "Online Revaluation and Photocopy",
        "categories": "['Supplementary', 'Revaluation']",
    },
    {
        "date": "2021-08-10",
        "link": "https://vce.ac.in/Downloads_AEB/2021/CIRCULAR-133-REVISED-LIBRARY-BOOKS_10-08-2021.pdf",
        "content": "Arrangement made for return as well as collection of text books by the students from the library in respect of Book-lending Scheme and SC/ST Book-bank",
        "index": "Circular",
        "categories": "['Information']",
    },
    {
        "date": "2021-08-10",
        "link": "https://sis.vce.ac.in/BE_I_Sem_Results_10082021/",
        "content": "B.E. (CBCS) I Semester Main and backlog Examinations held in July 2021",
        "index": "Online Results",
        "categories": "['Supplementary', 'Examination']",
    },
    {
        "date": "2021-08-10",
        "link": "https://vce.ac.in/Downloads_COE/2021/08_21_BE_I_Sem_RV_Notice_10-08-2021.pdf",
        "content": "B.E. (CBCS) I Semester Main and backlog Examinations held in July 2021 - Revaluation ",
        "index": "Notice",
        "categories": "['Supplementary', 'Examination', 'Revaluation']",
    },
    {
        "date": "2021-08-10",
        "link": "https://vce.ac.in/Downloads_COE/2021/08_21_BE_I_Sem_Result_Sheet_10-08-2021.pdf",
        "content": "B.E. (CBCS) I Semester Main and backlog Examinations held in July 2021",
        "index": "Result Sheet",
        "categories": "['Supplementary', 'Examination']",
    },
    {
        "date": "2021-08-09",
        "link": "https://vce.ac.in/Downloads_AEB/2021/132-ME-IISEM-II-INTERNAL-TEST-TIME-TABLE_09-08-2021.pdf",
        "content": "Online Mode - II-Internal Test Time-Table for M.E./M.Tech. II-Semester course for the year 2020-2021",
        "index": "Time Table",
        "categories": "['Examination', 'Timetable']",
    },
    {
        "date": "2021-08-09",
        "link": "https://vce.ac.in/Downloads_COE/2021/01_ME_MTech_I_Sem_Makeup_Notification_09-08-2021.pdf",
        "content": "M.E./M.Tech (CBCS) I-Semester Makeup Examinations will be conducted in September 2021",
        "index": "Notification",
        "categories": "['Supplementary', 'Examination']",
    },
    {
        "date": "2021-08-09",
        "link": "https://vce.ac.in/Downloads_COE/2021/02_ME_MTech_I_Sem_Makeup_Titmetable_09-08-2021.pdf",
        "content": "M.E./M.Tech (CBCS) I-Semester Makeup Examinations will be conducted in September 2021",
        "index": "Time Table",
        "categories": "['Supplementary', 'Examination']",
    },
    {
        "date": "2021-08-09",
        "link": "https://vce.ac.in/Downloads_COE/2021/01_BE_VIII_Sem_Makeup_notification_09-08-2021.pdf",
        "content": "B.E. VIII Semester Examinations will be conducted in September 2021",
        "index": "Notification",
        "categories": "['Examination']",
    },
    {
        "date": "2021-08-09",
        "link": "https://vce.ac.in/Downloads_COE/2021/02_BE_VIII_Sem_Makeup_Timetable_09-08-2021.pdf",
        "content": "B.E. VIII Semester Examinations will be conducted in September 2021",
        "index": "Time Table",
        "categories": "['Examination']",
    },
    {
        "date": "2021-08-09",
        "link": "https://vce.ac.in/Downloads_AEB/2021/Tranport_Facility_circular_09-08-2021.pdf",
        "content": "Transport facility on 'Payment basis' arranged through college buses for the interested students of B.E. II Semester who will be attending the Semester End Examinations.",
        "index": "Circular",
        "categories": "['Examination']",
    },
    {
        "date": "2021-08-06",
        "link": "https://vce.ac.in/Downloads_COE/2021/BE_VIII_semester_revaluation_results_06-08-2021.pdf",
        "content": "Revaluation Result of B.E. (CBCS) VIII-Semester Main & Backlog and IV Year II-Semester (Backlog) Examinations, July 2021 ",
        "index": "Result Sheet",
        "categories": "['Supplementary', 'Examination', 'Revaluation', 'Result']",
    },
    {
        "date": "2021-08-04",
        "link": "https://sis.vce.ac.in/ME_1sem_Results_04082021/",
        "content": "ME/M.Tech (CBCS) I Semester Main Examinations  held in July 2021",
        "index": "Online Results",
        "categories": "['Examination']",
    },
    {
        "date": "2021-08-04",
        "link": "https://vce.ac.in/Downloads_COE/Results_04-08-2021/RV_Notice_ME_I_Sem_Main.pdf",
        "content": "REQUEST FOR REVALUATION AND PHOTOCOPY OF THE ANSWER SCRIPTS ONLINE : ME/M.Tech (CBCS) I Semester Main Examinations  held in July 2021",
        "index": "Notice",
        "categories": "['Examination', 'Revaluation']",
    },
    {
        "date": "2021-08-04",
        "link": "https://vce.ac.in/Downloads_COE/Results_04-08-2021/RS_ME_I_Sem_Main_July_21.pdf",
        "content": "ME/M.Tech (CBCS) I Semester Main Examinations  held in July 2021",
        "index": "Result Sheet",
        "categories": "['Examination']",
    },
    {
        "date": "2021-08-04",
        "link": "https://sis.vce.ac.in/BE_367sem_Results_04082021/",
        "content": "BE III, V & VII Semesters Supplementary Examinations held in July 2021",
        "index": "Online Results",
        "categories": "['Supplementary', 'Examination']",
    },
    {
        "date": "2021-08-04",
        "link": "https://vce.ac.in/Downloads_COE/Results_04-08-2021/RV_Notice_BE_III_V_VII_Supply.pdf",
        "content": "REQUEST FOR REVALUATION AND PHOTOCOPY OF THE ANSWER SCRIPTS ONLINE : BE III, V & VII Semesters Supplementary Examinations held in July 2021",
        "index": "Notice",
        "categories": "['Supplementary', 'Examination', 'Revaluation']",
    },
    {
        "date": "2021-08-04",
        "link": "https://vce.ac.in/Downloads_COE/Results_04-08-2021/RS_BE_III_V_VII_Suppli_July_21.pdf",
        "content": "BE III, V & VII Semesters Supplementary Examinations held in July 2021",
        "index": "Result Sheet",
        "categories": "['Supplementary', 'Examination']",
    },
    {
        "date": "2021-08-03",
        "link": "https://erp.vce.ac.in/BEOnlineEaf/Automation/ExamBranch/ExamBranchProcess/StudentWiseEAFProcessLatest/StudentLoginFormForEAFLatest.aspx",
        "content": "ME/MTECH. (CBCS) II semester main Examinations Online EAF",
        "index": "Online EAF",
        "categories": "['Examination']",
    },
    {
        "date": "2021-07-31",
        "link": "https://erp.vce.ac.in/BEOnlineEaf/Automation/ExamBranch/ExamBranchProcess/StudentWiseEAFProcessLatest/StudentLoginFormForEAFLatest.aspx",
        "content": "B.E. (CBCS) II semester main Examinations Online EAF",
        "index": "Online EAF",
        "categories": "['Examination']",
    },
    {
        "date": "2021-07-31",
        "link": "https://vce.ac.in/Downloads_AEB/2021/129-BE-IISEM-II-INTERNAL-TIMETABLE_31-07-2021.pdf",
        "content": "Online II - Internal Test Time-Table for B.E. II Semester for the year 2020-2021",
        "index": "Time Table",
        "categories": "['Examination', 'Timetable']",
    },
    {
        "date": "2021-07-30",
        "link": "https://vce.ac.in/Downloads_COE/2021/No_172_ME-MTech_II-Sem_Notification_30-07-2021.pdf",
        "content": "ME/M.Tech (CBCS) II-Semester Main Examinations Notification and Time Table",
        "index": "Notification",
        "categories": "['Examination', 'Timetable']",
    },
    {
        "date": "2021-07-30",
        "link": "https://vce.ac.in/Downloads_COE/2021/No_173_ME-Mtech_II-Sem_Exam-TT_30-07-2021.pdf",
        "content": "ME/M.Tech (CBCS) II-Semester Main Examinations Notification and Time Table",
        "index": "Time Table",
        "categories": "['Examination', 'Timetable']",
    },
    {
        "date": "2021-07-30",
        "link": "https://vce.ac.in/Downloads_AEB/2021/128-BE-IISEM-3RD-QUIZ-TEST-TIMETABLE_30-07-2021.pdf",
        "content": "Third Quiz Test Online Time-Table for B.E. II Semester for the year 2020-2021",
        "index": "Time Table",
        "categories": "['Examination', 'Timetable']",
    },
    {
        "date": "2021-07-28",
        "link": "https://vce.ac.in/Downloads_COE/2021/No_174_BE_II-Sem_Notification_28-07-2021.pdf",
        "content": "BE (CBCS) II-Semester Main Examinations Notification and Time Table of BE (CBCS)II-Semester Main & Backlog Examinations - Aug/Sep-2021",
        "index": "Notification",
        "categories": "['Supplementary', 'Examination', 'Timetable']",
    },
    {
        "date": "2021-07-28",
        "link": "https://vce.ac.in/Downloads_COE/2021/No_175_BE_II-Sem_Exam-TT_28-07-2021.pdf",
        "content": "BE (CBCS) II-Semester Main Examinations Notification and Time Table of BE (CBCS)II-Semester Main & Backlog Examinations - Aug/Sep-2021",
        "index": "Time Table",
        "categories": "['Supplementary', 'Examination', 'Timetable']",
    },
    {
        "date": "2021-07-26",
        "link": "https://erp.vce.ac.in/BEOnlineRevaluation/Automation/ExamBranch/ExamBranchProcess/StudentWiseRevaluationProcess/StudentLoginFormForRevaluation.aspx",
        "content": "Online Registration Form For Revaluation and Photocopy of the Answer scripts online : BE VIII Semester(CBCS) Main Examinations held in July 2021",
        "index": "Online Revaluation and Photocopy",
        "categories": "['Examination', 'Revaluation']",
    },
    {
        "date": "2021-07-23",
        "link": "https://vce.ac.in/Downloads_COE/Results_23-07-2021/RV_Notice_23-07-2021.pdf",
        "content": "Request for Revaluation and Photocopy of the Answer scripts online : BE VIII Semester(CBCS) Main Examinations held in July 2021",
        "index": "Notice",
        "categories": "['Examination', 'Revaluation']",
    },
    {
        "date": "2021-07-23",
        "link": "https://vce.ac.in/Downloads_COE/Results_23-07-2021/Result_Sheet_23-07-2021.pdf",
        "content": "BE VIII Semester(CBCS) Main Examinations held in July 2021",
        "index": "Result Sheet",
        "categories": "['Examination']",
    },
    {
        "date": "2021-07-23",
        "link": "https://sis.vce.ac.in/results_be_23072021/",
        "content": "BE VIII Semester(CBCS) Main Examinations held in July 2021",
        "index": "Online Results",
        "categories": "['Examination']",
    },
    {
        "date": "2021-07-19",
        "link": "https://vce.ac.in/Downloads_COE/BE_VI_Sem_Updates_19-07-2021.pdf",
        "content": "BE VI Semester Main and Backlog Examinations-Change of time in Skill Development -IV (SS & TS)",
        "index": "Time Table",
        "categories": "['Supplementary', 'Examination']",
    },
    {
        "date": "2021-07-19",
        "link": "https://erp.vce.ac.in/BEOnlineEaf/Automation/ExamBranch/ExamBranchProcess/StudentHallTicketDownLoad/StudentLoginFormForDownloadHtno.aspx",
        "content": "B.E. IV Sem. and VI Sem. Regular and Backlogs,  II-II sem., III-II sem., Backlogs Hall ticket download",
        "index": "Hall Tickets",
        "categories": "['Supplementary']",
    },
    {
        "date": "2021-07-16",
        "link": "https://vce.ac.in/Departments/Mech/Downloads/FDP_RATE_2021_Brochure_16-07-2021.pdf",
        "content": "Online Faculty Development Programme on 'Research Avenues in Thermal Engineering' [RATE - 2021]   26th July - 30th July 2021  Department of Mechanical Engineering, VCE.",
        "index": "FDP",
        "categories": "['Information']",
    },
]

before_checker = {
    "date": "2021-07-26",
    "link": "https://erp.vce.ac.in/BEOnlineRevaluation/Automation/ExamBranch/ExamBranchProcess/StudentWiseRevaluationProcess/StudentLoginFormForRevaluation.aspx",
    "content": "Online Registration Form For Revaluation and Photocopy of the Answer scripts online : BE VIII Semester(CBCS) Main Examinations held in July 2021",
    "index": "Online Revaluation and Photocopy",
}
after_checker = {
    "date": "2021-07-26",
    "link": "https://erp.vce.ac.in/BEOnlineRevaluation/Automation/ExamBranch/ExamBranchProcess/StudentWiseRevaluationProcess/StudentLoginFormForRevaluation.aspx",
    "content": "Online Registration Form For Revaluation and Photocopy of the Answer scripts online : BE VIII Semester(CBCS) Main Examinations held in July 2021",
    "index": "Online Revaluation and Photocopy",
    "categories": "['Examination', 'Revaluation']",
}
