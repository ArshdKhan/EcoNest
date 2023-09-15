let form = document.querySelecter('form');

form.addEventListener('submit', (e) => {
  e.preventDefault();
  return false;
});

function Myalter()
{
  var email = document.getElementsById("email");
  var password = document.getElementById("password");
  if (email.value === "")
  {
    alert("Please Fill All Fields");
  }
  else
  {
    alert("Logged in!");
  }
}