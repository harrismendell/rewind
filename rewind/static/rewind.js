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
    swal({   title: "Are you sure you want to purchase " + data + "?",
        text: "As this is a prototype, we will skip the payment process and add it to your account.",
        type: "warning",
        showCancelButton: true,
        confirmButtonColor: "#DD6B55",
        confirmButtonText: "Claim it!",
        cancelButtonText: "No, cancel!",
        closeOnConfirm: false,
        closeOnCancel: false },
        function(isConfirm){
            if (isConfirm) {
                swal("You bought it!", "We will now route you to the account page.", "success");
            }
            else {swal("Cancelled", "You did not buy it.", "error");
            } });
    debugger;
}

//$("[rel='tooltip']").tooltip();


