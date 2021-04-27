$(document).ready(function () {
    console.log('dsgdfgdfg')

    $('#ajaxButton').one('click', function () {
        $.get( "ajax-test/", function( data ) {
        $( ".result" ).html( data );
    })


});


})