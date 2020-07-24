function logout(){
	$.get({
		url: '/f/logout',
		type: 'get',
		dataType: 'json',
		contentType: 'application/json',
		success: function(data){
			window.location.href = "/index.html";
			console.log(data);
		},
		error: function(data){
			console.error("Error");
		}
	});
}
