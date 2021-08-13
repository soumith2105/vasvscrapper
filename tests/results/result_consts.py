from bs4 import BeautifulSoup

result_soup = BeautifulSoup(
    """
<!-- <link href= "../../student.css" rel="stylesheet" type="text/css"> -->
<link href="../../css.css" rel="stylesheet" title="Style" type="text/css"/>
<!DOCTYPE html PUBLIC "-//W3C//Dtd XHTML 1.0 transitional//EN" "http://www.w3.org/tr/xhtml1/Dtd/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<script language="javascript">
//function allowNoOnly() {
//    if (!((event.keyCode >= 48 && event.keyCode <= 57) || event.keyCode == 46 || event.keyCode == 65)) {
//        event.keyCode = 0;
//    }
//}

//function validateMarks(i) {
//    var flag = false;
//    var varmarks = document.getElementById("marks" + i).value;
//    varmarks = parseInt(varmarks);

//    if (varmarks < 0 || varmarks > 100) {
//        document.getElementById("marks" + i).focus();
//        alert("Marks shoud be between 0 and 100");
//        document.getElementById("marks" + i).value = "";

//    }
//}
</script>
<title>
</title></head>
<body>
<form action="StudentSemWiseMarks.aspx" id="StudentProfilewithalldetails" method="post">
<input id="__VIEWSTATE" name="__VIEWSTATE" type="hidden" value="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"/>
<input id="__VIEWSTATEGENERATOR" name="__VIEWSTATEGENERATOR" type="hidden" value="F7A6478B"/>
<input id="__EVENTVALIDATION" name="__EVENTVALIDATION" type="hidden" value="jIyPGACLxmIImsb1AHYzNd9EgsZthvCJGxqdGiLEook6Ep42vJ5iUvUacOTn0tPPK19Qf3MqgvN+FLgxWQ6fE8cF704y/oPrWdkzCWin5lwUHdCZSKD8uf5bRCSEc4Di2W0AJjduZyugJIoIxBQ5OVZJo6S2sblsM2hfLRMx9MkoNVdAKOD2dWQYRTjlzdeXcTVzPj4xqUt4GB+iauL8sA=="/>
<div id="pnlContents">
<table align="center" border="0" cellpadding="1" cellspacing="1" style="width: 100%; height: 17px">
<tr><td>
<table align="center" border="0" cellpadding="1" cellspacing="1" style="width: 100%; height: 27px">
<tr><td align="center">
<p><font color="dodgerblue" size="4"><b>Vasavi College of Engineering</b></font> </p>
</td></tr> </table><br/>
<table align="center" border="0" cellpadding="1" cellspacing="1" id="tblerrormsg" style="width: 100%; height: 27px">
<tr>
<td align="center">
<span id="lblmsg"><font color="ForestGreen">Please enter the Hall Ticket Number to view  Sem Marks </font></span>
<input id="hduserbranchcode" name="hduserbranchcode" type="hidden"/>
<input id="hdpresentstudingyear" name="hdpresentstudingyear" type="hidden" value="7"/>
<input id="hdfileaccesstype" name="hdfileaccesstype" type="hidden"/>
<input id="hduserloginbranchcode" name="hduserloginbranchcode" type="hidden"/>
<input id="hdhtno" name="hdhtno" type="hidden"/>
</td>
</tr>
</table>
<br/>
<table align="center" border="1" bordercolor="dodgerblue" cellpadding="1" cellspacing="1" id="tblwelcome" style="width: 100%; height: 27px">
<tr>
<td>
<table align="center" bgcolor="dodgerblue" border="0" cellpadding="1" cellspacing="1" style="width: 100%; height: 27px">
<tr><td align="left">
<b><font color="white">Welcome <span id="lblusername"></span></font></b> </td></tr>
</table>
</td>
</tr>
</table>
<table align="center" border="1" bordercolor="dodgerblue" cellpadding="1" cellspacing="1" id="TblStudentHeading" style="width: 100%; height: 27px">
<tr>
<td id="TdStudentHeading"><table align="center" bgcolor="dodgerblue" border="0" cellpadding="1" cellspacing="1" width="100%"><tr align="center"><td align="ceneter"><b><font color="white"> Marks Report Of PODDUTURI. SOUMITH REDDY (1602-17-737-046) (IT - A)  4 YEAR - 8 SEMESTER </font></b></td></tr></table></td>
</tr>
</table>
<table align="center" border="0" bordercolor="dodgerblue" cellpadding="1" cellspacing="1" id="TblDispStudentProfile" style="width: 100%; height: 27px">
<tr>
<td id="TdDispStudentProfile"><table align="center" border="1" bordercolor="dodgerblue" cellpadding="1" cellspacing="1" width="100%"><tr><td> <table align="center" border="1" cellpadding="1" cellspacing="1" class="tableclass" width="100%"><tr bgcolor="dodgerblue" height="22px"><td align="left" colspan="10"><font color="white"> <b> Student Information </b></font></td></tr><tr><td align="left"><font color="">  Hall Ticket</font></td><td align="center"><font color="">:</font></td><td align="left"><font color=""> 1602-17-737-046</font></td><td align="left"><font color="">  Student Name</font></td><td align="center"><font color="">:</font></td><td align="left"><font color=""> PODDUTURI. SOUMITH REDDY</font></td><td align="center" colspan="3" rowspan="5"><img height="125" src="https://sis.vce.ac.in/vcetemp/Automation/StudentPhotos/2675.jpg" width="100"/></td></tr><tr><td align="left"><font color="">  Current Branch Info </font></td><td align="center"><font color="">:</font></td><td align="left"><font color=""> BE &amp; IT(A) - 4 Year 8 Semester </font></td><td align="left"><font color="">  Gender</font></td><td align="center"><font color="">:</font></td><td align="left"><font color=""> Male</font></td></tr><tr><td align="left"><font color="">  Date of Birth</font></td><td align="center"><font color="">:</font></td><td align="left"><font color=""> 21-May-1999</font></td><td align="left"><font color="">  Date of Joining</font></td><td align="center"><font color="">:</font></td><td align="left"><font color=""> 05-Aug-2017</font></td></tr><tr height="22px"><td align="left"><font color="">  Blood Group</font></td><td align="center"><font color="">:</font></td><td align="left"><font color=""> -</font></td><td align="left"><font color="">  CET Qualified</font></td><td align="center"><font color="">:</font></td><td align="left"><font color=""> EAMCET-2017</font></td></tr><tr height="22px"><td align="left"><font color="">  Rank</font></td><td align="center"><font color="">:</font></td><td align="left"><font color=""> 10610</font></td><td align="left"><font color="">  Religion</font></td><td align="center"><font color="">:</font></td><td align="left"><font color=""> Hindu</font></td></tr><tr height="22px"><td align="left"><font color="">  Current Status</font></td><td align="center"><font color="">:</font></td><td align="left"><font color=""> Studying</font></td><td align="left"><font color="">  Nationality</font></td><td align="center"><font color="">:</font></td><td align="left" colspan="2"><font color=""> Indian</font></td></tr><tr height="22px"><td align="left"><font color="">  Admn. Category</font></td><td align="center"><font color="">:</font></td><td align="left"><font color=""> Convener</font></td><td align="left"><font color="">  Category</font></td><td align="center"><font color="">:</font></td><td align="left" colspan="2"><font color=""> OC</font></td></tr><tr height="22px"><td align="left"><font color="">  Area</font></td><td align="center"><font color="">:</font></td><td align="left"><font color=""> Urban</font></td><td align="left"><font color="">  Mentor Name &amp; ID</font></td><td align="center"><font color="">:</font></td><td align="left" colspan="2"><font color=""> MrNelaturi David Raju (1709)</font></td></tr><tr height="22px"><td align="left"><font color="">  Identification Mark1</font></td><td align="center"><font color="">:</font></td><td align="left"><font color=""> A MOLE ON THE LEFT FIST</font></td><td align="left"><font color="">  Identification Mark2</font></td><td align="center"><font color="">:</font></td><td align="left" colspan="2"><font color=""> A MOLE ON THE CHEST</font></td></tr></table></td></tr></table><br/></td></tr></table></td></tr></table><br/><table align="center" border="1" bordercolor="dodgerblue" cellpadding="1" cellspacing="1" width="100%"><tr><td> <table align="center" border="1" cellpadding="1" cellspacing="1" class="tableclass" width="100%"><tr bgcolor="dodgerblue" height="22px"><td align="left" colspan="24"><font color="white"> <b> 4 Year and 8 Semester Marks Details</b></font></td></tr><tr bgcolor="dodgerblue" height="22px"><td align="center" rowspan="2"><font color="white"> <b> S.No </b></font></td><td align="center" rowspan="2"><font color="white"> <b> Subject Name</b></font></td><td align="center" colspan="2"><font color="white"><b> Int1 </b></font></td><td align="center" colspan="2"><font color="white"><b> Int2 </b></font></td><td align="center" colspan="2"><font color="white"><b> Asst1 </b></font></td><td align="center" colspan="2"><font color="white"><b> Asst2 </b></font></td><td align="center" colspan="2"><font color="white"><b> Asst3 </b></font></td><td align="center" colspan="2"><font color="white"><b> Quiz1 </b></font></td><td align="center" colspan="2"><font color="white"><b> Quiz2 </b></font></td><td align="center" colspan="2"><font color="white"><b> Quiz3 </b></font></td><td align="center" colspan="2"><font color="white"><b> Sessional <br/> Marks</b></font></td><td align="center" colspan="3"><font color="white"><b> External <br/> Grades </b></font></td></tr><tr bgcolor="dodgerblue" height="22px"><td align="center"><font color="white"><b> Max. Marks </b></font></td><td align="center"><font color="white"><b> Secured Marks</b></font></td><td align="center"><font color="white"><b> Max. Marks </b></font></td><td align="center"><font color="white"><b> Secured Marks</b></font></td><td align="center"><font color="white"><b> Max. Marks </b></font></td><td align="center"><font color="white"><b> Secured Marks</b></font></td><td align="center"><font color="white"><b> Max. Marks </b></font></td><td align="center"><font color="white"><b> Secured Marks</b></font></td><td align="center"><font color="white"><b> Max. Marks </b></font></td><td align="center"><font color="white"><b> Secured Marks</b></font></td><td align="center"><font color="white"><b> Max. Marks </b></font></td><td align="center"><font color="white"><b> Secured Marks</b></font></td><td align="center"><font color="white"><b> Max. Marks </b></font></td><td align="center"><font color="white"><b> Secured Marks</b></font></td><td align="center"><font color="white"><b> Max. Marks </b></font></td><td align="center"><font color="white"><b> Secured Marks</b></font></td><td align="center"><font color="white"><b> Max. Marks </b></font></td><td align="center"><font color="white"><b> Secured Marks</b></font></td><td align="center"><font color="white"><b> Grade </b></font></td><td align="center"><font color="white"><b> Sub. Credits </b></font></td><td align="center"><font color="white"><b> Grade Points </b></font></td></tr><tr height="22px"><td align="center"><font color="">1</font></td><td align="center"><font color="">SPM</font></td><td align="center"><font color="">30</font></td><td align="center"><font color="">26</font></td><td align="center"><font color="">30</font></td><td align="center"><font color="">29</font></td><td align="center"><font color="">5</font></td><td align="center"><font color="">2</font></td><td align="center"><font color="">5</font></td><td align="center"><font color="">5</font></td><td align="center"><font color="">5</font></td><td align="center"><font color="">5</font></td><td align="center"><font color="">5</font></td><td align="center"><font color="">4.66</font></td><td align="center"><font color="">5</font></td><td align="center"><font color="">3</font></td><td align="center"><font color="">5</font></td><td align="center"><font color="">4</font></td><td align="center"><font color="">40</font></td><td align="center"><font color="">36</font></td><td align="center" bgcolor=""><font color="">-</font></td><td align="center" bgcolor=""><font color="">0</font></td><td align="center" bgcolor=""><font color="">0</font></td></tr><tr height="22px"><td align="center"><font color="">2</font></td><td align="center"><font color="">NNDL</font></td><td align="center"><font color="">30</font></td><td align="center"><font color="">28</font></td><td align="center"><font color="">30</font></td><td align="center"><font color="">26</font></td><td align="center"><font color="">5</font></td><td align="center"><font color="">4</font></td><td align="center"><font color="">5</font></td><td align="center"><font color="">4.5</font></td><td align="center"><font color="">5</font></td><td align="center"><font color="">3.5</font></td><td align="center"><font color="">5</font></td><td align="center"><font color="">Ab</font></td><td align="center"><font color="">5</font></td><td align="center"><font color="">3.5</font></td><td align="center"><font color="">5</font></td><td align="center"><font color="">4.5</font></td><td align="center"><font color="">40</font></td><td align="center"><font color="">34</font></td><td align="center" bgcolor=""><font color="">-</font></td><td align="center" bgcolor=""><font color="">0</font></td><td align="center" bgcolor=""><font color="">0</font></td></tr><tr height="22px"><td align="center"><font color="">3</font></td><td align="center"><font color="">PROJ/INT</font></td><td align="center"><font color="">-</font></td><td align="center"><font color="">-</font></td><td align="center"><font color="">-</font></td><td align="center"><font color="">-</font></td><td align="center"><font color="">-</font></td><td align="center"><font color="">-</font></td><td align="center"><font color="">-</font></td><td align="center"><font color="">-</font></td><td align="center"><font color="">-</font></td><td align="center"><font color="">-</font></td><td align="center"><font color="">-</font></td><td align="center"><font color="">-</font></td><td align="center"><font color="">-</font></td><td align="center"><font color="">-</font></td><td align="center"><font color="">-</font></td><td align="center"><font color="">-</font></td><td align="center"><font color="">50</font></td><td align="center"><font color="">41</font></td><td align="center" bgcolor=""><font color="">-</font></td><td align="center" bgcolor=""><font color="">0</font></td><td align="center" bgcolor=""><font color="">0</font></td></tr><tr><td colspan="2"><font color="">Total</font></td><td align="center"><font color="">60</font></td><td align="center"><font color="">54</font></td><td align="center"><font color="">60</font></td><td align="center"><font color="">55</font></td><td align="center"><font color="">10</font></td><td align="center"><font color="">6</font></td><td align="center"><font color="">10</font></td><td align="center"><font color="">9.5</font></td><td align="center"><font color="">10</font></td><td align="center"><font color="">8.5</font></td><td align="center"><font color="">10</font></td><td align="center"><font color="">4.66</font></td><td align="center"><font color="">10</font></td><td align="center"><font color="">6.5</font></td><td align="center"><font color="">10</font></td><td align="center"><font color="">8.5</font></td><td align="center"><font color="">130</font></td><td align="center"><font color="">111</font></td><td align="center"><font color="">-</font></td><td align="center"><font color="">0</font></td><td align="center"><font color="">0</font></td></tr><tr><td colspan="2"><font color="">Percentage</font></td><td align="center" colspan="2"><font color="">90</font></td><td align="center" colspan="2"><font color="">91.66</font></td><td align="center" colspan="2"><font color="">60</font></td><td align="center" colspan="2"><font color="">95</font></td><td align="center" colspan="2"><font color="">85</font></td><td align="center" colspan="2"><font color="">46.6</font></td><td align="center" colspan="2"><font color="">65</font></td><td align="center" colspan="2"><font color="">85</font></td><td align="center" colspan="2"><font color="">85.38</font></td><td align="center" colspan="3"><font color="">SGPA : -</font></td></tr></table></td></tr></table><br/>
<br>

</br></div>
</form>
</body>
</html>""",
    "html.parser",
)

