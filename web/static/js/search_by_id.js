


function search_id(id) {

	$.get({
		url: '/recipes2?user=' + id,
		type: 'get',
		dataType: 'json',
		contentType: 'application/json',
		success: function(data)
		{

			console.log(data)

			for(i in  data){
				var title = data[i].title
				var id = data[i].id

				console.log(title)
				console.log(id)

				$("#recipe_user").append(makeLink(title, id), "<br>")
			}
		},
		error: function(data)
		{
			console.error("Error")
		}
	});
}



function get_current(){
	console.log("Voy a traer al ususario");
	$.getJSON("/current", function(data){
		console.log(data['id'])
		//var div = "<div>@<span>username</span></div>";
	    //div = div.replace("username" , data['username']);
		search_id(data['id']);
    });
}


function makeLink(title, id) {
	// Link placeholder
	return $("<a>", {href: "/recipe_view.html?id="+id, text: title})
}
