var day =70;
var word = document.getElementById('user').innerHTML.substring(1,6);
var l =  0;
function prv(){
        day = day -1;
        document.getElementById('daynum').innerHTML = "روز" + day + "واجور";
        tem = reset_();     
};
function nxt(){
        day = day +1;
        document.getElementById('daynum').innerHTML =  " روز " + day + " واجور ";
        tem = reset_();
        // jdd
};
function disablebut(){
        document.getElementById('nxt').disabled='true';
        document.getElementById('pvs').disabled='true';
};
function enablebut(){
        document.getElementById('nxt').disabled='';
        document.getElementById('pvs').disabled='';
};
var r_e = reset_();
document.getElementById('sub').addEventListener('click', function() {
        l = l+1;
        g = winif(main_vaj(word));      
});
function winif(g){
        if ( g =='ggggg'){
                tem = enablebut();
                massage = " شما با "+ l +" حدس به پاسخ رسیدید!";
                let win_text = document.getElementById('wintex');
                win_text.innerHTML = massage;
                win_text.style.display = 'inline-flex';
                p = l * 51;
                win_text.style.marginTop = p +'px';  
                document.getElementById("sub").disabled = true;   
        }      
};
function main_vaj(word){

                
                var answer='';
                var guss = ''; 
                // دریافت کلمه از کاربر
                for (let i = 1 ; i<6 ; i++){
                        var sel_ = "sel-"+i+"-"+l;
                        guss = guss + document.getElementById(sel_).value;

                }
                var length = guss.length;
                // بررسی 5 حرفی بودن کلمه
                if(length == 5){
                        answer = compair(guss,word);
                }
                else{
                        alert('5 word is required');
                }
                           // مدیریت نمایش 
                for (let i = 1 ; i<6 ; i++){
                        var sel_ = "sel-"+i+"-"+(l);
                        var sel_n = "sel-"+i+"-"+(l+1);
                        document.getElementById(sel_).disabled =true;
                        document.getElementById(sel_).style.height = "40px";
                        document.getElementById(sel_).style.opacity = "0.9"; 
                        if(answer !="ggggg"){
                                document.getElementById(sel_n).disabled =false; 
                                document.getElementById(sel_n).style.height = "40px";      
                        }
                       
                }
                // رنگ کردن بگ گراند سلول ها
                let anselms = document.getElementsByClassName('row_'+(l));
                var turn = colorify(answer,anselms);
                var inp = focusFirstInput();
                
return answer;

};
function colorify(answer,anselms){
for (let j = 0 ; j<5 ; j++){
                        if(answer[j] == "g") {
                                // alert(answer[4-j])
                                anselms[j].style.backgroundColor= "#66ff00";
                        } else if(answer[j] == "y"){
                                // alert(answer[4-j])
                                anselms[j].style.backgroundColor= "#FFFF00";
                        }else{
                                // alert(answer[4-j])
                                anselms[j].style.backgroundColor= "#FF2222";
                        }
                }
};
function reset_(){  
        l=0;
        document.getElementById('wintex').style.display = 'none';
        document.getElementById("sub").disabled = false;
        for (let i = 1 ; i<6 ; i++){
                var sel_ = "sel-"+i+"-1";
                document.getElementById(sel_).disabled = false;
                }
        for (let j = 1 ; j<9 ; j++){
                for (let i = 1 ; i<6 ; i++){
                        var sel_ = "sel-"+i+"-"+j;
                        var sel_n = "sel-"+i+"-"+(j+1);
                        document.getElementById(sel_n).disabled = true;
                        document.getElementById(sel_n).style.height = "1px";
                        document.getElementById(sel_).value = '';
                        document.getElementById(sel_).style.backgroundColor= '#777'; 
                }
};
    var inp = focusFirstInput();
};
function focusFirstInput() {
                var inputElements = document.getElementsByTagName('input');
                try {
                  for (var i = 0; i < inputElements.length; i++) {
                    var e = inputElements[i];
                    // uses jQuery for hasClass()
                    if (e.tagName == 'INPUT' &&   
                        e.value === '') {
                      e.focus();
                //       alert(i)
                      return;
                    }
                  }
                } catch (e) {} // in case IE gets angry
                return 0;
}
window.onload = focusFirstInput;
function autoTab( field2) {
                 document.getElementById(field2).focus();
        }
function replacechar(str,index,char){
        return str.substring(0, index)+char+str.substring(index+1);
};
function compair(guss,word) { //مقایسه دو کلمه و ارسال پاسخ
        answer = '';
        for (let i = 0 ; i< 5 ; i++){
                if (guss[i] == word[i]){
                        answer = answer +"g";
                        word = replacechar(word,i,"o"); 
                
                }
                else{
                        answer = answer +"o";
                }
        }
        // alert('for-1'+answer+'   '+word)
        for (let j = 0 ; j<5 ; j++){
                if(answer[j] == 'o'){
                        if(word.includes(guss[j])){
                                answer = replacechar(answer,j,"y");
                                index = word.indexOf(guss[j]);
                                word = replacechar(word,index,'o');
                        } else{
                                answer = replacechar(answer,j,"r");
                        }
                }
        }
        return answer;
        
};