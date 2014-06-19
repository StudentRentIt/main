$(document).ready( function() {
  //get current section
  function currentSection() {
    var curr;
    $('.submission-form-section').each(function(i, obj) {
        if (!$(obj).hasClass("hidden")) {
            curr = $(this).attr('id');
        }
    });
    return parseInt(curr.replace(/\D/g,''));
  }

  //function to show section-1
  function showSection1() {
      $("#form-section-1").removeClass("hidden");
      $("#form-section-2").addClass("hidden");
      $("#form-section-3").addClass("hidden");
      $("#form-section-4").addClass("hidden");

      //show-hide buttons
      $("#btn-previous").addClass( "hidden" );
      $("#btn-next").removeClass( "hidden" );
      $( ".submission-btn" ).addClass( "hidden" );

      //update menu list
      $("#form-label-1").addClass("label-success");
      $("#form-label-1").removeClass("label-default");
      $("#form-label-2").addClass("label-default");
      $("#form-label-2").removeClass("label-success");
      $("#form-label-3").addClass("label-default");
      $("#form-label-3").removeClass("label-success");
      $("#form-label-4").addClass("label-default");
      $("#form-label-4").removeClass("label-success");

      //update progress
      $( ".progress-bar" ).css({"width": "20%"});
  }

  //function to show section-2
  function showSection2() {
      $("#form-section-1").addClass("hidden");
      $("#form-section-2").removeClass("hidden");
      $("#form-section-3").addClass("hidden");
      $("#form-section-4").addClass("hidden");

      //show-hide buttons
      $("#btn-previous").removeClass( "hidden" );
      $("#btn-next").removeClass( "hidden" );
      $( ".submission-btn" ).addClass( "hidden" );

      //update menu list
      $("#form-label-1").addClass("label-default");
      $("#form-label-1").removeClass("label-success");
      $("#form-label-2").addClass("label-success");
      $("#form-label-2").removeClass("label-default");
      $("#form-label-3").addClass("label-default");
      $("#form-label-3").removeClass("label-success");
      $("#form-label-4").addClass("label-default");
      $("#form-label-4").removeClass("label-success");

      //update progress
      $( ".progress-bar" ).css({"width": "40%"});
  }

  //function to show section-3
  function showSection3() {
      //show section
      $("#form-section-1").addClass("hidden");
      $("#form-section-2").addClass("hidden");
      $("#form-section-3").removeClass("hidden");
      $("#form-section-4").addClass("hidden");

      //show-hide buttons
      $("#btn-previous").removeClass( "hidden" );
      $("#btn-next").removeClass( "hidden" );
      $( ".submission-btn" ).addClass( "hidden" );

      //update menu list
      $("#form-label-1").addClass("label-default");
      $("#form-label-1").removeClass("label-success");
      $("#form-label-2").addClass("label-default");
      $("#form-label-2").removeClass("label-success");
      $("#form-label-3").addClass("label-success");
      $("#form-label-3").removeClass("label-default");
      $("#form-label-4").addClass("label-default");
      $("#form-label-4").removeClass("label-success");

      //update progress
      $( ".progress-bar" ).css({"width": "60%"});
  }

  //function to show section-4
  function showSection4() {
      //show section
      $("#form-section-1").addClass("hidden");
      $("#form-section-2").addClass("hidden");
      $("#form-section-3").addClass("hidden");
      $("#form-section-4").removeClass("hidden");

      //show-hide buttons
      $("#btn-previous").removeClass( "hidden" );
      $("#btn-next").addClass( "hidden" );
      $( ".submission-btn" ).removeClass( "hidden" );

      //update menu list
      $("#form-label-1").addClass("label-default");
      $("#form-label-1").removeClass("label-success");
      $("#form-label-2").addClass("label-default");
      $("#form-label-2").removeClass("label-success");
      $("#form-label-3").addClass("label-default");
      $("#form-label-3").removeClass("label-success");
      $("#form-label-4").addClass("label-success");
      $("#form-label-4").removeClass("label-default");

      //update progress
      $( ".progress-bar" ).css({"width": "80%"});
  }

  //handle when a specific section button is pressed
  $( ".submission-form-menu-item" ).click(function() {
    target = $(this).attr('id');
    target_id = parseInt(target.replace(/\D/g,''));

    if (target_id === 1) {
      showSection1();
    }
    else if (target_id === 2) {
      showSection2();
    }
    else if (target_id === 3) {
      showSection3();
    }
    else if (target_id === 4) {
      showSection4();
    }
  });

  //handle when next button is clicked
  $( "#btn-next" ).click(function() {
      curr = currentSection();

      if ( curr === 1) {
          showSection2();
      }
      else if ( curr === 2) {
          showSection3();
      }
      else if ( curr === 3) {
          showSection4();
      }
  });

  //handle when previous button is clicked
  $( "#btn-previous" ).click(function() {
      curr = currentSection();

      if ( curr === 2) {
          showSection1();
      }
      else if ( curr === 3) {
          showSection2();
      }
      else if ( curr === 4) {
          showSection3();
      }
  });

});
