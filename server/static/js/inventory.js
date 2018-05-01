//click on X to delete todos
$("#inventory ul").on("click", "span", function(event){
  $(this).parent().fadeOut(function(){
    $(this).remove();
  });
  event.stopPropagation();
 });

$("#inventory input[type='text']").keypress(function(event){
  if(event.which === 13){
    var item = $(this).val();
    $(this).val("");
    $("#inventory ul").append("<li><span><i class='fa fa-trash'></i></span> " + item + "</li>");
  }
 });


function ajaxAddIngridient(item) {
  $.post(
    "/ingridient",
    { item: item },
  ) .done(function() {
  }) .fail(function() {
    alert( "Something went wrong" );
  })
}

function ajaxDeleteIngridient(item) {

  $.ajax({
    url: '/ingridient',
    data: { item: item },
    type: 'DELETE',
    success: function(response) {
      console.log(response);
    },
    error: function(error) {
      console.log(error);
    }
  });
}