mark_rows = list(
    map(
        lambda x: BeautifulSoup(x, "html.parser"),
        [
            '<tr bgcolor="dodgerblue" height="22px"><td align="left" colspan="24"><font color="white"> <b> 4 Year and 8 Semester Marks Details</b></font></td></tr>',
            '<tr bgcolor="dodgerblue" height="22px"><td align="center" rowspan="2"><font color="white"> <b> S.No </b></font></td><td align="center" rowspan="2"><font color="white"> <b> Subject Name</b></font></td><td align="center" colspan="2"><font color="white"><b> Int1 </b></font></td><td align="center" colspan="2"><font color="white"><b> Int2 </b></font></td><td align="center" colspan="2"><font color="white"><b> Asst1 </b></font></td><td align="center" colspan="2"><font color="white"><b> Asst2 </b></font></td><td align="center" colspan="2"><font color="white"><b> Asst3 </b></font></td><td align="center" colspan="2"><font color="white"><b> Quiz1 </b></font></td><td align="center" colspan="2"><font color="white"><b> Quiz2 </b></font></td><td align="center" colspan="2"><font color="white"><b> Quiz3 </b></font></td><td align="center" colspan="2"><font color="white"><b> Sessional <br/> Marks</b></font></td><td align="center" colspan="3"><font color="white"><b> External <br/> Grades </b></font></td></tr>',
            '<tr bgcolor="dodgerblue" height="22px"><td align="center"><font color="white"><b> Max. Marks </b></font></td><td align="center"><font color="white"><b> Secured Marks</b></font></td><td align="center"><font color="white"><b> Max. Marks </b></font></td><td align="center"><font color="white"><b> Secured Marks</b></font></td><td align="center"><font color="white"><b> Max. Marks </b></font></td><td align="center"><font color="white"><b> Secured Marks</b></font></td><td align="center"><font color="white"><b> Max. Marks </b></font></td><td align="center"><font color="white"><b> Secured Marks</b></font></td><td align="center"><font color="white"><b> Max. Marks </b></font></td><td align="center"><font color="white"><b> Secured Marks</b></font></td><td align="center"><font color="white"><b> Max. Marks </b></font></td><td align="center"><font color="white"><b> Secured Marks</b></font></td><td align="center"><font color="white"><b> Max. Marks </b></font></td><td align="center"><font color="white"><b> Secured Marks</b></font></td><td align="center"><font color="white"><b> Max. Marks </b></font></td><td align="center"><font color="white"><b> Secured Marks</b></font></td><td align="center"><font color="white"><b> Max. Marks </b></font></td><td align="center"><font color="white"><b> Secured Marks</b></font></td><td align="center"><font color="white"><b> Grade </b></font></td><td align="center"><font color="white"><b> Sub. Credits </b></font></td><td align="center"><font color="white"><b> Grade Points </b></font></td></tr>',
            '<tr height="22px"><td align="center"><font color="">1</font></td><td align="center"><font color="">SPM</font></td><td align="center"><font color="">30</font></td><td align="center"><font color="">26</font></td><td align="center"><font color="">30</font></td><td align="center"><font color="">29</font></td><td align="center"><font color="">5</font></td><td align="center"><font color="">2</font></td><td align="center"><font color="">5</font></td><td align="center"><font color="">5</font></td><td align="center"><font color="">5</font></td><td align="center"><font color="">5</font></td><td align="center"><font color="">5</font></td><td align="center"><font color="">4.66</font></td><td align="center"><font color="">5</font></td><td align="center"><font color="">3</font></td><td align="center"><font color="">5</font></td><td align="center"><font color="">4</font></td><td align="center"><font color="">40</font></td><td align="center"><font color="">36</font></td><td align="center" bgcolor=""><font color="">-</font></td><td align="center" bgcolor=""><font color="">0</font></td><td align="center" bgcolor=""><font color="">0</font></td></tr>',
            '<tr height="22px"><td align="center"><font color="">2</font></td><td align="center"><font color="">NNDL</font></td><td align="center"><font color="">30</font></td><td align="center"><font color="">28</font></td><td align="center"><font color="">30</font></td><td align="center"><font color="">26</font></td><td align="center"><font color="">5</font></td><td align="center"><font color="">4</font></td><td align="center"><font color="">5</font></td><td align="center"><font color="">4.5</font></td><td align="center"><font color="">5</font></td><td align="center"><font color="">3.5</font></td><td align="center"><font color="">5</font></td><td align="center"><font color="">Ab</font></td><td align="center"><font color="">5</font></td><td align="center"><font color="">3.5</font></td><td align="center"><font color="">5</font></td><td align="center"><font color="">4.5</font></td><td align="center"><font color="">40</font></td><td align="center"><font color="">34</font></td><td align="center" bgcolor=""><font color="">-</font></td><td align="center" bgcolor=""><font color="">0</font></td><td align="center" bgcolor=""><font color="">0</font></td></tr>',
            '<tr height="22px"><td align="center"><font color="">3</font></td><td align="center"><font color="">PROJ/INT</font></td><td align="center"><font color="">-</font></td><td align="center"><font color="">-</font></td><td align="center"><font color="">-</font></td><td align="center"><font color="">-</font></td><td align="center"><font color="">-</font></td><td align="center"><font color="">-</font></td><td align="center"><font color="">-</font></td><td align="center"><font color="">-</font></td><td align="center"><font color="">-</font></td><td align="center"><font color="">-</font></td><td align="center"><font color="">-</font></td><td align="center"><font color="">-</font></td><td align="center"><font color="">-</font></td><td align="center"><font color="">-</font></td><td align="center"><font color="">-</font></td><td align="center"><font color="">-</font></td><td align="center"><font color="">50</font></td><td align="center"><font color="">41</font></td><td align="center" bgcolor=""><font color="">-</font></td><td align="center" bgcolor=""><font color="">0</font></td><td align="center" bgcolor=""><font color="">0</font></td></tr>',
            '<tr><td colspan="2"><font color="">Total</font></td><td align="center"><font color="">60</font></td><td align="center"><font color="">54</font></td><td align="center"><font color="">60</font></td><td align="center"><font color="">55</font></td><td align="center"><font color="">10</font></td><td align="center"><font color="">6</font></td><td align="center"><font color="">10</font></td><td align="center"><font color="">9.5</font></td><td align="center"><font color="">10</font></td><td align="center"><font color="">8.5</font></td><td align="center"><font color="">10</font></td><td align="center"><font color="">4.66</font></td><td align="center"><font color="">10</font></td><td align="center"><font color="">6.5</font></td><td align="center"><font color="">10</font></td><td align="center"><font color="">8.5</font></td><td align="center"><font color="">130</font></td><td align="center"><font color="">111</font></td><td align="center"><font color="">-</font></td><td align="center"><font color="">0</font></td><td align="center"><font color="">0</font></td></tr>',
            '<tr><td colspan="2"><font color="">Percentage</font></td><td align="center" colspan="2"><font color="">90</font></td><td align="center" colspan="2"><font color="">91.66</font></td><td align="center" colspan="2"><font color="">60</font></td><td align="center" colspan="2"><font color="">95</font></td><td align="center" colspan="2"><font color="">85</font></td><td align="center" colspan="2"><font color="">46.6</font></td><td align="center" colspan="2"><font color="">65</font></td><td align="center" colspan="2"><font color="">85</font></td><td align="center" colspan="2"><font color="">85.38</font></td><td align="center" colspan="3"><font color="">SGPA : -</font></td></tr>',
        ],
    )
)


