function create_user(){
	console.log("created user")
	var user = $('#username').val();
	var pass = $('#password').val();


	var credentials = {
		'username': user,
		'password': pass
	};

	var json = JSON.stringify(credentials)

	$.post({
		url: '/users',
		type: 'post',
		dataType: 'json',
		contentType: 'application/json',
		data: json,
		success: function(data)
		{
			console.log(data.msg)
		},
		error: function(data)
		{
			console.error("Error")
		}
	});
}
