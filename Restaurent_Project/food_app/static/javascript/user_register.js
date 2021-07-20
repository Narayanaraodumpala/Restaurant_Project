function  validate(){
   var name=document.getElementById('name')
    var passw=document.getElementById('password')
  var   email=document.getElementById('email')
  var   mobile=document.getElementById('mob')
   var  lname=document.getElementById('lname')

    if (name.value.trim()===''){

         var  llname=document.getElementById('lname').style.visibility='visible';
        return false;

    }
    else if (passw.value.trim()===''|| passw.value.length<5){
        var lapss=document.getElementById('lpass').style.visibility='visible';
        return  false;
    }
    else if(email.indexOf("@") === -1 ||email.value.length<6){
        var lemail=document.getElementById('lemail').style.visibility='visible'
        return false;
    }
    else  if (mobile.value.trim()===''||mobile.value.length<10){
        var lmob=document.getElementById('lmob').style.visibility='visible'
        return  false;


    }
    else {
        return true
    }
}