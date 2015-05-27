$(document).ready(function(){

    $("button#btn-add").on('click', function () {
        var name = $(this).closest("li").find("h2").text();
        // var price = $(".orderPrice").text();
        if (name != "") {
            OrderApp.addItemToCart(name, 12);
        }
        makeTable()
    });

    $('#login').click(function(){
        $('#loginModule').toggle();
        $('#registrationModule').toggle();
    });
    makeTable()




});

function makeTable(){
    var cart = JSON.parse(sessionStorage.getItem("cart"));
    if (cart) {
        var container = $("#orderTable");
        var source = $("#cartTemplate").html();
        var template = Handlebars.compile(source);
        var context = {products:cart.products};
        var html = template(context);
        container.html(html);
    };
}