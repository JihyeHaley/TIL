~~~html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<link href="dragdrop.css">
<style>
	*{
		font-family: "jua";
	}
	
	@font-face {
	    src: url("../jsexam/BMJUA_ttf.ttf");
	    font-family: "jua";
	}
	h1{
		text-align : center;
		color : #006699;
		margin : 20px 20px;
		padding : 20px;
		/* font-family: "jua"; */
		font-size : 3em;
		/*text-shadow : 2px 2px 5px #0099cc, 2px 2px 5px #0099ff;*/
		background-image : url("/edu/jsexam/projectimage/disney.png");
		background-repeat : no-repeat;
		background-position : center left;
		background-size : 110px;
	}
	button{
		width : 120px;
		height : 45px;
		border-radius : 10px;
		color : white;
		background-color : #006699;
		margin : 0px 8px;
		font-size : 1.2em;
		/* font-weight : bold; */
	}
	button:hover{
		color : #0099ff;
		box-shadow : 2px 2px 5px #0099ff;
	}
	div{
		text-align : center;
		margin : 0px 20px;
	}
	fieldset{
		font-size : 1.4em;
		border : 2 dashed #006699;
		border-radius : 10px;
		max-width : 500px;
		margin : 0 auto;
	}
	nav{
		float: lsft;
	}
	
	section{
		float: right;
		color : #006699;
		margin : 0px 20px;
	}

	span{
		margin : 0px 10px;
	}
	
	#dropbox{
		float: left;
		width: 550px;
		height : 950px;
		margin: 20px 21px;
		border: 2px solid #999999;
		border-radius: 10px;
	}
	#picturesbox{
		float: left;
		width: 550px;
		height : 950px;
		margin: 20px 21px;
		border: 2px solid #999999;
		border-radius: 10px;
		padding: 5px 5px;
	}
	img{
		img-align : center;
		margin: 4px auto;
		
	}

</style>
</head>

<body>

<header>
	<h1>HTML5로 스티치 카드 만들기</h1>
</header>

<div>
	<button id="stSave" onclick="save();">Save</button>
	<button id="stRead" onclick="restore();">Read</button>
	<button id="stRemove" onclick="remove();">Clear</button>
	<br>

	<fieldset style="width:200">
	
		<legend> 만들어 볼까요? </legend>
			<span>
				<label for=background_color>배경</label>
				<input id=background_color name=background_color type=color>
			</span>
			<span>
				<label for=border_color>테두리</label>
				<input id=border_color name=border_color type=color>
			</span>
			<span>
				<label for=text_color>메시지</label>
				<input id=text_color name=text_color type=color>
			</span>
			<br>
			<label for=inputtext style="font-size:1.3em">입력 메시지</label><br>
   			<input id=inputtext name=inputtext type=text style="width:500px;">
	</fieldset>
</div>

<section id="dropbox">
	<canvas id="myCanvas" width="550" height="600"></canvas>
</section>

<section>
	<article id="picturesbox">
		<img id="image1" src="/edu/jsexam/projectimage/name1.png" style=" width:130px">
  	 	<img id="image2" src="/edu/jsexam/projectimage/name2.png" style=" width:130px">
    	<img id="image3" src="/edu/jsexam/projectimage/name3.png" style=" width:130px">
    	<img id="image4" src="/edu/jsexam/projectimage/name4.png" style=" width:130px">
    	<img id="image5" src="/edu/jsexam/projectimage/name5.png" style="width:130px">
  	 	<img id="image6" src="/edu/jsexam/projectimage/name6.png" style="width:130px">
    	<img id="image7" src="/edu/jsexam/projectimage/name7.png" style="width:130px">
    	<img id="image8" src="/edu/jsexam/projectimage/name8.png" style="width:130px">
    	<img id="image9" src="/edu/jsexam/projectimage/name9.png" style="width:130px">
  	 	<img id="image10" src="/edu/jsexam/projectimage/name10.png" style="width:130px">
    	<img id="image11" src="/edu/jsexam/projectimage/name11.png" style="width:130px">
    	<img id="image12" src="/edu/jsexam/projectimage/name12.png" style="width:130px">
    	<img id="image13" src="/edu/jsexam/projectimage/name13.png" style="width:130px">
  	 	<img id="image14" src="/edu/jsexam/projectimage/name14.png" style="width:130px">
    	<img id="image15" src="/edu/jsexam/projectimage/name15.png" style="width:130px">
    	<img id="image16" src="/edu/jsexam/projectimage/name16.png" style="width:130px">
    	<img id="image17" src="/edu/jsexam/projectimage/name17.png" style="width:130px">
  	 	<img id="image18" src="/edu/jsexam/projectimage/name18.png" style="width:130px">
    	<img id="image19" src="/edu/jsexam/projectimage/name19.png" style="width:130px">
    	<img id="image20" src="/edu/jsexam/projectimage/name20.png" style="width:130px">
    	<img id="image21" src="/edu/jsexam/projectimage/name21.png" style="width:130px">
  	 	<img id="image22" src="/edu/jsexam/projectimage/name22.png" style="width:130px">
    	<img id="image23" src="/edu/jsexam/projectimage/name23.png" style="width:130px">
    	<img id="image24" src="/edu/jsexsam/projectimage/name24.png" style="width:130px"> 
	</article>
</section>

<script>
var area;
var ctx;
	function initialize(){
		area = document.getElementById("myCanvas");
		ctx = area.getContext("2d");
		ctx.clearRect(0,0,400,500);
		ctx.beginPath();
		ctx.rect(0,0,400,500);s
		ctx.fillStyle = "white";
		ctx.fill();
	    ctx.stroke();
	}
	function remove() {
		ctx.clearRect(0,0,670,370); // 픽셀 정리

	}
	function save() {	
	    alert(canvas.toDataURL()); 
	    localStorage.setItem("canvas", canvas.toDataURL());    
	}
	function restore(){
		var img = new Image();
	    img.src = localStorage.getItem("canvas");
	    img.onload = function() { 
	    	ctx.drawImage(img, 0, 0);        
	    }
	}
	
	document.body.onload = initialize;
</script>

<script>
	var source, drop;
	 function initiate(){
	  source=document.getElementById('image');
	  source.addEventListener('dragstart', dragged, false);
	
	  drop=document.getElementById('dropbox');
	  drop.addEventListener('dragover', function(e){console.log("dragover"); e.preventDefault(); }, false);
	  drop.addEventListener('drop', dropped, false);
	} 
	function dragged(e){
		console.log("dragstart");
	  var code='<img src="'+source.getAttribute('src')+'">';
	  e.dataTransfer.setData('Text', code);
	}
	function dropped(e){
		console.log("drop");
	  e.preventDefault();
	  drop.innerHTML+=e.dataTransfer.getData('Text');
	}
	window.addEventListener('load', initiate);
</script>
</body>

</html>
~~~

