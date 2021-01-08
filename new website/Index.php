<html>
<head>
	<title>Rasperry Pi Rover</title>
 <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
<style>
body{
 background:#174c4c;
}

.slidecontainer {
  width: 50%; /* Width of the outside container */
}

/* The slider itself */
.slider {
  -webkit-appearance: none;  /* Override default CSS styles */
  appearance: none;
  width: 100%; /* Full-width */
  height: 25px; /* Specified height */
  background: rgb(0,0,0); /* Grey background */
  outline: none; /* Remove outline */
  opacity: 0.7; /* Set transparency (for mouse-over effects on hover) */
  -webkit-transition: .2s; /* 0.2 seconds transition on hover */
  transition: opacity .2s;
}

/* Mouse-over effects */
.slider:hover {
  opacity: 1; /* Fully shown on mouse-over */
}

/* The slider handle (use -webkit- (Chrome, Opera, Safari, Edge) and -moz- (Firefox) to override default look) */
.slider::-webkit-slider-thumb {
  -webkit-appearance: none; /* Override default look */
  appearance: none;
  width: 25px; /* Set a specific slider handle width */
  height: 25px; /* Slider handle height */
  background: rgb(0,255,0); /* Green background */
  cursor: pointer; /* Cursor on hover */
}

.slider::-moz-range-thumb {
  width: 25px; /* Set a specific slider handle width */
  height: 25px; /* Slider handle height */
  background: rgb(0,255,0); /* Green background */
  cursor: pointer; /* Cursor on hover */
}

</style>
</head>
<body class = "keyable">

<center><img src = "http://192.168.1.128:8000/" id="camfeed" class = "keyable" alt="Camera feed from robot"></center>
<center> <div class="slidecontainer">
 <input type="range" min="0" max="700" value="0" class="slider" id="tSlide">
	<center id = "tout">Throttle: 0</center>
