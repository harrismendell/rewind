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
    swal({   title: "Are you sure you want to purchase \"" + data['record'] + "\" by " + data['band'] + "?",
        text: "It costs " + data['price'] + ". As this is a prototype, we will skip the payment process and add it to your account.",
        showCancelButton: true,
        confirmButtonText: "I want it!",
        cancelButtonText: "I don't want it!",
        closeOnConfirm: false,
        closeOnCancel: true },
        function(isConfirm){
            if (isConfirm) {
                swal({
                    title: "You bought \"" + data['record'] + "!\"",
                    text: "Thank you so much. It will now appear on your account page."},
                    function(){
                        $.post("/payment_confirm",
                        {
                            band: data['band'],
                            record: data['record'],
                            record_cover: data['record_cover'],
                            price: data['price'],
                            days_to_go: data['days_to_go']
                        })
                    }
                );
            }
        });
}

function validateForm() {
    var x = document.forms["signup"]["username"].value;
    var y = document.forms["signup"]["password"].value;
    var z = document.forms["signup"]["retype"].value;

    if (x == null || x == "") {
        alert("Name must be filled out");
        return false;
    }
    if (x.length < 6) {
        alert("Name must be at least 6 characters");
        return false;
    }
    if (y.length < 6) {
        alert("Password must be at least 6 characters");
        return false;
    }

    if (y != z){
        alert("Passwords must match");
        return false;
    }
}


