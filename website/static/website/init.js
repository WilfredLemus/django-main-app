$(document).ready(function(){

    $("button#btn-add").on('click', function () {
        console.log("dsa")
        var name = $(this).closest("li").find("h2").text();
        var price = $(this).closest("li").find("span").text();
        if (name != "" && price != "") {
            OrderApp.addItemToCart(name, price);
        }
        makeTable();
    });

    $("#orderTable").on("click", "button.action-delete",function(){
        console.log('1313');
        var id = $(this).data("id");
        console.log(id);
        OrderApp.removeItemFromCart(id);
        makeTable();
    })

    $('#login').click(function(){
        $('#loginModule').toggle();
        $('#registrationModule').toggle();
    });
    makeTable();

});

function makeTable(){
    $("#orderTable").empty();
    var cart = JSON.parse(sessionStorage.getItem("cart"));
    if (cart) {
        var items=cart.products;
        var totalPrice=0;
        for(var item in items){
            totalPrice+=parseInt(items[item].price);
            var tr = $("<tr></tr>");
            var tdName = $("<td></td>").append(items[item].name);
            var tdPrice = $("<td></td>").append(items[item].price);
            var buttonIcon = $("<span></span>").addClass("glyphicon glyphicon-remove");
            var removeButton = $("<button></button>").addClass("btn btn-danger action-delete").attr("data-id",items[item].id).append(buttonIcon);
            var tdEmpty = $("<td></td>").append(removeButton);
            tr.append(tdName);
            tr.append(tdPrice);
            tr.append(tdEmpty);
            $("#orderTable").append(tr);
        }
        $("#totalPrice").html(totalPrice);


        // var container = $("#orderTable");
        // var source = $("#cartTemplate").html();
        // var template = Handlebars.compile(source);
        // var context = {products:cart.products};
        // var html = template(context);
        // container.html(html);
    };
}