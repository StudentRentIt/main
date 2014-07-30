$(document).ready(function(){
    function convertToSlug(Text)
    {
        return Text
            .toLowerCase()
            .replace(/ /g,'-')
            .replace(/[^\w-]+/g,'')
            ;
    }

    $(".btn-restore").click(function() {
        // restore a property to be shown in searches for a specific user
        id = $(this).data("id");
        title = $(this).data("title")

        //post the data
        $.post(
            "/property/toggle/" + id + "/",
            {
                "property_id" : id
            }
        );

        //collapse the table row and tell the user they will now see the property
        showText = '<td colspan="3" class="text-center">' + title + ' will now bee seen in your future searches. ' +
                   '<a href="/property/' + id + '/' + convertToSlug(title) + '/">View Property</a> now.'
        $(this).closest("tr").html(showText);

        //remove tooltip
        $( ".tooltip" ).remove();
    });
});