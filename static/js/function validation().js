function validation()
{
    var password = document.getElementById('password').value;
    var numbers = /[0-9]/g;
    var lowerCaseLetters = /[a-z]/g;
    var upperCaseLetters = /[A-Z]/g;

    if(password == ""){
    alert('Password cannot be empty');
    }
    if(password.match(numbers)){
    
    }
    else{
        var ele = document.getElementById('pwd')
        ele.innerText='Password must contain atleast 1 numeric value'
        // alert('Password must contain atleast 1 numeric value');
    }
    if(password.match(lowerCaseLetters)){
    
    }
    else{
        alert('Password must contain atleast 1 lower case letter');
    }
    if(password.match(upperCaseLetters)){
    
    }
    else{
        alert('Password must contain atleast 1 upper case letter');
    }
    if(password.value.length >= 8) {
        
      } 
      else {
        alert('Password must be atleast 8 characters');
      }
}