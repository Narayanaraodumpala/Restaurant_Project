function Signin(){
  var name = document.getElementById("name");
  var subject = document.getElementById("password").value;
  var phone = document.getElementById("phone").value;
  var email = document.getElementById("email").value;
  var message = document.getElementById("message").value;
  var mgen=document.getElementById("gender")
  var fmgen=document.getElementById("fgender")
  var error_message = document.getElementById("error_message");

  error_message.style.padding = "10px";

  var text;
  if(name.length < 5 || name.value.trim()===""){
    text = "Please Enter valid Name , it should not contain blank spaces";
    error_message.innerHTML = text;
    return false;
  }
  if(subject.length < 5 || subject.trim()===""){
    text = "Password Should Contain atleast 5 letters, it should not contain blank spaces ";
    error_message.innerHTML = text;
    return false;
  }
  if(isNaN(phone) || phone.length !== 10){
    text = "Please Enter valid Phone Number , it must contain 10 numbers";
    error_message.innerHTML = text;
    return false;
  }
  if(email.indexOf("@") === -1 || email.length < 6){
    text = "Please Enter valid Email";
    error_message.innerHTML = text;
    return false;
  }
  if(message.length <=40 ){
    text = "Please Enter More Than 40 Characters";
    error_message.innerHTML = text;
    return false;
  }

  return true;
}