$(document).ready( function() {
    $('#likes').click(function(){
        var boookid;
        boookid = $(this).attr("data-boookid");
        $.get('/readinghub/like/', {book_id: boookid}, function(data){
            $('#like_count').html(data);
            $('#likes').hide();
        });
    });

    $('#suggestion').keyup(function(){
        var query;
        query = $(this).val();
        $.get('/readinghub/suggest/', {suggestion: query}, function(data){
            $('#cats').html(data);
        });
    });

});
