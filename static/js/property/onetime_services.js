$(document).ready(function(){
    //$(document).on('click', ".btn-service", function() {
    $( ".btn-service" ).click(function(){
        //change button
        $(this).toggleClass("btn-add btn-added btn-success btn-default");

        //change panel
        var parentPanel = $(this).parents('.panel');
        parentPanel.toggleClass("panel-default panel-success");

        //add service price to the subtotal
        var subtotalObj = $( "#subtotal" );
        var price = parseInt($(this).data("price"));
        var previousSubTotal = parseInt($( "#subtotal" ).text());

        if ($(this).hasClass( "btn-added" )) {
            nextSubTotal = previousSubTotal + price;
            $(this).text("Remove From Cart");
        }
        else if ($(this).hasClass( "btn-add" )) {
            var nextSubTotal = previousSubTotal - price;
            $(this).text("Add To Cart");
        }

        //update the values
        subtotalObj.text(nextSubTotal);
    });

    //update the services hidden input
    $( "#stripe-button").click(function(){
        console.log("button stripe pressed");
        var services = "";
        $( ".panel-service" ).each(function(i) {
        if ($(this).hasClass( "panel-success" )) {
                //get the ids that are selected for services
                id = $(this).find( ".btn-added" ).attr("id").replace("service","");
                console.log("adding " + id);
                if (services !== "") {
                    services = services + ", " + id;
                }
                else {
                    services = id;
                }
            }
        });
        $( "#services-input" ).val(services);
    });
});