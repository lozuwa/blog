$(document).ready(function(){
	function workstation_click(){
		alert("workstation clicked")
	}
	$("#workstation-ai").click(function(){
	    $.post("12/15/2017",
	    {
	        post: "posts"
	    },
	    function(data, status){
	        console.log("Data: " + data + "\nStatus: " + status);
	    });
	});
});