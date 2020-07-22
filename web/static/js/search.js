function search() {
	var query = $("#search").val()

	$.get({
		url: '/recipes',
		type: 'get',
		dataType: 'json',
		contentType: 'application/json',
		success: function(data)
		{
			console.log(data)
		},
		error: function(data)
		{
			console.error("Error")
		}
	});
}
