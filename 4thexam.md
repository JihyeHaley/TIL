* get, post

* Httpsession

  * 식별자, 생성 시간, 최종 액세스 시간 등의 Session에 대한 정보를 참조하여 제어한다.
  * HttpSession 객체 생성방법

  ~~~html
  - HttpServletRequest객체.getSession() : // 기존 Session이 있으면 기존 Session 객체를, 없으면 새로 생성하여 반환한다.
  - HttpServletRequest객체.getSession(false) // 기존 Session이 있으면 기존 Session 객체를, 없으면 null을 반환한다.
  ~~~

  * HttpSession METHOD

  ~~~html
  - setAttribute(String, Object)
  - getAttribute(): Object
  - getCreationTime(): long
  - getLastAccessedTime(): long
  - setMaxInactiveInterval(int second) // Client가 이 시간동안 request가 없으면 Session 만료.
  - getMaxInactiveInterval(): int
  - invalidate() : // Session 종료. Session에 속한 속성들도 같이 제거.
  - getId() : String // jSessionId값 return
  ~~~

  

* Query 없을 때 return 되는 것들  

* getAttribute SetAttribute
  * Attribute : 공유되는 데이터
  * getAttribute는 특정 요소 노드 내에 특정 한 속성값을 가져오는 메소드
    * Object x =request.getAttribute("객체");
  * setAttribute는 메소드 속성값을 변경시키는 메소드
    * 객체명.setAttribute("속성노드명", 새로운 속성값);

* param

  * <object> 요소에 의해 호출되는 플러그인의 매개변수(parameter)를 정의할 때 사용한다.

* Scope
  * Scope : 속성을 공유할 수 있는 유효범위
  * Application
    * 가장 큰 영역
    * 웹 어플리케이션이 실행되고 있는 동안 속성을 사용할 수 있다.
    * 모든 이가 공유할 수 있는 데이터
  * Session
    *  한 브러우저 내에 1개의 session 만 생성
  * Request
    * Forward,
    * request영역의 속성을 여러 페이지에서 공유할 수 있다.
  * Page
    * page 내장객체가 아닌 pageContext내장객체를 통해 접근할 수 있는 영역

* session 객체 삭제할 때 메서드
  *  void invalidate()
  * https://wickedmagic.tistory.com/131?category=468124
  * 세션값 삭제하기
    * removeAttribute.jsp
    * session.removeAttribute("...");

* servlet 수행상의 특징

* (el, 수행문태그)
* SpringIoC?
* Filter
* statement prepared statement
  * https://javaconceptoftheday.com/statement-vs-preparedstatement-vs-callablestatement-in-java/
* Create statement
  * https://javaconceptoftheday.com/statement-vs-preparedstatement-vs-callablestatement-in-java/

* Pom
  * maven 내부에서 반본적으로 사용될 상수 값을 정의할 때 사용
    * build
    * version
    * properties
    * scm
    * repositories
    * distribution Mangement
    * profiles
* Maven 
  * 자바 프로젝틑의 build를 자동화 해주는 tool
  * java source compile, package -> deploy
    1. settings.xml
    2. pom.xml