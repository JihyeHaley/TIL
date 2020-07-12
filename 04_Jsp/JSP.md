* Page Scope : Servlet 또는 JSP가 수행되는 동안만 유효한 객체 (공유가 안된다.)

* Request Scope : **HttpServletRequest**에 저장해줘야 한다.

​								응답되고 나면 사라진다.

* Session Scope : 일정시간동안 객체가 유지되도록 **HttpSession**. 최대 유지 시간이 브라우저가 살아있는 동안

* Application Scope: **Servlet Context**에 보관 
  * public void setAttribute(String key, Object value)
  * public object getAttribute(String key)
  * public void removeAttribute(String key)



### #MVC 방식

* 요청 - Servlet "RequestScope

* 응답 - JSP - RequestScope

Controller, View, Model



##### Model

1. Domain Model (Count VO 같은거)
2. Business Obj
3. DAO (JDBC)