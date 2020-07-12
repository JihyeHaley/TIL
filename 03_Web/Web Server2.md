# Web Servlet Day 2

##### queryTest.html

~~~html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	    <form method="GET" 
	    action="http://localhost:8000/sedu/querytest">
		이름 : <input name="stname" value="듀크" required><br>
		암호 : <input type="password" name="pwd"><br>
		나이 : <input type="number" name="age"><br>
		성별 : <input type="radio" name="gender" value="남자">남자
		<input type="radio" name="gender" value="여자">여자
		<br>
		
		취미 : 
		피아노 <input type="checkbox" name="hobby" value="피아노">
		수영 <input type="checkbox" name="hobby" value="수영">
		독서 <input type="checkbox" name="hobby" value="독서">
		게임 <input type="checkbox" name="hobby" value="게임">
		<br>
	
		좋아하는 색 : 
		<select name="color">
		    <option value=""></option>
			<option value="빨강색">RED</option>
			<option value="파랑색">BLUE</option>
			<option value="노랑색">YELLOW</option>
		</select>
		<br>
		
		좋아하는 음식 :
		<br> 
		<select name="food" size="4" multiple>
			<option value="라면">라면</option>
			<option value="냉면">냉면</option>
			<option value="짜장면">짜장면</option>
			<option value="햄버거">햄버거</option>
			<option value="닭강정">닭강정</option>
			<option value="육회">육회</option>
		</select>
		<br>
		
		의견 : 
		<br>
		<textarea name="op" rows="10" cols="50"></textarea><br>
		
		<input type="hidden" name="h_1" value="-ㅅ-">
		<input type="hidden" name="h_2" value="=ㅅ="> 
		
		<input type="submit" value="보내기">
		<input type="reset" value="다시작성하기">
	</form>
</body>
</html>
~~~



##### QueryTestServlet.java

~~~java
package core;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/querytest")
public class QueryTestServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		String name = request.getParameter("stname");
		String pwd = request.getParameter("pwd");
		int age = Integer.parseInt(request.getParameter("age"));
		
		String gender = request.getParameter("gender");
		
		String[] hobby = request.getParameterValues("hobby");
		String[] food = request.getParameterValues("food");
		
		String color = request.getParameter("color");
		String op = request.getParameter("op");
		
		response.setContentType("text/html; charset=utf-8");
		PrintWriter out = response.getWriter();
		
		out.print("<h2> 전달된 내용 </h2>"); out.print("<hr>");
		
		
		out.print("<ul>");
		out.print("<li> 이름 : " +name+ "</li>");
		out.print("<li> 암호 : " +pwd+ "</li>");
		out.print("<li> 나이 : " +age+ "</li>");
		
		out.print("<li> 성별 : ");
			if (gender == null) {
				out.print("선택 제대로 하세요 -ㅅ-");	
			}
			else {
				out.print(gender);
			}
		out.print("</li>");
		
		out.print("<li> 취미 : ");
			if (hobby == null) {
				out.print("선택 제대로 하세요 -ㅅ-");	
			}
			else {
				for (int i=0 ; i<hobby.length ; ++i) {
					if (i == hobby.length -1) {
						out.print(hobby[i]);
						break;
					}
					out.print(hobby[i] +",");
				}
			}
		out.print("</li>");
		
		out.print("<li> 좋아하는 색 :" +(color == ""?"없음":color) +"</li>");
		out.print("<li> 좋아하는 음식 : ");
		if (food == null) {
			out.print("선택 제대로 하세요 -ㅅ-");	
		}
		else {
			for (int i = 0; i < food.length; ++i) {
				if (i == food.length - 1) {
					out.print(food[i]);
					break;
				}
				out.print(food[i] +",");
			}
		}
		out.print("</li>");
		
		
		out.print("<li> 의견 : " + op + "</li>");
		out.print("<li> 비밀1 : " + request.getParameter("h_1") + "</li>");
		out.print("<li> 비밀2 : " + request.getParameter("h_2") + "</li>");
		
		
		out.print("</ul>"); out.print("<hr>");
		out.print("<a href='http://70.12.113.164:8000/sedu/queryForm.html'>"
				+ "입력화면으로</a>");
		
		out.close();
	}

}

~~~



name =duke&passwd=1234&age=&gender=female

​	request.getParameter("name") --> "duke"

​	request.getParameter("passwd") --> "1234"

​	request.getParameter("age") --> ""

​	request.getParameter("hobby") --> "null"







# HTTP 상태 500 – 내부 서버 오류

**null을 가지고 숫자열로 변환을 하려 하는데 변환이 안되서 NumberFormatException 에러가 난다**









~~~html
dsdf

<html> 
<head> 
<title>
Creating Object JSON with JavaScript</title>
<script language="javascript">    
var JSONObj = { "name" : "tutorialspoint.com", "year" : 2005 }; 
document.write("<h1>JSON with JavaScript example</h1>"); 
document.write("<br>"); 
document.write("<h3>Website Name=" + JSONObj.name + "</h3>");
document.write("<h3>Year=" + JSONObj.year + "</h3>"); 
</script> 
</head> 
<body>
</body> 
</html>

~~~

