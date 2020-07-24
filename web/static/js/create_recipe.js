function create_recipe(){
    console.log("created recipe")
    var name = $('#name').val()
    var url = $('#image').val()
    var ing = $('#Ingredients').tagsinput('items')
    var inst = $('#Instructions').tagsinput('items')
    

    var tag = $('input');
    
    tag.tagsinput({
        itemDescription: "description",
        itemIngredients: "Ingredients",
        itemInstructions : "Instructions"
    });

    tag.tagsinput('add', { "description": name , "Ingredients": ing   , "Instructions": inst});
    console.log(tag)

    var credential = {
        "title": name,
        "markdown": url,
        "tags":tag
    };

}

function edit_area() {
	var simplemde = new SimpleMDE({ element: $("#markdown")[0] });
}
