$(document).ready(function() {

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

	$("#makeOrder").click(function () {

		cart = sessionStorage.getItem("cart");
		
		var table_num=parseInt($("#tableNumber").val());
		var table_num_span = parseInt($("#tableNumber").text());
		if (isNaN(table_num) && isNaN(table_num_span)){
			alert("You have to choice table!")
			return false;
		}
		$.ajax({
			type:"POST",
			url:"/order/makecurrentorder/",
			data: {
				'cart': cart,
				'table': table_num
			},
			success: function(result){
				if(result.success){
					sessionStorage.clear();
					window.location = 'finalize';
				}
			},
			headers: {
				'X-CSRFToken': csrftoken
			}
		})
	});


});