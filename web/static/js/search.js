function search() {
	var query = $("#search").val()

	$.get({
		url: '/recipes',
		type: 'get',
		dataType: 'json',
		contentType: 'application/json',
		success: function(data)
		{
			var options = {
				includeScore: true,
				keys : ['title']
			}

			var fuse = new Fuse(data, options)

			var results = fuse.search(query)

			for(i in results){
				console.log(results[i].item.title)
				console.log(results[i].item.id)
			}
		},
		error: function(data)
		{
			console.error("Error")
		}
	});
}
