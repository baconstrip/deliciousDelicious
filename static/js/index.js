
function updatePage() {
    $.get("ajax/update", function(data) {
        $(".contents").html(data);
    });    
}

updatePage();
setInterval(updatePage(), 1000);
