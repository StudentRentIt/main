$(document).ready(function(){
    $(function() {
    $( "#slider-price" ).slider({
      range: true,
      min: 0,
      max: 3000,
      values: [ 500, 1500 ],
      slide: function( event, ui ) {
        $( "#amount" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 100 ] );
      }
    });
    $( "#amount" ).val( "$" + $( "#slider-range" ).slider( "values", 0 ) +
      " - $" + $( "#slider-range" ).slider( "values", 100 ) );
  });
});