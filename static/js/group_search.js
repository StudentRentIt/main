$( document ).ready( function (){
    $( ".btn-add-group-search" ).unbind().click( function() {
        id = $( this ).data( "id" );

        $.post('/search/group/property/',
            {"property_id": id}
        );

        // change to remove button
        if ( $( this ).hasClass( "btn-add" ) ){
            $( this ).html( "<span class='glyphicon glyphicon-minus'></span>" );
        }
        else if ( $( this ).hasClass( "btn-remove" ) ){
            $( this ).html( "<span class='glyphicon glyphicon-plus'></span>" );
        }
    });
});