#### Productlog

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

<body>
<form method="GET" action="http://localhost:8000/sedu/basket">
   <h2 style="text-align:center">원하는 상품을 클릭해 주세요!! 마구마구^^</h2>
   <hr>
   <section>
      <a href="/sedu/basket?pid=p001"><img src="/sedu/images/1.jpg"></a>
      <a href="/sedu/basket?pid=p002"><img src="/sedu/images/2.jpg"></a>
      <a href="/sedu/basket?pid=p003"><img src="/sedu/images/3.jpg"></a>
      <a href="/sedu/basket?pid=p004"><img src="/sedu/images/4.jpg"></a>
      <a href="/sedu/basket?pid=p005"><img src="/sedu/images/5.jpg"></a><br>
      <a href="/sedu/basket?pid=p006"><img src="/sedu/images/6.jpg"></a>
      <a href="/sedu/basket?pid=p007"><img src="/sedu/images/7.jpg"></a>
      <a href="/sedu/basket?pid=p008"><img src="/sedu/images/8.jpg"></a>
      <a href="/sedu/basket?pid=p009"><img src="/sedu/images/9.jpg"></a>
      <a href="/sedu/basket?pid=p010"><img src="/sedu/images/10.jpg"></a>
   </section>
</form>
</body>
</html>
~~~



#### BasketServlet

~~~java
package core;
import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class BasketServlet
 */
@WebServlet("/basket")
public class BasketServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		response.setContentType("Text/html; character=utf-8");
		PrintWriter out=response.getWriter();
		String pid = request.getParameter("pid");
	    int pnum = Integer.parseInt(pid.replaceAll("[^0-9]", ""));
	    out.print("<h2>id : "+pid+"</h2><br>");
	    out.print("<img src='/sedu/images/"+pnum+".jpg' style = 'width : 50%;'>");
	    out.print("<a href='/sedu/productlog.html'>back to product homepage</a>");
	    out.close();
		
	}

}

~~~

