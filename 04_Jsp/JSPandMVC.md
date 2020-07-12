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

   * request

   * response

   * session

   * out

   * application

   * config

   * exception page,  **에러 날때만 사용 가능**

     ~~~jsp
     <%@ page isErrorPage="true" @>
       에러인지 아닌지 확인하고 해결할려고 쓰는 아이
       isErrorPage가 True 여야만 Exception이 작동한당
       
       jasper
       
     
       얘가 정의하고 있는 syntax 에러도 지켜줘야한다.
     ~~~

   * pageContext

2. JSP 태그
    <%@  %>        지시자태그
   **<%!   %>      **   선언문태그        자바코드 포함 수행문태그
**<%=  %>**         표현식태그        자바코드 포함
    **<%   %>**          수행문태그        자바코드 포함
    <%--   --%>.     주석태그
                          무조건 멤버변수가 되어버린다.
   
    * <%@ %> 지시자태그
   
      * Converter 라는 것이 jsp소스를 servlet으로 변경해준다.
   
        ~~~jsp
        <%@ page 속성명="속성값"... %>
        					속석명... 
        		* 배운 속성명 - language, contentType, PageEncoding, 
        									errorPage, isErrorPage, import
         	* 안배운 속성명 -- session, buffer, isELIgored ..
        
        
        <%@ include file="포함하려는 대상파일의 로컬 URL" %> : include 지시자 태그
        ~~~
   
        * 포함하는 위치: 이 지시자 태그가 사용된 위치
        * 포함하는 시기: JSP를 Servlet 으로 변환하기 전
        * 포함하는 대상: html, jsp, jspf(권장)
   
3. 액션태그

   ~~~jsp
   <jsp:include/>
   <jsp:forward/>
   <jsp:pram/>
   꺽새 를 꼭 주기
   ~~~

   | a.jsp | b.jsp |
   | ----- | ----- |

   Include action 태그로: 2개의 서블릿                                     (동적 Include)

   Include  지시자 태그로 : 1개의 서블릿 (변환시 일어나는 액션) (정적 Include)	

   * ***‼️Include 지시자 태그로 하면 반복되면 에러가 난다.***

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





xxxVO - Value Object  - 값을 보관하는 용도의 객체

xxxDAO - Data Access Object - DB 연동기능(JDBC)을 지원하는 객체

xxxService(xxxBiz) - Service Object - 이런 저런 서비스 로직을 지원하는 객체





Application scope는 재기동해도 계속 유지된다

서버를 죽이고 다시 키면 reset되서 시작된다.





(1) MVC라는 새로운 Dynamic Web Project

(2) 이 프로젝트에서 생성되는 소스(텍스트)들의 인코딩 정보를 utf-8로 설정

(3) 만들어진 MVC 프로젝트를 톰캣 서버에 컨텍스트로 등록

(4) src 폴더에 controller, model 패키지 생성

(5) WebContent 폴더에 images, jspexam 폴더 생성







VOClass만들어서 작동

