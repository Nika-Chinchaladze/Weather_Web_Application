document.getElementById("slide1").addEventListener("click", function() {
    document.getElementById("container").scrollLeft -= 50;
})

document.getElementById("slide2").addEventListener("click", function() {
    document.getElementById("container").scrollLeft += 50;
})

document.getElementById("slide3").addEventListener("click", function() {
    document.getElementById("containerHour").scrollLeft -= 50;
})

document.getElementById("slide4").addEventListener("click", function() {
    document.getElementById("containerHour").scrollLeft += 50;
})
