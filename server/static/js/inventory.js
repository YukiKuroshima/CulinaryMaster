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

// $("#inventory .fa-plus").click(function(){
// 	$("#inventory input[type='text']").fadeToggle();
// });