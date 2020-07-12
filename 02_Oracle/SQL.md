# SQL Day1

##### DQL -> (DML --> DDL)

##### CRUD

##### Create : INSERT 명령어

##### Read (DQL에 속한다) : *SELECT 명령어*

##### Update : UPDATE 명령어

##### Delete : DELETE 명령어

##### 기본키!! Primary Key

서버와 **클라이언트**

​             1) cmd 창에 나가서 SQLplus라는 명령을 수행시킨다.

​            2) SQLdeveloper 라는 추가 프로그램을 설치하여 사용 

cmd;

select user from dual;

오라클이 주는 학습용 일반계정 : scott(생성), hr(lock해제)





### [Select 명령어]

대소문자를 구별하지 않다

*  **FROM -> WHERE -> SELECT**

* select  추출하려는 컬럼명리스트 | * (3)

* from 테이블이름 (모든 행을 꺼낼때) <- 얘먼저 가장 먼저 가져온다. (1)

* [where 행의 조건식 (2)]

* order by 컬렴명(별칭, 식), desc[asc]

* 

* example

  * ```sql
    select * from emp;
    
    select *
    from emp;
    
    select ename, sal from emp; //emp가 갖고 있는 행만큼
    
    select sysdate from dual;
    
    select user from dual;
    
    select 100+200 from dual; // dual은 한번만 는 명령
    						  // 1행 1열 ("x")
    
    select ename, sal
    from emp 
    where sal > 2000
    order by sal desc; 
    /*or*/ order by sal asc; 
    /*or*/ order by sal
    
    ```

    

