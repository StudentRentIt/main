$(document).ready(function() {
    $(".btn-add").click(function(){
        id = $(this).data("id");

        $.post('/scrape/add/' + id + '/');
        $(this).text("Added");
    });
});