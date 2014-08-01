$(document).ready(function(){
    $.stellar();

    $("#home-search").click(function() {
        // search from the main search box
        rent = $("#search-rent").val().replace(/\D/g,'');
        schoolLink = $("#search-school").data("link");
        bed = $("#search-bed").val();
        $("#main-search-form").attr("action", schoolLink);
    });
});