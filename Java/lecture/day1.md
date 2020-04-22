# Day1

## 1. Installation(설치)

(1) 크롬 브라우저 설치 : https://www.google.com/chrome
(2) Java SE(JDK) 설치 : http://java.sun.com/ -> https://www.oracle.com/technetwork/java/index.html
     설치후 환경변수 설정 : JAVA_HOME, PATH
                                  JAVA_HOME - C:\Program Files\Java\jdk1.8.0_231
                                  PATH - %JAVA_HOME%\bin
(3) Eclipse 설치 : http://www.eclipse.org/
                        C:\unico\eclipse-workspace
                        프로젝트라는 폴더를 생성해야 한다.
                        Java Project   javaexam
                        Dynamic Web Project
                        Spring MVC Project
                                 :

 맛보기용 자바 프로그램 : FirstApp

## 1. JAVA 구문

JAVA의 정석 책 참고

### 개요

1. 데이터 타입: 2장
2. 변수 활용: 2장
3. 연산자: 3장
4. 제어문: 4장
5. 배열: 5장

----------------------------- 기본 구문

6. 클래스 정의와 객체 생성
7. 상속, 다형성, 추상클래스, 인터페이스
8. 예외처리

----------------------------- OOP  구문 객체지향 구문

9. API - Application Programming Interface

   자주 필요로하는 기능을 미리 만들어 놓은 프로그램
   클래스(Math, Date, Calendar, ...) - 패키지(java.io, java.net,java.sql, java.lang...) 패키지들
   IO 패키지 - 파일 입출력 패키지. 
   패키지 - 클래스 묶음. JAVA.LANG - OBJECT, STRING, STIRNGbUFFER 등등 클래스들.
   패키지화 학습 소스들을 패키지화 : DAY1, DAY2 ..... 클래스 묶어 놓고, 그룹화

### LiteralTest

1. 데이터 타입
   숫자데이터 - 정수(byte(1바이트 -128~+127), short(2), int(4), long(8)), 실수(float(4), double(8))
   논리데이터 - True and False (Boolean)
   문자데이터 - 문자의 코드값 처리할 수 있는 타입, 2바이트, '1' ->0031, 'a' -> 0061, '가' - AC00
   문자열데이터 - 객체로 취급, "ABC", "가나다", "123". "###". ""

1(정수)   1.0(실수)   '1'(문자)   "1"(문자열형)

abSW
ST009
ASCII Code

리터럴(Literal) : 프로그램 소스 코드에서 사용되는 데이터 값을 리터럴이라고 한다.
                    		1, 1.0, '1', "1", "가",  리터럴이라고 부른다.
	        				true, false, "java"
                    		!!!! 문자데이터 안에는 문자가 반드시 한!! 개!! 만 있어야 한다! 

변수 : 데이터 값을 저장하는 메모리의 방
       데이터 값을 저장하기 위해 메모리의 일정 공간에 붙여진 이름
        저장된 데이터 값을 계속해서 변경 가능
        반드시 만들어서 써야 한다
        필요시 생성해서 사용한다.

​        변수의 생성을 변수 선언이라고 한다. 

​		타입 변수명;
​        타입 변수명 = 초기값; // 초기값 : 최초로 넣어지는 값

​		정수 데이터 -> byte, short, int, long 중에서 선택 어지간하면 int

​		실수 데이터 -> float, double                          		어지간하면 float

​		문자 데이터 -> char

​    	논리 데이터 -> boolean

​		문자열 -> string

[대입연산자] 의 오른쪽에는 다양하게 올 수 있다! 
		오늘쪽에 있는 것에 먼저 연산이 된다.
	변수 =    식;
  	          변수, 리터럴,연산식, 리턴값이 있는 메서드의 호출식

```java
//방         값
L-value   R-value

10 = 20;		 it is impossible
data1 = data2;	 it is possible
data1 = 100; 	 it is possible

data1 = Math.random();  0.0 <= x < 1.0
```



### 연산자

```java
//- 기능
//  산술연산자, 비교연산자, 논리연산자, 조건연산자, 대입연산자
//	     ㄴ(조건문, 제어문하고 같이 쓰임)

//- 사용되는 항 (피연산자, 연산에 사용되는 데이터)의 갯수
//  단항 연산자 : ++num (num = num+1)
//  이항 연산자 : 항1 연산자 항2; it has variety of kinds maybe countless 
//  삼항 연산자 : 항1 ? 항2 : 항3
	       int bigNumber = num1> num2 ? num1 : num2;

	       int bigNumber;
	       if(num1>num2)
		bigNumber = num1;
	       else
		bigNumber = num2;

(우선순위 순)
. 
++. --. +, -, !, ~,(타입명) {부호 연산자} <-단항 연산자
*, /, %
+, -
==, !=, >, <, >=, <=, instanceof (7장 공부할때) <- 연산결과가 boolean 값으로 나온다
>>, >>>, <<, <<<
&, |, ^
&&
||
항1 ? 항2 : 항3
=, +=, -=, *=, /=

int su=10;
su = su + 3;
++su;
su += 1;
```

