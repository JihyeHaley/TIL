# Join

☘️표시는 안했지만 scott 계정에서 EMP데이터를 가져오는 것이 아니라면 반드시 ***FROM DUAL*** 써줘야 합니다! 



#### * 집합연산자와 조인의 차이점

조인은 두 개 이상의 테이블을 연결하여 하나의 테이블처럼 출력할 때 사용하는 방식. 

* 집합 연산자를 사용한 결과는 두 개 이상 SELECT문의 결과 값을 세로로 연결한 것이고, 

* 조인을 사용한 결과는 두개 이상의 테이블 데이터를 가로로 연결한 것.
* 조인은 where 절에 적는다.
* 조인은 같은 행이 없는 절은 삭제해버린다. == innerjoin
  * 일치하는 행이 없으면 다 빼버려서 오류가 발생할 수 있다.
* null인 것도 표시하고 싶다면 = 추가하고자 하는 테이블에 (+) 값을 표시! 
* 저장하는 건 아니고 셀렉트 하는 동안에만 합쳐버리는 거

~~~sql
--기본형
select * from emp, dept 
--모두다 출력되게 한다.


select * 
from emp, dept
where emp.deptno = dept.deptno;
-- inner join
-- adams의 deptno가 null이라서 근데 둘 null인게 없어서 제외된 것
-- adams도 빠지고 no 40번호 다 빠졌다


-- outer join case 4개
--1. 
select * 
from emp, dept
where emp.deptno = dept.deptno(+);
-- left outer join

--2.
select * 
from emp, dept
where emp.deptno(+) = dept.deptno;
-- right outer join
-- 40번 deptno가 일단 출력이 된다.
-- null로 나오지만 40번 deptno = Operation이 나오긴 한다.
-- 하지만 Adams가 빠졌다.


--3.
where emp.deptno(+) = dept.deptno(+);
-- 지원되지 않는 형식이다!!!


--4. 해결방법이 있는 방안 union 사용
select * from emp, dept where emp.deptno = dept.deptno (+);
union
select * from emp, dept where emp.deptno(+) = dept.deptno;


~~~



등가조인(222)

비등가조인(224)



자체조인 (225) self join

크로스 조인 ???



#### * ANSI JOIN

##### INNER JOIN

###### 1) inner join - using 

~~~sql
select 
from 테이블 1 join 테이블 2 using (조인에 사용할 컬럼명)
where 행에 대한 조건
~~~



###### 2) inner join - on

~~~sql
select 
from 테이블 1 join 테이블 2 on  (조인 조건식 ex) e.deptno=d.deptno)
where 행에 대한 조건
~~~



##### OUTER

* LEFT, RIGHT, FULL 조인!!!

###### 3)outer join - using

~~~SQL
select 
from 테이블 1 LEFT join 테이블 2 using (조인에 사용할 컬럼명) 또는 on  (조인 조건식)
where 행에 대한 조건
~~~

###### 4) outer join -on 

~~~sql
select 
from 테이블 1 RIGHT join 테이블 2 using (조인에 사용할 컬럼명) 또는 on  (조인 조건식)
where 행에 대한 조건
~~~

###### 5) outer join - full

~~~sql
select 
from 테이블 1 FULL join 테이블 2 using (조인에 사용할 컬럼명) 또는 on  (조인 조건식)
where 행에 대한 조건
~~~



natural join -알아서 처리해주는 !!!!!!



~~~sql
select 컬럼리스트 | *
from 테이블명 
where 컬럼 = 정해진 값 이미 알고 있는 값

select 컬럼리스트 | *
from 테이블명
where 컬럼 = (select 명령)

select *
from emp
where sal > (select sal from emp where ename = 'ADAMS');
				1100;
				
				
컬럼 < ANY (10,5,7,6) -- 이중에 하나라도 참이면 참이된다.
					-- 제일 큰 값보다 작으면 된다.
					
컬럼 < ALL ( 10,5,7,6) --> 제일 작은 값보다 모두 다 작아야한다.


SELECT *
FROM EMP
WHERE SAL < ALL (SELECT SAL FROM EMP WHERE DEPTNO = 30);
~~~







