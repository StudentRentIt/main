$(document).ready(function(){
    $(document).on('click', ".btn-add", function() {
    /*
    button has btn-add if the service/package is not currently active or set to
    be active. When the user clicks to add the button we want to change the panel
    and button to show that the service/package will be added.
    */
    //$(".btn-add").click(function(){
        //change button stuff
        $(this).toggleClass("btn-add btn-added btn-success btn-default");
        if ($(this).hasClass("btn-package")) {
            $(this).text("Remove Package");

            //add the new values to the hidden package input
            id = $(this).attr("id").replace("package","");
            $("#package-input").val(id);

            //disable the other packages on front-end because there can only be 1 chosen
            $( ".panel-package" ).each(function() {
              if ($(this).hasClass( "panel-success" )) {
                  //change the panel
                  $(this).removeClass("panel-success");
                  $(this).addClass("panel-default");

                  //change the button in the previously active package
                  btnAdd = $(this).find( ".btn-added" );
                  btnAdd.removeClass( "btn-added btn-success" );
                  btnAdd.addClass( "btn-add btn-default" );
                  btnAdd.text( "Add Package" );
              }
            });
        }
        else if ($(this).hasClass("btn-service-recurring")) {
            $(this).text("Remove Service");
        }
        else if ($(this).hasClass("btn-service-onetime")) {
            $(this).text("Remove Service");
        }

        //change panel stuff
        parentPanel = $(this).parents('.panel');
        parentPanel.toggleClass("panel-default panel-success");

        //modify the input values
    });


    $(document).on('click', ".btn-added", function() {
    /*
    button has btn-added if the service or package has been added or is set
    to be added. When a user clicks this button we want to change the panel to
    show that the package/service is not currently active and also change the button
    to show the same.
    */
    //$(".btn-added").click(function(){
        //change button stuff
        $(this).toggleClass("btn-add btn-added btn-success btn-default");

        if ($(this).hasClass("btn-package")) {
            $(this).text("Add Package");
            $("#package-input").val("");
        }
        else if ($(this).hasClass("btn-service-recurring")) {
            $(this).text("Add Service");
        }
        else if ($(this).hasClass("btn-service-onetime")) {
            $(this).text("Purchase Service");
        }

        //change panel stuff
        parentPanel = $(this).parents('.panel');
        parentPanel.toggleClass("panel-default panel-success");
    });

    $(document).on('click', "#btn-submit", function() {
        //set the value of the services input to what is selected
        var futureServices = "";

        $( ".panel-service" ).each(function(i) {
            if ($(this).hasClass( "panel-success" )) {
                //get the ids that are selected for services
                id = $(this).find( ".btn-added" ).attr("id").replace("service","");
                if (futureServices !== "") {
                    futureServices = futureServices + ", " + id;
                }
                else {
                    futureServices = id;
                }
            }
        });
        $( "#services-input" ).val(futureServices);
    });
});