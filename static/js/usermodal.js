$( document ).ready(function() {

    //change to the register view
    $("#btn-register").click(function(){

        //hide login
        $("#mLogin").addClass("hidden");

        //show register, title
        $("#mRegister").removeClass("hidden");
        $("#user-modal-title").text("Sign Up");

    });

    $("#btn-login").click(function(){
        set_to_login();
    });

    $("#btn-user-cancel").click(function(){
        set_to_login();
    });

    function set_to_login() {
        //change to the login vie
        //hide register
        $("#mRegister").addClass("hidden");

        //show login, button, title
        $("#mLogin").removeClass("hidden");
        $("#user-modal-title").text("Login");
    }

});