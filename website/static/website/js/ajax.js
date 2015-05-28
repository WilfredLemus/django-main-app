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
		console.log(cart)
		$.ajax({
			type:"POST",
			url:"/order/makecurrentorder/",
			data: {'cart':cart},
			success: function(result){
				if(result.success){
					sessionStorage.clear();
				}
			},
			headers: {
				'X-CSRFToken': csrftoken
			}
		})
	});


});