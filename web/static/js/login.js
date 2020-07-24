
function login(){
	console.log("LOGIN USER");
	var username = $('#username').val();
	var password = $('#password').val();
	
	var credentials = {'username': username, 'password': password};
	$.post({
		url: '/authenticate',
		type: 'post',
		dataType: 'json',
		contentType: 'application/json',
		success: function(data){
			window.location.href = "./search_by_id.html";
			console.log("Authenticaded!");
			alert("Authenticaded!!!");
		},
		data: JSON.stringify(credentials)
	});
}
