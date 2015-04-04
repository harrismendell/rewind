$(function() {
    $('.menuitem').each(function() {
        if(window.location.pathname == $(this).find('a').attr('href')){
            $(this).addClass('active');
        }
    });

    //Courtesy of http://bootsnipp.com/snippets/featured/thumbnail-caption-hover-effect
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


