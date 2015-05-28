$(document).ready(function(){

    $("button#btn-add").on('click', function () {
        var name = $(this).closest("li").find("h2").text();
        var price = $(this).closest("li").find("span").text();
        if (name != "" && price != "") {
            OrderApp.addItemToCart(name, price);
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
    $("#orderTable").empty();
    var cart = JSON.parse(sessionStorage.getItem("cart"));
    if (cart) {
        var items=cart.products;

        for(var item in items){
            var tr = $("<tr></tr>");
            var tdName = $("<td></td>").append(items[item].name);
            var tdPrice = $("<td></td>").append(items[item].price);
            var tdEmpty = $("<td></td>").append('');
            tr.append(tdName);
            tr.append(tdPrice);
            tr.append(tdEmpty);
            $("#orderTable").append(tr);
        }
        // var container = $("#orderTable");
        // var source = $("#cartTemplate").html();
        // var template = Handlebars.compile(source);
        // var context = {products:cart.products};
        // var html = template(context);
        // container.html(html);
    };
}