function makeLink(title, id) {
	// Link placeholder
	return $("<a>", {href: "/recipe_view.html?id="+id, text: title})
}

function search() {
	var query = $("#search").val()

	$.get({
		url: '/recipes2',
		type: 'get',
		dataType: 'json',
		contentType: 'application/json',
		success: function(data)
		{
			$("#recipes").empty()
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


function all_recipes() {

	$.get({
		url: '/recipes2',
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

				$("#recipes").append(makeLink(title, id), "<br>")
			}
		},
		error: function(data)
		{
			console.error("Error")
		}
	});
}