```sql
--QUESTION
--제출파일명 : exercise6.sql
--모두 서브쿼리를 사용해서 해결합니다.

-- 1. 'DALLAS'에서 근무하는 직원의 이름, 직위, 부서번호를 출력하시오.
--이름         직위         부서번호              
---------- --------- ----------
--SCOTT	   ANALYST	20
--SMITH	   CLERK		20
--JONES	   MANAGER	20
--FORD	   ANALYST	20

select ename, job, deptno
from emp
where deptno in (select deptno from dept where loc='DALLAS');

--2. 'SMITH'보다 월급을 많이 받는 직원들의 이름과 월급 그리고 부서명을 출력한다.
--직원명               급여             부서명         
---------- ---------- ------------
--SCOTT		3000	RESEARCH
--ALLEN		1600	SALES
--WARD		1250	SALES
--JONES		2975	RESEARCH
--MARTIN	1250	SALES
--BLAKE		2850	SALES
--CLARK		2450	ACCOUNTING
--KING		5000	ACCOUNTING
--TURNER	1500	SALES
--JAMES		950	SALES
--FORD		3000	RESEARCH
--MILLER		1300	ACCOUNTING

select e.ename, e.sal, d.dname
from emp e join dept d using (deptno)
where e.sal 
		> any (select sal from emp where ename = 'SMITH');

--3. 30번 부서의 직원들과 동일한 해에 입사한 직원들의 이름, 월급, 
--   부서번호 그리고 입사년도를 출력한다.(30번부서 제외하고)
--Ename        Sal            DeptNo         HireYear
---------- ---------- ---------- ----------
--FORD	   3000	       20		1981
--KING	   5000	       10		1981
--CLARK	   2450	       10		1981
--JONES	   2975	       20		1981

select ename, sal, deptno, to_char(hiredate, 'yyyy')
from emp
where to_char(hiredate, 'yyyy') = any (select to_char(hiredate, 'yyyy') from emp where deptno=30) and deptno !=30;

--4. 'BLAKE'와 같은 부서에 있는 직원들의 이름과 입사일을 뽑는데 'BLAKE'는 빼고 출력한다. 
--ENAME      HIREDATE
---------- --------
--JAMES	     81/12/03
--TURNER     81/09/08
--BLAKE	     81/05/01
--MARTIN     81/09/28
--WARD	     81/02/22
--ALLEN	     81/02/20

select ename, hiredate
from emp
where deptno in (select deptno from emp where ename ='BLAKE') and ename != 'BLAKE';

--5. 평균급여보다 많은 급여를 받는 직원들의 직원번호, 이름, 월급을
-- 출력하되, 월급이 높은 사람 순으로 출력한다.
--  EMPNO ENAME    SAL
---------- ------ ----------
--7839	KING	5,000원
--7788	SCOTT	3,000원
--7902	FORD	3,000원
--7566	JONES	2,975원
--7698	BLAKE	2,850원
--7782	CLARK	2,450원

select empno, ename, sal
from emp
where sal > any (select avg(sal) from emp)
order by sal desc;


--6. 이름에 'T'를 포함하고 있는 직원들과 같은 부서에서 근무하고
--   있는 직원의 직원번호와 이름을 출력한다.
--EMPNO ENAME     
---------- ----------
--7902	FORD
--7566	JONES
--7369	SMITH
--7788	SCOTT
--7900	JAMES
--7844	TURNER
--7698	BLAKE
--7654	MARTIN
--7521	WARD
--7499	ALLEN  
select empno, ename
from emp e
where e.deptno in (select deptno from dept where upper(e.name) like '%T%');


--7 급여가 평균급여보다 많고,이름에 S자가 들어가는 직원과 동일한
--  부서에서 근무하는 모든 직원의 직원번호,이름 및 급여를 출력하시오.
--EMPNO      ENAME      SAL
----------  --------  -------
--7902	     FORD	      3000
--7566	     JONES      2975
--7788	     SCOTT      3000
--7698	     BLAKE      2850

select empnom, ename, sal
from emp
where sal > all (select avg(sal) from emp where upper(ename) like '%S%');

--8. 30번 부서에 있는 직원들 중에서 가장 많은 월급을 받는 직원보다
--   많은 월급을 받는 직원들의 이름, 부서번호, 월급을 출력한다. 
--   (단, ALL 또는 ANY 연산자를 사용할 것)
--  이름    부서번호   월급
--------------------------------
--JONES	20	2975
--SCOTT	20	3000
--FORD	20	3000
--KING	10	5000

select ename, deptno, sal
from emp
where sal > any (select max(sal) from emp where deptno=30) and deptno !=30;

--9. SALES 부서에서 일하는 직원들의 부서번호, 이름, 직업을 출력한다.
--DEPTNO    ENAME       JOB      
---------- ---------- ---------
--30번 부서  ALLEN	       SALESMAN
--30번 부서  WARD	       SALESMAN
--30번 부서  MARTIN      SALESMAN
--30번 부서  BLAKE	       MANAGER
--30번 부서  TURNER      SALESMAN
--30번 부서  JAMES	       CLERK
 
 select deptno, ename, job
 from emp
 where deptno in (select deptno from dept where dname ='SALES');
 

--10. 'KING'에게 보고하는 모든 직원의 이름과 입사날짜를 출력한다. 
--     (KING에게 보고하는 직원이란 mgr이 KING인 직원을 의미함) 
--이름         입사날짜
---------- ----------
--JONES	   1981년 04월 02일
--BLAKE	   1981년 05월 01일
--CLARK	   1981년 06월 09일

select ename, to_char(hiredate, 'yyyy"년" mm"월" dd"일')
from emp
where mgr = (select mgr from emp where ename ='kING' );



```

