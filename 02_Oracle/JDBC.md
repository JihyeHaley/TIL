# JDBC

##### [JDBC (Java DataBase Connectivity) 프로그래밍]

- Java API

  Java.sql

  Javax.sql

- DBMS 에 무관하게 프로그램을 개발할 수 있다.

- 구성: JDBC API + JDBC Driver

  ​		(인터페이스) (인터페이스들의 구현클래스)

  ​		DBMS에 무관 DBMS에 따라 달라진다.

  팩토리메서드 : 객체 생성을 대신해주는 일반 메서드

   SQL명령을 수행시키는 기능을 지원하는 객체 - ***Statement***

  ​										executeQuery() : ResultSet - SELECT

  ​										executeUpdate():int - 그 외의 모든 SQL

  **(x)**  Statement  stmt = new Statement() ;

  **(O)** Statement stmt = Connection 객체의 createStatement();

* JDBC 프로그램의 구현순서

  1. JDBC  Driver 로딩 - Class.forName()

  2. DBMS에 접속 - DriveManager.getConnection("jdbc url", "계정", "암호");

  3. Statement/PreparedStatement 객체 생성

  4. 처리하려는 기능에 따라서 SQL 문을 전달하고 수행시킨다.

  5. 결과처리

     ResultSet 객체
     next(). getXXX()

     Select 명령의 수행 결과 여부에 관계없이 ResultSet  객체는 리턴

  6. 종료시 close() 필수~~~ 