function create_recipe(){
    console.log("created user")
	var user = $('#username').val();
	var pass = $('#password').val();


	var credentials = {
		'username': user,
		'password': pass
	};

	var json = JSON.stringify(credentials)

}