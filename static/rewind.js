$(function() {
    $('.menuitem').each(function() {
        if(window.location.pathname == $(this).find('a').attr('href')){
            $(this).addClass('active');
        }
    });

    
});

