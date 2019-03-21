$(document).ready( function() {
    $("#about-btn").addClass('btn btn-primary')

    $("#about-btn").click( function(event) {
        msgstr = $("#msg").html()
        msgstr = msgstr + "ooo"
        $("#msg").html(msgstr)
});


});