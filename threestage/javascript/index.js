/*
var myscore = 100;
var str;
var n = parseInt(myscore/10);
switch (n){
    case 10:
        str = "youxiu";
        break;
    case 9:
        str = "youxiu";
        break;
    case 8:
    case 7:
        str = "lianghao";
    default :
        str = "jige"
}
console.log(str)
*/

// 1+2+3+4+5+6 =5050
/*
var i;
var sum=0;
for (i=0;i<=100;i++){
    sum = sum + i;
}
console.log(sum)
/*
 */

/*
var str = "5201314199006061234"
console.log(str.substr(0,3))
console.log(str.substring(0,3))
 */

/*
var d1 = new Date();
var d2 = new Date("2020-1-1 10:58:58")
console.log(d2.getDate())
*/

/*
var arrayObj=new Array();
*/

function show1() {
    //alert("123456")
    //document.getElementById("userName").value="999"
    var xb=document.getElementsByName("xb");
    var xbText;
    if (xb[0].checked){
        xbText=xb[0].value;
    }else {
        xbText=xb[1].value;
    }
    alert(xbText)
}

function ymd() {
    var yyyy=document.getElementById("yyyy");
    var mm=document.getElementById("mm");
    var dd=document.getElementById("dd");
    var date=new Date();
    var year = parseInt(date.getFullYear());
    initSelect(yyyy,1999,year);
    initSelect(mm,1,12);
    initSelect(dd,1,31);
    var n=yyyy.length;
    yyyy.selectedIndex=Math.round(n/2);
}

function initSelect(obj,start,end) {
    for (var i=start;i<=end;i++){
        obj.options.add(new Option(i,i))
    }
}

function ceshi() {
    var mm=document.getElementById("mm");
    var dd=document.getElementById("dd");
    var m=parseInt(mm.value);

    var dayEnd;
    if (m==4 || m==6 || m==9 || m=11){
        dayEnd=30;
    }else if{
        dayEnd=28;
    }else {
        dayEnd=31;
    }
    dd.options.length=0;
    initSelect(dd,1,dayEnd);
}
