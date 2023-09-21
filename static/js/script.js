// These variables are assigned to html elements
const buttonNav = document.getElementById("nav-button");
const username = document.getElementById("username");
const buttonForm = document.getElementById("button-form");

let clicked = false;

/**
 *  On click, it takes back the username (The username located in the Navbar)
 *  to its original position when the Navbar-toggler button is clicked
 *  Because when the Navbar-toggler button is clicked
 *  the username is getting pushed down
 */
buttonNav.addEventListener("click", function() {
    if (!clicked) {
        username.style.cssText = "margin-bottom: 128px;";
        clicked = true;
    }
    else {
        username.style.cssText = "margin-bottom: 0px;";
        clicked = false;
    }
})

/**
 *  Dismisses the alert messages after 3 seconds
 */
setTimeout(function() {
    let messages = document.getElementById("msg");
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 3000);

/**
 * Shows a confirm popup message when the user submits a booking
 */
buttonForm.addEventListener("click", function(e) {
    let result = confirm('Are you sure you want to book this table?');
    if (result === false) {
        e.preventDefault();
    }
})

/**
 * Shows a confirm popup message when the user signs out
 */
function checker() {
    let final = confirm('Are you sure you want to sign out?');
    if (final == false) {
        event.preventDefault();
    }
}