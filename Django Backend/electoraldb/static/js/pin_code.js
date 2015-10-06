// AJAX for posting
function get_towns(pin,callback) {
	// console.log("create post is working!") // sanity check
	// alert($("input[name='csrfmiddlewaretoken']").val());
	
	$.post("/electoraldb/town_from_pin/",{pincode:pin},function (json){
		//alert(json); // log the returned json to the console
		callback(json)
	});
};