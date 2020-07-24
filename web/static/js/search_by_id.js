
function get_current(){
	console.log("Voy a traer al ususario");
	$.getJSON("/current", function(data){
		console.log(data['username'])
		var div = "<div>@<span>username</span></div>";
		div = div.replace("username" , data['username']);
		$('#contact').append(div);
		get_users(data['id']);
    });
}
