$(document).ready( function() {
    function removeFavorite(obj) {
        var action = "remove";
        id = (obj).id;

        //post the data
        $.post(
            "/favorites/" + action + "/",
            {
                "property_id" : id
            },
            function(data) {
              alert("Response: " + data);
            },
            'json'
        );
    }

    function toggleFavorite(obj) {
        var action = "";
        id = (obj).id;

        //get action and change style
        if ( $(obj).hasClass( "btn-default" ) ) {
            action = "add";
        }
        else if ( $(obj).hasClass( "btn-heart" ) ) {
            action = "remove";
        }
        $(obj).toggleClass( "btn-default btn-heart" );

        //post the data
        $.post(
            "/favorites/" + action + "/",
            {
                "property_id" : id
            },
            function(data) {
              alert("Response: " + data);
            },
            'json'
        );
    }

    //change favorite for a user
    $('.btn-favorite').click(function() {
        toggleFavorite(this);
    });

    $('.btn-delete-favorite').click(function() {
        removeFavorite(this);
    });
});