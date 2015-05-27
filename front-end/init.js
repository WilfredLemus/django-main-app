$(document).ready(function(){

    $("button#btn-add").on('click', function () {
        var name = $(this).closest("li").find("h2").text();
        // var price = $(".orderPrice").text();
        if (name != "") {
            OrderApp.addItemToCart(name, 12);
        }
    });

    $('#login').click(function(){
        $('#loginModule').toggle();
        $('#registrationModule').toggle();
    });
});