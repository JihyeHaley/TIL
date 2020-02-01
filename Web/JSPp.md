JSP ---------->Servlet

​	Custom Tag: 필요한 기능의 태그를 직접 만들 수 있는 기능

​			Apache Open Group: JSTL(Library) 만들어진 태그드르이 표준

​												  **J**ava **S**tandard **T**ag **L**ibrary

​												core library, xml library, sql library

​												fmt library, fn library

​	Action Tag: JSP가 제공하는 태그로 기능, 구현방법이 정해져있는 태그들..



ASP, PHP -> CGI

JSP ---- > 웹페이지 ----> HTML + JSP태그 + Java 코드

​	   규격화된 문서 -----> XML   + JSP태그 + Java 코드

​									  JSON + 

```
<h1>
<form>
<br>
<%= %>
<% %>
<jsp:forward /> <forward />
"jsp" 접두어       jsp태그 아님!
<jsp:useBean />
```



for 문

for( 변수선언 : 컬렉션객체 ){



}



다음 기능의 JSP를 구현해 본다. 파일명 : latlng.jsp

주소를 Query 문자열로 받아서 
https://maps.googleapis.com/maps/api/geocode/xml?address=Query문자열로받은주소&language=ko&key=AIzaSyD8k2DWC_7yFHCrH6LDR3RfITsmWMEqC8c

사이트에 요청하고 위도와 경도만 다음과 같이 추출하여 
출력하는 프로그램을 구현한다.

정상 처리시 ---
주소 : xxxx
위도 : xxxx
경도 : xxxx

오류 발생시 ---
오류가 발생했어요....