</div>
</center>
<center><div id="instructions">
  Throttle:q,e
  Steering: a,d
  Turntable: z,c
  Drive: w,s
  Move camera: mouseover the camfeed
  Pneumatic arm joint 1: u,j
  Pneumatic arm joint 2: i,k
  Pneumatic arm hand: o,p
  </div></center>


 <script>
	valx = 90;
	valy = 90;
	valth = 0;    
	valgo = 0;
	valturn = 0;    
  valtable = 0;
   valj1 = 0;
   valj2 = 0;
   valj3 = 0;
        $("#camfeed").on("mousemove", function(event) {
	valx = event.offsetX;
	valy = event.offsetY;
	valx = Math.round((valx/640)*180);
	valy = Math.round((valy/480)*180);


        var xmlhttp = new XMLHttpRequest();	
        xmlhttp.open("GET", "input.php?xc=" + valx + "&&yc="+ valy, true);
        xmlhttp.send(); 
        });


	$("#tSlide").on("input", function() {
	console.log(valth);
	
	  valth = $("#tSlide")[0].value;
	   $("#tout").html("Throttle: " + valth);
	   var xmlhttp = new XMLHttpRequest();	
        xmlhttp.open("GET", "input.php?th=" + valth, true)
        xmlhttp.send(); 
       
        });
	
	$(".keyable").on("keypress", function(key) {
	
	valkey = key.originalEvent.key;


	if(valkey == "a"){

	console.log(valkey);
	valturn = 2;
	var xmlhttp = new XMLHttpRequest();	
         xmlhttp.open("GET", "input.php?tu=" + valturn, true);
        xmlhttp.send(); 

	}else if(valkey == "d"){
	
	valturn = 1;
		console.log(valkey);
	var xmlhttp = new XMLHttpRequest();	
        xmlhttp.open("GET", "input.php?tu=" + valturn, true);
        xmlhttp.send(); 
	}else if(valkey == "w"){
	
	valgo = 2;
	console.log(valkey);
	var xmlhttp = new XMLHttpRequest();	
         xmlhttp.open("GET", "input.php?go=" + valgo, true);
        xmlhttp.send(); 
	}else if(valkey == "s"){

	valgo = 1;
	console.log(valkey);
	var xmlhttp = new XMLHttpRequest();	
       xmlhttp.open("GET", "input.php?go=" + valgo, true);
        xmlhttp.send(); 
	}else if(valkey == "z"){
	
	valtable = 2;
	console.log(valkey);
	var xmlhttp = new XMLHttpRequest();	
         xmlhttp.open("GET", "input.php?tb=" + valtable, true);
        xmlhttp.send(); 
	}else if(valkey == "c"){

	valtable = 1;
	console.log(valkey);
	var xmlhttp = new XMLHttpRequest();	
       xmlhttp.open("GET", "input.php?tb=" + valtable, true);
        xmlhttp.send(); 
	}else if(valkey == "q"){

	valth = parseInt(valth);
	valth-=5;
	if(valth <0){
	valth = 0;
	}
	document.getElementById("tSlide").value = valth.toString();
	$("#tout").html("Throttle: " + valth);
	valth = valth.toString();
	var xmlhttp = new XMLHttpRequest();	
         xmlhttp.open("GET", "input.php?th=" + valth, true);
        xmlhttp.send(); 

	console.log(valth);
	}else if(valkey == "e"){

	valth = parseInt(valth);
	valth+=5;
	if(valth>700){
	valth = 700;
	}
	document.getElementById("tSlide").value = valth.toString();
	$("#tout").html("Throttle: " + valth);
	valth = valth.toString();
	var xmlhttp = new XMLHttpRequest();	
         xmlhttp.open("GET", "input.php?th=" + valth, true);
        xmlhttp.send(); 

		
	console.log(valth);
	}else if(valkey == "u"){
	
	valj1 = 2;
	console.log(valkey);
	var xmlhttp = new XMLHttpRequest();	
         xmlhttp.open("GET", "input.php?j1=" + valj1, true);
        xmlhttp.send(); 
	}else if(valkey == "j"){

	valj1 = 1;
	console.log(valkey);
	var xmlhttp = new XMLHttpRequest();	
       xmlhttp.open("GET", "input.php?j1=" + valj1, true);
        xmlhttp.send(); 
	}else if(valkey == "i"){
	
	valj2 = 2;
	console.log(valkey);
	var xmlhttp = new XMLHttpRequest();	
         xmlhttp.open("GET", "input.php?j2=" + valj2, true);
        xmlhttp.send(); 
	}else if(valkey == "k"){

	valj2 = 1;
	console.log(valkey);
	var xmlhttp = new XMLHttpRequest();	
       xmlhttp.open("GET", "input.php?j2=" + valj2, true);
        xmlhttp.send(); 
	}else if(valkey == "o"){
	
	valj3 = 2;
	console.log(valkey);
	var xmlhttp = new XMLHttpRequest();	
         xmlhttp.open("GET", "input.php?j3=" + valj3, true);
        xmlhttp.send(); 
	}else if(valkey == "p"){

	valj3 = 1;
	console.log(valkey);
	var xmlhttp = new XMLHttpRequest();	
       xmlhttp.open("GET", "input.php?j3=" + valj3, true);
        xmlhttp.send(); 
	}else {
	

	}


	});

	$(".keyable").keyup(function(key) {
	
	valkey = key.originalEvent.key


	if(valkey == "a"){

	console.log(valkey+" up");
	valturn = 0;
	var xmlhttp = new XMLHttpRequest();	
          xmlhttp.open("GET", "input.php?tu=" + valturn, true);
        xmlhttp.send(); 

	}else if(valkey == "d"){
	
	console.log(valkey+" up");
	valturn = 0;
	var xmlhttp = new XMLHttpRequest();	
          xmlhttp.open("GET", "input.php?tu=" + valturn, true);
        xmlhttp.send(); 
	}else if(valkey == "w"){
	
	valgo = 0;
	console.log(valkey+" up");
	var xmlhttp = new XMLHttpRequest();	
         xmlhttp.open("GET", "input.php?go=" + valgo, true);
        xmlhttp.send(); 
	}else if(valkey == "s"){

	valgo = 0;
	console.log(valkey+" up");
	var xmlhttp = new XMLHttpRequest();	
       xmlhttp.open("GET", "input.php?go=" + valgo, true);
        xmlhttp.send(); 
	}
    else if(valkey == "z"){
	
	valtable = 0;
	console.log(valkey+" up");
	var xmlhttp = new XMLHttpRequest();	
         xmlhttp.open("GET", "input.php?tb=" + valtable, true);
        xmlhttp.send(); 
	}else if(valkey == "c"){

	valtable = 0;
	console.log(valkey+" up");
	var xmlhttp = new XMLHttpRequest();	
       xmlhttp.open("GET", "input.php?tb=" + valtable, true);
        xmlhttp.send(); 
	}else if(valkey == "u"){
	
	valj1 = 0;
	console.log(valkey+" up");
	var xmlhttp = new XMLHttpRequest();	
         xmlhttp.open("GET", "input.php?j1=" + valj1, true);
        xmlhttp.send(); 
	}else if(valkey == "j"){

	valj1 = 0;
	console.log(valkey+" up");
	var xmlhttp = new XMLHttpRequest();	
       xmlhttp.open("GET", "input.php?j1=" + valj1, true);
        xmlhttp.send(); 
	}else if(valkey == "i"){
	
	valj2 = 0;
	console.log(valkey+" up");
	var xmlhttp = new XMLHttpRequest();	
         xmlhttp.open("GET", "input.php?j2=" + valj2, true);
        xmlhttp.send(); 
	}else if(valkey == "k"){

	valj2 = 0;
	console.log(valkey+" up");
	var xmlhttp = new XMLHttpRequest();	
       xmlhttp.open("GET", "input.php?j2=" + valj2, true);
        xmlhttp.send(); 
	}else if(valkey == "o"){
	
	valj3 = 0;
	console.log(valkey+" up");
	var xmlhttp = new XMLHttpRequest();	
         xmlhttp.open("GET", "input.php?j1=" + valj3, true);
        xmlhttp.send(); 
	}else if(valkey == "p"){

	valj3 = 0;
	console.log(valkey+" up");
	var xmlhttp = new XMLHttpRequest();	
       xmlhttp.open("GET", "input.php?j1=" + valj3, true);
        xmlhttp.send(); 
	}else if(valkey == "q"){

	

	console.log(valth);
	}else if(valkey == "e"){

	
	console.log(valth);
	}else {
	

	}


	});

    </script>
</body>
</html>
