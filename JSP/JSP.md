## JSP



#### : JavaServer Pages

프로그램이 흘러가는 흐름 = Thread

|    CGI    |   --->   |         ASP, PHP          |                           |
| :-------: | :------: | :-----------------------: | :-----------------------: |
|  Servlet  |   --->   |            JSP            | 실행시 Servlet으로 변경됨 |
|  (1998)   | 생성년도 |          (1999)           |                           |
| 자바+HTML |          | HTML+JSPX태그+약간의 Java |                           |
|           |          |       마지막 공부는       |       MVC 개발 패턴       |
|           |          |                           |       Servlet + JSP       |
|           |          |                           |        요청 + 응답        |

1. 내장객체 -9개

   * request, 
   * response, 
   * session, 
   * out, 
   * application, 
   * config,
   * exception page, 
   * pageContext

2. JSP 태그
    <%@  %>,    <%!   %>,      <%=   %>,      <%   %>,      <%--   --%>
   지시자태그,    선언문태그,     표현식태그,    수행문태그,      주석태그

3. 액션태그

   ~~~jsp
   <jsp:include/>
   <jsp:forward/>
   <jsp:pram/>
   ~~~

4. 커스텀태그
   필요에 의해서 고객이 하고 싶은대로 할 수 있게 해준

   **JSTL**/;/



<JSP태그 연습>

~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>beginner</h1>
<hr>
<h3>Current time <%= java.time.LocalDateTime.now() %></h3>
</body>
</html>
~~~



<멤버변수> ! 있음.

<지역변수> ! 없음.



인용구 안에서도 쓸 수 있다.

request.getHeader("referer")

은 요청한 URL을 뽑아오는 메소드 호출! 자동으로 가져옴 



#### Forward 다른 방법

~~~java
String url;
if(input==rand){
  url= ;
}else{
  url= ;
}

request.getRequestDispatcher(url).forward(request,response)
~~~



#### JSP에서 현재시간 출력

~~~java
LocalDateTime ctime= LocalDateTime.now();

DateTimeFormatter formatter = DateTimeFormatter.offPattern("hh~~~~");
~~~



