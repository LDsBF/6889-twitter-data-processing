$(document).ready(function () {
    $("#title").html(data["title"]);
    $("#wordCloudGraph").attr("src", data["img1"]);
    $("#histogramGraph").attr("src", data["img2"]);

    console.log(typeof id);
    console.log(id === "0");

    $("#prev").click(function () {
        window.location.href = "/" + (parseInt(id) - 1).toString();
    });

    $("#next").click(function () {
        window.location.href = "/" + (parseInt(id) + 1).toString();
    });

    if (id === "0") {
        console.log("disabled");
        $("#prev").remove();
    }
})