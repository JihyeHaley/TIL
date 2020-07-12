### day2 실습



#### 문서-1

```
[문제1] 10 에서 38사이의 숫자 중에서 2씩 증가한 값으로 벡터를 생성하고
           3행 5열의 매트릭스를 만들어 m1 에 저장한다.(행 우선 저장)
           각 원소 값들에 100을 더한 결과로 매트릭스 m2 를 만든다.
           m1 에서 최대값을 추출하여 m_max_v 에 저장한다.                     
           m1 에서 최소값을 추출하여 m_min_v 에 저장한다.   
	   m1 에서 행 단위의 최대값을 추출하여 row_max 에 저장한다.
	   m1 에서 열 단위의 최대값을 추출하여 col_max 에 저장한다.
           m1, m2, m_max_v, m_min_v, row_max, col_max를 화면에 출력한다.

[문제2]  다음과 같이 값이 구성되는 매트릭스를 정의하여 m2 에 저장한다.
       1,2,3 의 벡터 n1, 4,5,6 의 벡터 n2, 7,8,9 의 벡터 n3 를 이용하여 matrix를 생성한다.
 
[문제3] 다음과 같이 값이 구성되는 매트릭스를 정의하여 m3 에 저장한다.
       1~9 의 벡터를 이용하여 matrix를 생성하고 출력한다.
 
[문제4]  m3 를 가지고 다음과 같이 값이 구성되는 매트릭스를 정의하여 m4 에 저장하고 출력한다.
	 
[문제5] 다음과 같이 구성 되는 2행 3열 매트릭스 alpha를 생성한 후에
        

       alpha에 ‘x’, ‘y’, ‘z’ 라는 행을 추가하여 alpha2 를 만들고 출력한다.
       alpha에 ‘s’, ‘p’ 라는 열을 추가하여 alpha3 를 만들고 출력한다.



[문제6] 다음과 같이 값이 구성되는 배열을 정의하여 a 라는 변수에 저장한다.
 

       (1) 2행3열4층의 데이터를 출력한다.
       (2) 각 층마다 2행의 데이터를 출력한다.
       (3) 각 층마다 1열의 데이터를 출력한다.
       (4) 3층의 모든 데이터를 출력한다.
       (5) a라는 배열을 구성하는 모든 데이터에 100을 + 연산하여 출력한다.
       (6) 4층의 모든 데이터들에 100을 곱한 결과를 출력한다.
       (7) 각층의 1행, 2열과3열만 출력한다.
       (8) 2층의 2행 데이터들의 값을 100을 더한 값으로 변경한다.
       (9) 1층의 모든 데이터들의 값에 2를 뺀 값으로 변경한다.
       (10) a 배열의 모든 데이터 값들을 10을 곱한 값으로 변경한다.
       (11) a 변수를 삭제한다.

```



#### 정답-1

lab_2.r

```r
#문제1
vec <- seq(10,38, 2)

m1 <-matrix(vec, nrow=3, byrow=TRUE)
m1 <- matrix(seq(10,38, 2), nrow=3, byrow=TRUE); m1

m2 <- m1+100

m_max_v <- max(m1)
m_min_v <- min(m1)
row_max <- apply(m1, 1, max)
col_max <- apply(m1, 2, max)

m_max_v; m_min_v; row_max; col_max

#문제2
n1 <-c(1,2,3)
n2 <-c(4,5,6)
n3 <-c(7,8,9)

m2<-cbind(n1,n2,n3); colnames(m2) <- NULL; m2

#문제3

m3 <- matrix(1:9, nrow=3, byrow=TRUE); m3

#문제4

rownames(m3) <- c("row1", "row2", "row3")
colnames(m3) <- c("col1", "col2", "col3")
m4<- m3 ;m4

#문제5
a<- letters[1:6]
alpha <- matrix(a, nrow=2); alpha

b<- c('x','y','z')
alpha2 <- rbind(alpha, b); rownames(alpha2) <- NULL; alpha2

c<- c('s', 'p')
alpha3 <- cbind(alpha2, c); colnames(alpha3)<-NULL; alpha3

#문제6
a<- array(1:24, dim=c(2,3,4))

a[2,3,4] 
a[2,,]
a[,1,] 
a[,3,]
a*100 
a[,,4]*100
a[1,2:3,] 
a<- a[2,,2]+100 
a<- a[,,1]-2 ;a
a<- a*10
rm(a)

```

<hr>

#### 문서-2

