$( document ).ready( function() {
    $( ".group-comment-add" ).click( function() {
        $(this).parent( ".group-comments" ).load(document.URL +  this);
    });
});