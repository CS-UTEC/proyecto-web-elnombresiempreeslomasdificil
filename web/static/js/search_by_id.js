
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

function search_id(id) {
	var query = $("#search").val()

	$.get({
		url: '/recipes2/' + id,
		type: 'get',
		dataType: 'json',
		contentType: 'application/json',
		success: function(data)
		{
			$("#recipe_user").empty()
			var options = {
				includeScore: true,
				keys : ['tags']
			}

			var fuse = new Fuse(data, options)

			var results = fuse.search(query)

			for(i in results){
				var item = results[i].item

				var title = item.title
				var id = item.id

				console.log(title)
				console.log(id)

				$("#recipes").append(makeLink(title, id), "<br>")
			}
		},
		error: function(data)
		{
			console.error("Error")
		}
	});
}
