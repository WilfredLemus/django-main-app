$(document).ready(function(){

  $(".btn-done").on("click", function(){
    $(this).closest("tr").removeClass("danger").addClass("success");
    $(this).children("span").removeClass("glyphicon glyphicon-remove").addClass("glyphicon glyphicon-ok");

    var orderId = $(this).closest("tr").find(".ord_id").html();
    $.ajax({
	type: "GET",
  	url: "/change_state/",
  	data: {
    	order_id: orderId
  	},
  	success: function( ) {
    	console.log("dada")
  	}
	});
})

  $(".btn-done3").on("click", function(){
    $(this).closest("tr").removeClass("danger").addClass("success");
    $(this).children("span").removeClass("glyphicon glyphicon-remove").addClass("glyphicon glyphicon-ok");

    var orderId = $(this).closest("tr").find(".ord_id").html();

    $.ajax({
    type: "GET",
    url: "/change_state_calls/",
    data: {
        table_id: orderId
    },
    success: function( ) {
        console.log("dada")
    }
    });
})



$(".btn-done2").on("click", function(){
  $(this).closest("tr").removeClass("danger").addClass("success");
  $(this).children("span").removeClass("glyphicon glyphicon-remove").addClass("glyphicon glyphicon-ok");

  var orderId = $(this).closest("tr").find(".ord_id").html();

  $.ajax({
type: "GET",
  url: "/change_state_accepted/",
  data: {
    order_id: orderId
  },
  success: function( ) {
    console.log("dada")
  }
});
})

});

var limit="0:10"

if (document.images){
var parselimit=limit.split(":")
parselimit=parselimit[0]*60+parselimit[1]*1
}
function beginrefresh(){
if (!document.images)
return
if (parselimit==1)
window.location.reload()
else{
parselimit-=1
curmin=Math.floor(parselimit/60)
cursec=parselimit%60
if (curmin!=0)
curtime=curmin+" minutes and "+cursec+" seconds left until page refresh!"
else
curtime=cursec+" seconds left until page refresh!"
window.status=curtime
setTimeout("beginrefresh()",1000)
}
}

window.onload=beginrefresh
