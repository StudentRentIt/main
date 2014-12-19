$(document).ready(function(){
    $.stellar();
    $('#search-school').popover({
        placement:'bottom',
        trigger:'manual',
    });

    $("#home-search").click(function() {
        // search from the main search box
        rent = $("#search-rent").val().replace(/\D/g,'');
        schoolLink = $("#search-school").data("link");
        bed = $("#search-bed").val();

        // set the submit to go to the school link
        if( schoolLink && schoolLink != "No Results"){
            $("#main-search-form").attr("action", schoolLink);
            $("#main-search-form").submit();
        }
        else {
            $('#search-school').popover('show');
        }
    });
});