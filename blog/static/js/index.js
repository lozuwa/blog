$("lessons-learned-from-making-a-dataset-from-scratch").click(function(){
    $.post("3/20/2018/?id=1",
    {
        post: "posts"
    },
    function(data, status){
        console.log("Data: " + data + "\nStatus: " + status);
    });
});