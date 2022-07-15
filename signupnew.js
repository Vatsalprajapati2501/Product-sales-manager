function formValidation() {
    const firstname = document.getElementById("fname");
    const lastname = document.getElementById("lname");
    const email = document.getElementById("email");
    const upassword = document.getElementById("password");
    const confirmPassword = document.getElementById("cpassword");

    if (firstname.value.length < 2 || firstname.value.length > 20) {
        alert("Name length should be more than 2 and less than 21");
        firstname.focus();
        return false;
    }
    if (lastname.value.length < 2 || lastname.value.length > 20) {
        alert("Name length should be more than 2 and less than 21");
        lastname.focus();
        return false;
    }
    if (!email.value.match(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/)) {
        alert("Please enter a valid email!");
        email.focus();
        return false;
    }
    if (!upassword.value.match(/^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$/) || password.value.length < 8) {
        alert("Password should contain 8 characters having a number, lower and upper case and special character.");
        upassword.focus();
        return false;
    }

    if (upassword.value != confirmPassword.value) {
        alert("Passwords do not match");
        confirmPassword.focus();
        return false;
    }
    return true;
}