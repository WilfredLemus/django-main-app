$(document).ready(function(){

  $(".btn-done").on("click", function(){
    $(this).closest("tr").removeClass("danger").addClass("success");
    $(this).children("span").removeClass("glyphicon glyphicon-remove").addClass("glyphicon glyphicon-ok");
  })

})


