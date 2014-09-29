$( document ).ready( function (){
    // add or remove a property from group search
    $('.btn-add-group-search').off('click');
    $('.btn-add-group-search').on('click', function() {
        id = $( this ).data( "id" );

        $.post('/search/group/property/',
            {"property_id": id}
        );

        // change to remove button
        if ( $( this ).hasClass( "btn-add" ) ){
            $( this ).html( '<span class="glyphicon glyphicon-plus"></span>' );
            $( this ).addClass( "btn-remove" ).removeClass( "btn-add" );
            $( this ).attr( "data-original-title", "Add to Group Search" );
        }
        else if ( $( this ).hasClass( "btn-remove" ) ){
            $(this).html( "<span class='glyphicon glyphicon-minus'></span>" );
            $( this ).addClass( "btn-add" ).removeClass( "btn-remove" );
            $( this ).attr( "data-original-title", "Remove from Group Search" );
        }
    });
});