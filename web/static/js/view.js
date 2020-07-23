function qStr(){
	var params = urlParams = new URLSearchParams(window.location.search)
	console.log(params.get('id'))

	$.get({
		url: '/recipes2/' + params.get('id'),
		type: 'get',
		dataType: 'json',
		contentType: 'application/json',
		success: function(data)
		{
			$("#view").append(data.markdown_html)
			$("#tags").val(data.tags.join())
		},
		error: function(data)
		{
			console.error("Error")
		}
	});
}
