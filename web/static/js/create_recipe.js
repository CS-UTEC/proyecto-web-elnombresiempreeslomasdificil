function create_recipe(){
    console.log("created recipe")
    var user = $('#Ingredients').tagsinput()

    console.log(user)

}

function edit_area() {
	var simplemde = new SimpleMDE({ element: $("#markdown")[0] });
}
