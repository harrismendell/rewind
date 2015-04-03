$(function() {
    $('.menuitem').each(function() {
        if(window.location.pathname == $(this).find('a').attr('href')){
            $(this).addClass('active');
        }
    });

    $('.thumbnail').hover(
        function(){
            $(this).find('.caption').slideDown(300);
        },
        function(){
            $(this).find('.caption').slideUp(300);
        }
);

});

//$("[rel='tooltip']").tooltip();


