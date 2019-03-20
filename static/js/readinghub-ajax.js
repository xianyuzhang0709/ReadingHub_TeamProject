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

    $('.rango-add').click(function(){
        var catid = $(this).attr("data-catid");
        var url = $(this).attr("data-url");
        var title = $(this).attr("data-title");
        var me = $(this)
        $.get('/readinghub/add/',
            {category_id: catid, url: url, title: title}, function(data){
            $('#pages').html(data);
            me.hide();
        });
    });







});
