#### productlogsession

~~~html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style>
	img{
		width : 160px;
		height : 160px;
		border : 1px ;
		border-radius : 10px;
		border : 1px solid #cc33ff;
		box-shadow: 5px 5px 5px #cc33ff;
		margin : 5px 5px;
		margin-top: 10px;
	}
	img:hover{
		transform : rotate(10deg); /*3도 만큼 회전시켜라*/
		transition : transform 1s; /*transform을 2초동안 움직여라*/
	}

	section{
		text-align : center;
	}
</style>
</head>
<script>
	var xhr, h1;

	window.onload = function(){
		xhr = new XMLHttpRequest();
		xhr.onload = function(e){
			if(e.target.status != 200) return;

			var jsObj = JSON.parse(e.target.responseText);
			h1.innerHTML = "선택된 상품";
			ul.innerHTML = "선택된 상품 : " + jsObj['pid']+Object.keys[jsObj].length+" 개 ";
		}
		h1 = document.getElementById('selected');
		var imgs = document.getElementsByTagName("img");
		for(var i in imgs){
			imgs[i].onclick = function(e){
				xhr.open('GET',"/sedu/basket1?pid="+e.target.id, true);
				xhr.send();
			};
		}
		ul=document.getElementById('number');
	}
</script>
<body>
<form method="GET" action="http://localhost:8000/sedu/basket1">
	<h2 style="text-align:center">Hollister, Choose your best</h2>
	<hr>
	<section>
		<img src="/sedu/images/1.jpg" id="p001">
		<img src="/sedu/images/2.jpg" id="p002">
		<img src="/sedu/images/3.jpg" id="p003">
		<img src="/sedu/images/4.jpg" id="p004">
		<img src="/sedu/images/5.jpg" id="p005"><br>
		<img src="/sedu/images/6.jpg" id="p006">
		<img src="/sedu/images/7.jpg" id="p007">
		<img src="/sedu/images/8.jpg" id="p008">
		<img src="/sedu/images/9.jpg" id="p009">
		<img src="/sedu/images/10.jpg" id="p010">
	</section>
	
	<section>
		<h1 id="selected"></h1>
		<ul id="number"></ul>
	</section>
</form>
</body>
</html>

~~~



#### BasketServlet2

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
@WebServlet("/basket2")
public class BasketServlet2 extends HttpServlet {
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
	
		out.print(String.format("{\"pid\":\"%s\"}", pid.length()));
		out.close();
	    //int pnum = Integer.parseInt(pid.replaceAll("[^0-9]", ""));
	    // out.print("<h2>id : "+pid+"</h2><br>");
	    // out.print("<img src='/sedu/images/"+pnum+".jpg' style = 'width : 50%;'>");
		//String fileName=request.getParameter("fileName");
		//ServletContext context = getServletContext();
		//String uploadFilePath = context.getRealPath("fieldfolder");
		//String filePath = uploadFilePath + File.separator + fileName;	
		//FileInputStream fileInputStream = new FileInputStream(filePath);
		//String mimeType = getServletContext().getMimeType(filePath);
		//	mimeType = "application/octest-stream";
		//}
		//response.setContentType(mimeType);
		//ServletOutputStream servletOutStream= response.getOutputStream();
	//servletOutStream.flush();
	//servletOutStream.close();
	//fileInputStream.close();	
}
}

~~~

