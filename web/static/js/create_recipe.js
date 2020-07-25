var simplemde

function create_recipe(){
    console.log("created recipe")
    var name = $('#name').val()

    var tag = $('#tags').tagsinput('items');

    console.log(tag)

    var data = {
        "title": name,
        "markdown": simplemde.value(),
        "tags":tag
    };

    console.log(data)

	$.post({
		url: '/recipes2',
		type: 'post',
		dataType: 'json',
		contentType: 'application/json',
		data: JSON.stringify(data),
		success: function(data)
		{
			console.log(data.msg)
			window.location.href = "./search_by_id.html";
			
		},
		error: function(data)
		{
			console.error("Error")
		}
	});
}

function edit_area() {
	simplemde = new SimpleMDE({ element: $("#markdown")[0] });
	simplemde.value("# Título\n## Ingredientes\n* \n* \n## Instrucciones")
}
