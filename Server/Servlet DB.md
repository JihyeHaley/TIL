## Servlet 에서의 DB 연동

1. JDBC 드라이버 로딩 (class.forName())
2. DB 서버 접속 (DriveManager.getConnection("jdbcurl", "계정", "암호")
3. SQL 문을 수행하기 위한 Statement, PreparedStatement 객체 생성
4. Select 명령을 수행할 때는  - executeQuery() : ResultSet(next, getxxxx())
   INSERT, DELETE, UPDATE, CREATE TABLE, DROP TABLE....
   * excuteUpdate()  : int  //리턴값이 숫자. //int 의미는 SQL 명령에 의해 변화된 행의 갯수

 

visitorMain.html - 방명록 리스트 보기  --->  visitorDB를 Get방식으로 요청해서 받을거 visitordb(GET)

​								방명록 작성하기      --->  visitorForm.html --> visitordb(POST)



2개의 html (visitorMain, visitorForm)

1개의 Servlet (/visitordb)

visitorDBServlet(/visitordb)

​	POST - 전송되는 쿼리 문자열을 visitor 테이블에 저장

​	GET -  visitor 테이블의 데이터를 모두 읽어 와서 테이블 형식으로 브라우저로 출력





StackTrace 넌 뭐하는 친구이니?