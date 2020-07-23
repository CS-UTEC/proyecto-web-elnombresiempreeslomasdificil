function create_user(){
	console.log("created user")
	var user = $('username').val();
	var pass = $('password').val();


	$.post("/users" + {
		username: user,
		password: pass,
	},
	function(data, status){
		    alert("Data: " + data + "\nStatus: " + status);
	});
}
