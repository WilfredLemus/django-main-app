"use strict";
var OrderApp = (function () {

    // var ordersResult;
    var id = 0;

    //set where to add content and get data from local storage
    var displayCart = function() {
        var container = $("#cartItems tbody");
        container.empty();
        //Get cart data from local storage
        var cart = JSON.parse(sessionStorage.getItem("cart"));
        //Display cart items
        helpers.displayWithJade(container, "views/cart-items.jade",{
            cart: cart
        });
    }


    var displayOrderTable = function(){
        var orderRes = new Resource("http://localhost:3000/api/orders");
        orderRes.query().then(function(res){
            var container = $("#tableOfOrders tbody");
            container.empty();
            var orders = res;
            console.log(orders);

            helpers.displayWithJade(container, "views/order-table.jade",{
                orders: orders
            });
        });
    }


    var sendOrder = function(seat){
        var cart = JSON.parse(sessionStorage.getItem("cart"));
        console.log(cart);
        var order = new Resource("http://localhost:3000/api/orders");
        order.create(cart, seat);
    }

        // $.ajax({
        //     "method": "get",
        //     "url": "http://localhost:3000/api/orders",
        //     "dataType": "json"
        // }).done(function (result) {
        //     ordersResult = result;
        //     for (var order in ordersResult) {
        //         if (ordersResult[order] != null) {
        //             container.append("<tr.success><td.col-xs-8>" + ordersResult[order].name +
        //             "</td><td.col-xs-3>" + ordersResult[order].price +
        //             "</td><td.col-xs-1>span.glyphicon.glyphicon-remove</td>");
        //             var actions = $('.btn_actions_' + order);

        //             $('#btn_delete_' + order).click(function (target) {
        //                 var id = event.target.getAttribute('data-id');
        //                 deleteorder(id);
        //             });
        //         }
        //     }
        // })

    var removeItemFromCart = function(inerId) {
        var cart = JSON.parse(sessionStorage.getItem("cart"));
        for (var i=0;i<cart.products.length;i++){
            if (cart.products[i].id === inerId){
                cart.products.splice(i,1);
                break;
            }
        }

        for (var i=0;i<cart.products.length;i++){
            cart.products[i].id = i+1;
        }

        sessionStorage.setItem("cart", JSON.stringify(cart));
    }

    var update = function(id, name, email) {
        $.ajax({
            "method": "put",
            "url": "http://localhost:3000/api/orders/" + id,
            "data": {
                "name": name,
                "email": email
            },
            "dataType": "json"
        }).done(function (result) {
            displayResults();
        })
    }

    var addItemToCart = function(name, price) {
        var cart = JSON.parse(sessionStorage.getItem("cart"));
        if (cart === null) {

            cart = {
                table:0,
                products: []
            }
        };
        id = cart.products.length+1;
        cart.products.push({
            id: id,
            name: name,
            price: price
        })

        sessionStorage.setItem("cart", JSON.stringify(cart));
    }

    var addTable = function(number) {
        var cart = JSON.parse(sessionStorage.getItem("cart"));
        if (cart === null) {

            cart = {
                table:number,
                products: []
            }
        };

        sessionStorage.setItem("cart", JSON.stringify(cart));
    }


    return {
        displayCart: displayCart,
        removeItemFromCart: removeItemFromCart,
        update: update,
        addItemToCart: addItemToCart,
        sendOrder: sendOrder,
        displayOrderTable: displayOrderTable,
        addTable:addTable
    };
})();


















