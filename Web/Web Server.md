# Servlet

* Web Client : HTML, CSS3, JavaScript

* Web Server : Servlet, JSP, JDBC, Spring, FW, MyBatis FW, (Junit FW, log4J) - Java



JSP 는 동적처리를 서버엣 한다!!!!

* servlet은 
  * sedu -> Java Resource -> src 에 생성한다.



#### web 만들어보기

* jsphtml사용

  ​	[http://localhost:8000/sedu/first.jsp?gname=%EC%A7%80%ED%98%9C]

  ​    [http://localhost:8000/sedu/first.jsp?gname=지혜]

  ​                               **URL**                             ? **URI**

* server 사용

  ​	[http://localhost:8000/sedu/firstServlet?gname=고길동]



## ＠Servlet 이란..!

* 1998년 가을에 발표된 기술

* CGI(Common Gateway Interface) - 웹의 표준, 구현언어 투명성
  * Fast CGI
  * Servlet
* Server Side Applet(Applet : 웹 브라우저에서 실행되는 Java 프로그램)

#### - 구현상의 특징

1.  HttpServlet을 상속해야한다.

2.  main()구현하지 않는다. (main()메서드를 담고 있는 메인 클래스는 톰캣이 내장)

3. 수행하는 동안 호출되는 메서드가 정해져 있는데
   ***이 때 호출되는 메서드는 init(), service(), destroy(), doGet(), doPost()등이다.***
   이 메서드들을 선태적으로 오버라이딩해서 구현한다.

4. 서블릿에서 수행 결과를 출력할 때 

   * 요청해온 브라우저로의 출력(응답)

     * HttpServletResponse의 getWriter()를 호출해서 클라이언트의 출력 스트림 객체  생성해서

   * 표준 출력: System.out.println();                    //servlet에서는 얘가 extra! ! 

     ​					***톰캣서버에 콘솔창에서***

5. Servlet이 수행하는데 필요한 데이터를 요청 보내오는 클라이언트로 부터 전다받을 수 있다. 이 때 전달받는 데이터를 쿼리 문자열이라고 한다.

   * HttpServletRequest 의 ***getParameter(): String*** 또는 ***getParameterValues():String[]***를 사용한다.

   ​                                                        단수                                                 복수
      추출하고 싶은 argument에 이름을 준다! 



#### - 수행상의 특징

1. 서블릿을 요청할 때는 "/컨텍스트루트명/서블릿의매핑명" 형식의 URI를 사용한다.

2. 서블릿의 요청은 

   * 서블릿을 요청하는 URL 문자열을 브라우저의 주소 필드에 입력해서 직접 요청

     * GET

   * <a> 태그로 요청

     * GET

   * <form>태그를 통해서 요청

     * GET/POST

3. 서블릿 객체는 한 번 생성되는 서버 종료되거나 컨텍스트가 리로드 될때까지 객체 상태를 유지한다.

4. 여러 클라이언트가 동일한 서블릿을 동시 요청하면 하나의 서블릿을 객체를 공유해서 수행한다.

5. 최초 요청시의 수행 흐름

   init(),     service() -> doGet(),    destroy()

   ​							  -> doPost()

Core 패키지 : FlowServlet(/flow)

​						MemberLocalServlet(/memberlocal)

Web Server : Web 통신에서 서버역할을 수행하는 프로그램 (Http Server)

Web Server + Application Server (MAIN CLASS)= Web Application Server = WAS

TOMCAT = WAS = 코요테(웹서버)+ 카탈리나(어플리케이션서버)





~~~java
package core;

import java.io.IOException;
import java.time.temporal.ChronoField;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.time.LocalDate;
/**
 * Servlet implementation class MemberLocalServlet
 */
@WebServlet("/myFirstServlet")
public class MyFirstServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
	int member_v=0;
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		response.setContentType("text/html; charset=utf-8");
		PrintWriter out =response.getWriter();
		String p1 = request.getParameter("p1");
		if(p1==null) {
			p1 ="GUEST";
		}
		LocalDate now = LocalDate.now();
		int p2 = now.get(ChronoField.DAY_OF_WEEK);
		String week[] = {"", "월", "화", "수", "목", "금", "토", "일"};

		
		out.print("<h1>"+p1+"님 반가워요...  오늘은 "+week[p2]+"요일입니다!!"+"</h1>");
		

		out.close();
	}

}
~~~

