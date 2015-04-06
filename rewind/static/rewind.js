$(function() {
    $('.menuitem').each(function() {
        if(window.location.pathname == $(this).find('a').attr('href')){
            $(this).addClass('active');
        }
    });

    //Courtesy of http://bootsnipp.com/snippets/featured/thumbnail-caption-hover-effect
    $('.shopthumbnail').hover(
        function(){
            $(this).find('.caption').slideDown(300);
        },
        function(){
            $(this).find('.caption').slideUp(300);
        }
);

});

function confirmClaim(data){
    swal({   title: "Are you sure you want to purchase \"" + data[2] + "\" by " + data[1] + "?",
        text: "It costs " + data[4] + ". As this is a prototype, we will skip the payment process and add it to your account.",
        showCancelButton: true,
        confirmButtonText: "I want it!",
        cancelButtonText: "I don't want it!",
        closeOnConfirm: false,
        closeOnCancel: true },
        function(isConfirm){
            if (isConfirm) {
                swal({
                    title: "You bought \"" + data[2] + "!\"",
                    text: "We will now route you to the account page."},
                    function(){
                        $.post("/payment_confirm",
                        {
                            band: data[1],
                            record: data[2],
                            record_cover: data[3],
                            price: data[4]
                        })
                    }
                );
            }
        });
}

//$("[rel='tooltip']").tooltip();


