$(document).ready(function(){

    // $(".menuItem").on('click', function () {
    //     var down = $(this).css('height') == '220px';
    //     if( down ) {
    //             $(this).animate( {height: '300px'}, 'slow');
    //          }
    //      else {
    //             $(this).animate( {height: '220px'}, 'slow');
    //          }
    // });

    $(".menuItem img").hover(
        function() {
          console.log("dsa")
          $( this ).closest("li").animate({ height: '+=200px' });
          },
        function() {
          console.log("dsa")
          $( this ).closest("li").animate({ height: '-=200px' });
        }
    );

    function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
    var csrftoken = getCookie('csrftoken');


    var cart = JSON.parse(sessionStorage.getItem("cart"));
    if (cart) {
        var table=cart.table;
        console.log(cart.table);
        $("#finalizeTableNumber").html(table);

    };

    $("button#waiter").on('click', function () {
        var cart = JSON.parse(sessionStorage.getItem("cart"));
            if (cart) {
                var table=cart.table;
                $.ajax({
                                type:"POST",
                                url:"/callwaiter/",
                                data: {
                                    'table': table
                                },
                                headers: {
                                    'X-CSRFToken': csrftoken
                                }
                            })
            }

    });

    $("button#btn-add").on('click', function () {

        var real_id = $(this).attr("name");

        var name = $(this).closest("li").find("h2").text();
        var price = $(this).closest("li").find("span").text();
        console.log(price)
        if (name != "" && price != "" && real_id != "") {
            OrderApp.addItemToCart(name, price, real_id);
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
        var totalPrice=parseFloat($("#totalPrice").text());
        for(var item in items){
            totalPrice+=parseFloat(items[item].price);
            console.log(items[item].price);
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
        $("#totalPrice").html(cart.total_price);


        // var container = $("#orderTable");
        // var source = $("#cartTemplate").html();
        // var template = Handlebars.compile(source);
        // var context = {products:cart.products};
        // var html = template(context);
        // container.html(html);
    };
}
