var minutes = 30
var seconds = 00
// Update the count down every 1 second
var x = setInterval(function () {

    



    // Output the result in an element with id="demo"
    document.getElementById("demo").innerHTML = minutes + " MINUTES   " + seconds + " SECONDS   ";
    
    
    if(seconds==0){minutes=minutes-1;seconds=60}
    seconds=seconds-1
    // If the count down is over, write some text 
    if (minutes < 0) {
        clearInterval(x);
        document.getElementById("demo").innerHTML = "TIME OUT";
        alert("Your Time Is Over")
    }
}, 1000);