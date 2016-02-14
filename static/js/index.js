
function updatePage() {
    $.get("ajax/update", function(data) {
        $(".contents").html(data);
    });    
}

setInterval(updatePage, 1000);