headings = [
    "int1_max",
    "int1",
    "int2_max",
    "int2",
    "assn1_max",
    "assn1",
    "assn2_max",
    "assn2",
    "assn3_max",
    "assn3",
    "quiz1_max",
    "quiz1",
    "quiz2_max",
    "quiz2",
    "quiz3_max",
    "quiz3",
    "sess_max",
    "sess",
]


headings_main = [
    "int1_per",
    "int2_per",
    "assn1_per",
    "assn2_per",
    "assn3_per",
    "quiz1_per",
    "quiz2_per",
    "quiz3_per",
    "sess_per",
]


final_result = [
    {
        "SPM": {
            "int1_max": 30.0,
            "int1": 26.0,
            "int2_max": 30.0,
            "int2": 29.0,
            "assn1_max": 5.0,
            "assn1": 2.0,
            "assn2_max": 5.0,
            "assn2": 5.0,
            "assn3_max": 5.0,
            "assn3": 5.0,
            "quiz1_max": 5.0,
            "quiz1": 4.66,
            "quiz2_max": 5.0,
            "quiz2": 3.0,
            "quiz3_max": 5.0,
            "quiz3": 4.0,
            "sess_max": 40.0,
            "sess": 36.0,
            "ext_grade": "NA",
            "ext_sub_credits": 0,
            "ext_grade_pts": 0,
        },
        "NNDL": {
            "int1_max": 30.0,
            "int1": 28.0,
            "int2_max": 30.0,
            "int2": 26.0,
            "assn1_max": 5.0,
            "assn1": 4.0,
            "assn2_max": 5.0,
            "assn2": 4.5,
            "assn3_max": 5.0,
            "assn3": 3.5,
            "quiz1_max": 5.0,
            "quiz1": -1.0,
            "quiz2_max": 5.0,
            "quiz2": 3.5,
            "quiz3_max": 5.0,
            "quiz3": 4.5,
            "sess_max": 40.0,
            "sess": 34.0,
            "ext_grade": "NA",
            "ext_sub_credits": 0,
            "ext_grade_pts": 0,
        },
        "PROJ/INT": {
            "int1_max": 0.0,
            "int1": 0.0,
            "int2_max": 0.0,
            "int2": 0.0,
            "assn1_max": 0.0,
            "assn1": 0.0,
            "assn2_max": 0.0,
            "assn2": 0.0,
            "assn3_max": 0.0,
            "assn3": 0.0,
            "quiz1_max": 0.0,
            "quiz1": 0.0,
            "quiz2_max": 0.0,
            "quiz2": 0.0,
            "quiz3_max": 0.0,
            "quiz3": 0.0,
            "sess_max": 50.0,
            "sess": 41.0,
            "ext_grade": "NA",
            "ext_sub_credits": 0,
            "ext_grade_pts": 0,
        },
    },
    {
        "int1_max": 60.0,
        "int1": 54.0,
        "int2_max": 60.0,
        "int2": 55.0,
        "assn1_max": 10.0,
        "assn1": 6.0,
        "assn2_max": 10.0,
        "assn2": 9.5,
        "assn3_max": 10.0,
        "assn3": 8.5,
        "quiz1_max": 10.0,
        "quiz1": 4.66,
        "quiz2_max": 10.0,
        "quiz2": 6.5,
        "quiz3_max": 10.0,
        "quiz3": 8.5,
        "sess_max": 130.0,
        "sess": 111.0,
        "int1_per": 90.0,
        "int2_per": 91.66,
        "assn1_per": 60.0,
        "assn2_per": 95.0,
        "assn3_per": 85.0,
        "quiz1_per": 46.6,
        "quiz2_per": 65.0,
        "quiz3_per": 85.0,
        "sess_per": 85.38,
        "ext_sub_credits": 0,
        "ext_grade_pts": 0,
        "sgpa": None,
    },
]
