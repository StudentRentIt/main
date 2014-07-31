$(document).ready(function(){
    $(".btn-toggle-property").click(function() {
        id = $(this).data("id");
        title = $(this).data("title")

        //post the data
        $.post(
            "/property/toggle/" + id + "/",
            {
                "property_id" : id
            }
        );

        //collapse the section and tell the user it has been hidden
        hiddenText = '<div class="row text-center"><div class="col-xs-offset-2 col-xs-8">' +
            title + ' has been hidden from your future searches. You can unhide it at <a href="/property/hidden/">Hidden Properties</a>.' +
            '</div></div>'
        $(this).closest(".list-view-row").html(hiddenText);

        //remove tooltip
        $( ".tooltip" ).remove();
    });
});