```
[문제1] airquality 라는 데이터셋이 몇 개의 관측치를 가지고 있으며 어떠한 변수들을 가지고 있는지 채크하려 한다. 이 때 사용되는 R코드를 작성하시오.

[문제2] 다음과 같이 값이 구성되는 데이터프레임을 정의하여 df1 에 저장한다.
 
[문제3] 다음과 같이 값이 구성되는 데이터프레임을 정의하여 df2 에 저장한다.
		 
[문제4] c() 함수로 먼저 벡터를 생성한 다음 data.frame()사용해서 다음과 같이 구성되는 데이터 프레임 df3를 만들어 출력해 본다.(제품명이 팩터형이 되지 않게 한다.)
	제품명	가격	판매량
	사과	1800	24
	딸기	1500	38
	수박	3000	13

[문제5] 앞에서 만든 데이터 프레임을 이용해서 과일 가격 평균, 판매량 평균을 구하여 출력한다.

[문제6] 다음 세 벡터를 이용하여 데이터프레임 df4를 생성하고, name 변수는 문자, gender 변수는 팩터, math 변수는 숫자 데이터의 유형이라는 것을 확인하시오.
	name <- c(“Potter”, “Elsa”, “Gates”, “Wendy”, “Ben”)
	gender <- factor(c(“M”, “F”, “M”, “F”, “M”))
	math <- c(85, 76, 99, 88, 40)

위에서 만든 데이터프레임에 대해 다음 작업을 수행하시오. 
(a) stat 변수를 추가하시오. stat <- c(76, 73, 95, 82, 35)
(b) math 변수와 stat 변수의 합을 구하여 score 변수에 저장하시오. 
(c) 논리 연산 인덱싱을 이용하여 score가 150 이상이면 A, 100 이상 150 미만이면 B, 70 이상 100 미만이면 C, 70 미만이면 D 등급을 부여하고 grade 변수에 저장하시오.	

[문제7] emp변수에 할당된 데이터프레임 객체의 구조를 점검한다.
[문제8] emp 에서 3행, 4행 , 5행만 출력한다.
[문제9] emp 에서 ename컬럼만 출력한다.
[문제10] emp 에서 ename 과 sal컬럼만 출력한다.
[문제11] 업무가 SALESMAN 인 사원의 이름, 월급, 직업을 출력한다.
[문제12] 월급이 1000 이상이고 3000이하인 사원들의 이름, 월급, 부서번호를 출력한다.
[문제13] emp 에서 직업이 ANALYST 가 아닌 사원들의 이름, 직업, 월급을 출력한다.
[문제14] emp 에서 업무가 SALESMAN 이거나 ANALYST 인 사원들의 이름, 직업을 출력한다.
[문제15] emp 에서 커미션이 정해지지 않은 직원의 이름과 월급 정보를 출력한다.
         (NA 값을 채크하는 것은 제공된 교육자료의 1 페이지를 참고한다.)
[문제16] 월급이 적은 순으로 모든 직원 정보를 출력한다.

```



#### 문서-2

lab_3.r

```r
#문제1

str(airquality)
dim(airquality) #행, 열의 개수만 볼려면면

#문제2

x <- 1:5
y <-seq(2,10,2)
df1 <- data.frame(x,y)
colnames(df1) <- c('x','y')
rownames(df1) <- c(1,2,3,4,5)
df1


#문제3
col1 <- c(1,2,3,4,5)
col2 <- c('a', 'b','c','d','e')
col3 <- seq(6,10,1)
df2 <- data.frame(col=1:5, col2=letters[1:5], col3=seq(6,10,1))
df2<-data.frame(col1, col2, col3)

#문제4
df3 <- data.frame(
  제품명=c('사과', '딸기', '수박'), 
  가격=c(1800, 1500, 3000), 
  판매량=c(24,38,13), stringAsFactors=F) #자동으로 팩터형으로 바뀌니깐.

#문제5
mean(df3$가격)
mean(df3$판매량)

#문제6
df4 <-data.frame(
  name=c("Potter", "Elsa", "Gates", "Wendy", "Ben"), 
  gender=c(factor(c("M","F","M","F","M"))),
  math=c(85,76,99,88,40))

is.character(name); is.factor(gender); is.numeric(math)
df4$stat=c(76, 73, 95, 82, 35)

df4$score=df4$math+df4$stat

df4$grade=ifelse(df4$score>=150, 'A', 
                 ifelse(df4$score>=100, 'B',
                        ifelse(df4$score>=70, 'C','D')))

#문제7
str(emp)

#문제8
emp[c(3,4,5),]

#문제9
emp[,"ename",drop=F] 

#문제10
emp[,c("ename","sal"),drop=F] 

#문제11
subset(emp, select=c('ename', 'sal', 'job'), subset=(emp$job=="SALESMAN"))

#문제12
subset(emp, select=c('ename', 'sal', 'empno'), subset=(sal>=1000 & sal<=3000))
subset(emp, select=c('ename', 'sal', 'empno'), subset=(emp$sal>=1000 & sal<=3000))

#문제13
subset(emp, select=c('ename', 'job', 'sal'), subset=(emp$job!='analyst'))


#문제14??
subset(emp, select=c('ename', 'job'), subset=(emp$job =="salesman" | emp$job=="analyst"))       
emp[emp$job=="salesman" & emp$job =="analyst", c("ename","sal")]

#문제15
subset(emp,select=c('ename','sal'),is.na(emp$comm)) 

subset(emp, is.na(comm), c(ename, job))

#문제16 ??
emp[order(emp$sal, decreasing=F),]

## 문제 16번 응용 
sort(emp$sal)
order(emp$sal) #index로 추출

```

