$(document).ready(function () {
    $(".homebtn").click(function () {
        console.log(this.id);
        window.location.href = "/" + this.id;
    });
})