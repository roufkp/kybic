   


  document.addEventListener("DOMContentLoaded", function() {
    var button = document.getElementById("open");
    var ul = document.getElementById("ul");
    button.addEventListener("click", open);
    // console.log("Button clicked!");

  });
  
  function open() {
    // Your code here
    ul.classList.toggle("active");
  }