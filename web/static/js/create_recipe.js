function create_recipe(){
    console.log("created recipe")
    var name = $('#name').val()
    var url = $('#image').val()
    var ing = $('#Ingredients').tagsinput('items')
    var inst = $('#Instructions').tagsinput('items')

    
    var tag = $('input');
        elt.tagsinput({

        insgredientes: {
            source: ing
        },
        instrucciones: {
            source: inst
        }
    });


	var credentials = {
		'user_id': 1,
		'title': name,
		'markdown': pass,
		'tags': pass,
    };




}

function edit_area() {
	var simplemde = new SimpleMDE({ element: $("#markdown")[0] });
}
