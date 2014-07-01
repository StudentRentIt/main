$(document).ready(function(){
    $(".main-nav").css("border-bottom", "none");

    $("#search-view").click(function() {
        var mapObject = $('#map-canvas');
        var listObject = $('#list-view');
        var source = "";
        var target = "";


        //set source and target
        if ($("#search-view").text().match("^List")){
            source = "mapview";
            target = "listview";
        }
        else if ($("#search-view").text().match("^Map")){
            source = "listview";
            target = "mapview";
        }

        //set non-delayed attributes
        if (target == "listview"){
            //set to 50% width
            mapObject.removeClass("map-view").addClass("list-view");
        }
        else if (target == "mapview"){
            listObject.addClass("hidden");
            mapObject.removeClass("list-view").addClass("map-view");
            //mapview.css("width", "100%");
            $("#search-view").text("List View");
        }

        //set delayed attributes
        setTimeout(changeView, 1050);
        function changeView() {
            if (target == "listview"){
                listObject.removeClass("hidden");
                $("#search-view").text("Map View");
            }
        }
    });

    //all multiple choice seach selections will be handled here
    $(".search-multi").click(function() {
        prependText = "<span class='glyphicon glyphicon-ok'></span> ";
        value = $(this).data("id");

        //set the type to perform logic splits further down
        // commented out 20140409 aww
        // if($(this).hasClass("search-multi-property-type")){
        //     ele_type = "property_type";
        //     obj = $("#property-type-input");
        // }
        if($(this).hasClass("search-multi-lease-type")){
            ele_type = "lease_type";
            obj = $("#lease-type-input");
        }
        else if($(this).hasClass("search-multi-lease-start")){
            ele_type = "lease_start";
            obj = $("#lease-start-input");
        }
        else if($(this).hasClass("search-multi-lease-term")){
            ele_type = "lease_term";
            obj = $("#lease-term-input");
        }

        /*
        if the button is currently active we need to set it inactive by
        giving the user a visual indication as well as remove the value
        from the hidden input string
        */
        if(!$(this).hasClass("active")){
            //tasks to the button
            $(this).css("background-color", "#5cb85c");
            $(this).css("color", "white");
            $(this).prepend(prependText);

            /*
            get which of the multi-search fields was chosen and add that value
            into the hidden input string
            */
            obj.val(function(i,val) {
                return val + (!val ? '' : ', ') + value;
            });
        }

        /*
        if it is active, perform various actions to make it inactive and reflect
        those changes in what the user sees as well as removing the value from
        the input string
        */
        if($(this).hasClass("active")){
            //tasks to the button
            $(this).css("background-color", "#eeeeee");
            $(this).css("color", "black");
            $(this).find(".glyphicon").remove();

            /*
            get which of the multi-search fields was chosen and remove that part
            of the string that is in the hidden input
            */
            // commented out 20140409 aww
            // if($(this).hasClass("search-multi-property-type")){
            //     $("#property-type-input").val($("#property-type-input").val().replace(value + ", ", ""));
            //     $("#property-type-input").val($("#property-type-input").val().replace(", " + value, ""));
            //     $("#property-type-input").val($("#property-type-input").val().replace(value, ""));
            // }
            if($(this).hasClass("search-multi-lease-term")){
                $("#lease-term-input").val($("#lease-type-input").val().replace(value + ", ", ""));
                $("#lease-term-input").val($("#lease-type-input").val().replace(", " + value, ""));
                $("#lease-term-input").val($("#lease-type-input").val().replace(value, ""));
            }
            if($(this).hasClass("search-multi-lease-start")){
                $("#lease-start-input").val($("#lease-start-input").val().replace(value + ", ", ""));
                $("#lease-start-input").val($("#lease-start-input").val().replace(", " + value, ""));
                $("#lease-start-input").val($("#lease-start-input").val().replace(value, ""));
            }
            if($(this).hasClass("search-multi-lease-term")){
                $("#lease-term-input").val($("#lease-term-input").val().replace(value + ", ", ""));
                $("#lease-term-input").val($("#lease-term-input").val().replace(", " + value, ""));
                $("#lease-term-input").val($("#lease-term-input").val().replace(value, ""));
            }
        }

        $(this).toggleClass("active");
    });
});