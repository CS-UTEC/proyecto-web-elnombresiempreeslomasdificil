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
			$("#view").append(data.markdown)
		},
		error: function(data)
		{
			console.error("Error")
		}
	});
}
