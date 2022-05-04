$(document).ready(function () {
    $("#title").html(data["title"]);
    $("#dataflow").attr("src", data["img"]);

    $("#prev").click(function () {
        window.location.href = "/" + (parseInt(id) - 1).toString();
    });
})