```java
//실습1 LiteralTest
public class LiteralTest {
	public static void main(String[] args) {
		System.out.println(1 + 1);		// 2
		System.out.println(1.0 + 1);	// 2.0 	1.0 + 1 -> 1.0 + 1.0 -> 2.0
		System.out.println('1' + 1);	// 50 	1이라는 문자의 값
		System.out.println("123" + 4);	// 11	"123" + 4 -> "123" + "4" -> "11"
		
		System.out.println(7777777777777777777777777777777D);
	}
}
```

```java
//실습2 VariableTest
public class VariableTest {

	public static void main(String[] args) {
		System.out.println(1+2+3+4+5+10); // 25
		System.out.println(1+2+3+4+5-10); // 5
		System.out.println(1+2+3+4+5*10); // 60
		System.out.println(1+2+3+4+5/10); // 10 10.5X
		
		
		char munja = 'A'; // 0x41, 65
		System.out.println(munja + munja); // 130
		System.out.println("" + munja + munja); // "" : NULL문자열
		System.out.println(munja + munja + ""); // 이미 계산 됐으니 숫자 값이 출력이 된다.
	}

}
```

- **실습3 문제**

다음에 제시된 세 개의 정수데이터(리터럴)를 변수를 선언하여 저장하고 합계와 평균을 
구하여 제시된 출력 형식과 같이 출력하는 프로그램을 작성하시오. 
(평균의 소수 이하는 고려하지 않는다.)
작성 클래스명 : Exercise1

10, 25, 33

[ 출력 형식 ]
합계 : 68
평균 : 22

```java
//실습3 Exercise1
public class Exercise1 {
	public static void main(String[] args) {
		int a = 10, b = 25, c = 33;
		int sum = 0, avg = 0;
		sum = a + b + c;
		avg = sum / 3;
		System.out.println("합계 : " + sum);
		System.out.println("합계 : " + avg);
	}
}
```

- **실습4 문제**

다음에 제시된 두 개의 정수데이터(리터럴)를 
변수를 선언하여 저장하고 
나눈 몫과 나머지를 구하여 제시된 출력 형식과 같이 
출력하는 프로그램을 작성하시오. 

작성 클래스명 : Exercise2
35, 10
[ 출력 결과 ]
35 를 10 으로 나눈 결과 몫은 3 이고 나머지는 5 입니다.  

```java
//실습4 Exercise2
public class Exercise2 {
	public static void main(String[] args) {
		int a, b;
		a = 35;
		b = 10;
		System.out.println("35를 10으로 나눈 결과 몫은 " + 35 / 10 + " 이고 " + "나머지는 " + 35 % 10 + " 입니다.");
	}
}
```

- **실습5 문제**

1. char 타입의 변수 name1, name2, name3 를 선언하고 본인 
   이름의 각 문자들을 문자 리터럴로 만들어 각각 저장한다.
2. 이름을 하나의 행에 출력한다.  
   작성 클래스명 : Exercise3

```java
//실습5 Exercise3
public class Exercise3 {

	public static void main(String[] args) {
		char name1, name2, name3;
		name1 = '유';
		name2 = '성';
		name3 = '진';
		System.out.println("" + name1 + name2 + name3); 
	}
}
```

-  **실습6 문제**

(문제에서 요구되는 변수들외에는 추가로 선언하지 않는다.)

1. int 타입의 변수 number 를 선언하고 100 이라는 값을 저장한다.
2. int 타입의 변수 result 를 선언한다.
3. number 변수의 값에 10을 더하고 결과를 result 에 담아 
   결과를 출력한다.    출력형식 : 덧셈 연산의 결과 - 110
4. number 변수의 값에 10을 빼고 결과를 result 에 담아 
   결과를 출력한다.    출력형식 : 뺄셈 연산의 결과 - 90
5. number 변수의 값에 10을 곱하고 결과를 result 에 담아 
   결과를 출력한다.    출력형식 : 곱셈 연산의 결과 - 1000
6. number 변수의 값에 10을 나누고 결과를 result 에 담아 
   결과를 출력한다.	  출력형식 : 나눗셈 연산의 결과 - 10

작성 클래스명 : Exercise4

```java
//실습6 Exercise4
public class Exercise4 {
	public static void main(String[] args) {
		int number = 100;
		int result = 0;
		result = number + 10;
		System.out.println("덧셈 연산의 결과 - " + result);
		
		result = number - 10;
		System.out.println("뺄셈 연산의 결과 - " + result);
		
		result = number * 10;
		System.out.println("곱셈 연산의 결과 - " + result);
		
		result = number / 10;
		System.out.println("나눗셈 연산의 결과 - " + result);
	}
}
```

