function init() {
    var num = document.getElementById("num");
    num.value=0;
    num.disabled="disabled";
    var oButton=document.getElementsByTagName("input")
    for (var i=0;i<oButton.length;i++){
        oButton[i].onclick=function () {
            if(isNumber(this.value)){
                num.value=(num.value+this.value)*1
            }else {
                //alert("feishuzi")
                var btn_num=this.value;
                switch (btn_num){
                    case "+":
                        alert("1111");
                        break;
                    case "-":
                        alert("2222");
                        break;
                    case "*":
                        alert("3333");
                        break;
                    case "/":
                        alert("4444");
                        break;
                    case ".":
                        alert("5555");
                        break;
                }
            }
        }
    }
}
function isNumber(n) {
    if (isNaN(n)==false){
        return true; //参数n是数字
    }else {
        return false; //参数n不是数字
    }
}