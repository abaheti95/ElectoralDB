// AJAX for posting
function get_voter(v,callback) {	
	$.post("/electoraldb/voter_search/",{voterid:v},function (json){
		j = jQuery.parseJSON(json);
		// alert(json);
		// alert(jQuery.type(j)); // log the returned json to the console
		callback(j[0].fields);
	});
};

function get_voters(pin,t,callback) {
	$.post("/electoraldb/voters_search/",{pincode:pin,town:t},function (json){
		//alert(json); // log the returned json to the console
		
		// console.log(json);
		// alert(json);
		// alert(jQuery.type(json)); // log the returned json to the console
		var j = jQuery.parseJSON(json);
		// alert(j);
		// console.log(j);
		// alert(jQuery.type(j)); // log the returned json to the console
		callback(j);
	});
};