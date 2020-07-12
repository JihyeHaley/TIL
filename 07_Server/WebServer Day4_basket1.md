#### Productlogajax

~~~html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
	* {
		text-align:center;
	}
	body{
		background-color: black;
	}
	
	h1{
		color : white;
		text-shadow: 3px 3px 8px #ffe500;
	}

	img{
		border:solid 1px white;
		border-radius: 10px;
		box-shadow: 1px 1px 20px 2px #8e8d86;
		margin :10px;
	}
	img:hover{
		transition-duration: 1s; 
  		transform: scale(1.5); 
	}
</style>
<script>
	var xhr, h1;

	window.onload = function(){
		xhr = new XMLHttpRequest();
		xhr.onload = function(e){
			if(e.target.status != 200) return;

			var jsObj = JSON.parse(e.target.responseText);
			h1.innerHTML = "선택된 상품 : " + jsObj['pid'];
		}
		h1 = document.getElementById('selected');
		var imgs = document.getElementsByTagName("img");
		for(var i in imgs){
			imgs[i].onclick = function(e){
				xhr.open('GET',"/sedu/basket1?pid="+e.target.id, true);
				xhr.send();
			};
		}
	}
</script>
<title>Insert title here</title>
</head>
<body>
<h1>STORE SHOP</h1>
<hr>
<figure>
<img src="/sedu/images/1.jpg" width = 200 height = 200 id="p001">
<img src="/sedu/images/2.jpg" width = 200 height = 200 id="p002">
<img src="/sedu/images/3.jpg" width = 200 height = 200 id="p003">
<img src="/sedu/images/4.jpg" width = 200 height = 200 id="p004">
<img src="/sedu/images/5.jpg" width = 200 height = 200 id="p005"><br/>
<img src="/sedu/images/6.jpg" width = 200 height = 200 id="p006">
<img src="/sedu/images/7.jpg" width = 200 height = 200 id="p007">
<img src="/sedu/images/8.jpg" width = 200 height = 200 id="p008">
<img src="/sedu/images/9.jpg" width = 200 height = 200 id="p009">
<img src="/sedu/images/10.jpg" width = 200 height = 200 id="p010"><br/>

</figure>
<h1 id='selected'></h1>
</body>
~~~



#### BasketServlet1

~~~java
package core;

import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.FileWriter;
import java.time.LocalDateTime;
import java.time.temporal.ChronoField;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


/**
 * Servlet implementation class BasketServlet1
 */
@WebServlet("/basket1")
public class BasketServlet1 extends HttpServlet {
	private static final long serialVersionUID = 1L;
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		String contentType = "text/html; charset=UTF-8";
		response.setContentType("text/html; charset=UTF-8");
		PrintWriter out = response.getWriter();
		response.setContentType(contentType);
		String pid = request.getParameter("pid");
		String dirName = "c://logtest";
		File file = new File(dirName);
		
		
		if (!file.exists()) {	
			if (file.mkdirs()) { 
				System.out.println(dirName + "completed");				
			} else {
				System.out.println(dirName + "failed");
			}
		}

		LocalDateTime now = LocalDateTime.now();
		int p1 = now.get(ChronoField.YEAR);
		int p2 = now.get(ChronoField.MONTH_OF_YEAR);
		int p3 = now.get(ChronoField.DAY_OF_MONTH);
		int p4 = now.get(ChronoField.HOUR_OF_DAY);
		int p5 = now.get(ChronoField.MINUTE_OF_HOUR);
			
		dirName="c:\\logtest\\mylog.txt";
		FileWriter writer = new FileWriter(dirName,true);
		//out.print("<h2>"+"" +p1+p2+p3+p4+p5+"  pid:  "+pid+"</h2>");
		writer.write("" +p1+p2+p3+p4+p5+"  pid:  "+pid+"\r\n");
		writer.close();
	
		out.print(String.format("{\"pid\":\"%s\"}", pid));
		out.close();
	    
}
}

~~~

