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

			console.log(fuse.search(query))
		},
		error: function(data)
		{
			console.error("Error")
		}
	});
}
