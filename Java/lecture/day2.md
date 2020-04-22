# Day2

연산자 피연산자(항)

++su, --su, -su, !true

++su, su++ <- 요 2개는 다른고얌

I-value: 방: 변수
r-value: 값: 식(변수, 리터럴, 연산식, 리턴값이 있는 메서드의 호출식)

= 연산을 처리할 때
I-value의 타입과 r-value의 타입은 동일해야 한다.
그런데 만일 다른 타입이 사용되면 r-value의 값이 손실되지 않는 범위에서 I-value의 타입으로 자동 변환한다.

int = char
(4)    (2)

int = double
(4)   (8)
ㄴ 이런 경우에는 형태를 변환해줘야 한다. e.g. ivalue=(int)dvalue

Boolean은 형태 변환 못해~~


```java
[조건문 Swtich]

	switch(식) {
	    ㄴ! 중괄호 셋트가반드시 필요
	    ㄴ! boolean 사용 못함. 
	    ㄴ! int(byte, short, char)랑 string만 사용할 수 있음!

	    case 비교값1 : 수행문장1;
		          수행문장2;
		          break;

	    case 비교값2 : 수행문장3;
		          수행문장4;
		          break;

	    case 비교값3 : 수행문장5;
		          수행문장6;			          
		          break;

	    case 비교값4 : 수행문장7;
		          수행문장8;	
		          break;

	    default: 수행문장 9; <- 그 외의 모든 경우 라는 뜻.
		
	}
```

```java
byte < short < int < long < float < double
(1)      (2)       (4)    (8)
char < int < long < float < double


short = char
char = short
char = byte
```

### 제어문

정의된 수행 문장들을 한번씩 순차적으로 수행하면서 진행하는 것이 기본이지만
조건에 따라 수행문장들을 선택하여 수행하거나 
반복해서 여러번 수행도록 하고자 할때 제어문을 사용한다.

- (선택) 조건 제어문 - if , else, = they are friend. they are not single exisintg
- 반복 제어문 - for, while, do ~ while
- 분기 제어문 - break, continue 

```java
case1)	if(조건식)
	     수행문장1:

case2)	if(조건식){
	    수행문장1:
	    수행문장2:
	}

case3)	if(조건식){
	    수행문장1:
	    수행문장2:
	}else
	    수행문장3:
	    수행문장4:
	}

int month = (int)(Math.random()*12)+1;
int month = (int)(Math.random()*12)+1;
int month = (int)(Math.random()*12)+1
```

```java
if(조건식1)
     수행문장1;
else if(조건식2)
     수행문장2;
else if(조건식3)
     수행문장3;
        ;
else
     수행문장n;
     
switch(식) {
      case 비교값1 : 수행문장1;
                          수행문장2;
      case 비교값2 : 수행문장3;
                          수행문장4;
      case 비교값3 : 수행문장5;
                          수행문장6;
      case 비교값4 : 수행문장7;
                          수행문장8;
      default : 수행문장9;
   }

switch(식) {
      case 비교값1 : 수행문장1;
                          수행문장2;
                          break;
      case 비교값2 : 수행문장3;
                          수행문장4;
                          break;
      case 비교값3 : 수행문장5;
                          수행문장6;
      case 비교값4 : 수행문장7;
                          수행문장8;
		break;
      default : 수행문장9;                    
   }
  
   식 : int(byte,short,char), String


       

```

### 반복 구문

```java
while : 조건이 만족되는 동안 반복하려는 경우

for(초기식:조건식:증감식)
    반복문장
while(조건식)
    반복문장

for(변수의 선언 및 초기화;반복횟수를 결정할 조건식;변수의 값을 변화시키는 식)
ㄴ 반드시 세미콜론을 사용해줘야 한다!!!!!!!!!!!
ㄴ e.g. for(;;)  -> infinite loof!!!
ㄴ for(int i=1; i<10;i++)
ㄴ for(int i=1;i <= 10;i+=2)
ㄴ for(int num=1; num <= 9; num++)
	System.out.print(5*num + "     ")
ㄴ for(int n=5; n>0;n--)
	System.out.print(n)
ㄴ 식은 생략될 수 있지만 세미콜론은 생략될 수 없다!
```

```java
// 실습1 OperTest1
public class OperTest1 {
	public static void main(String[] args) {
		int num1 = 100, num2 = 50;
	
		System.out.println(num1 + num2);
		System.out.println(num1 - num2);
		System.out.println(num1 * num2);
		System.out.println(num1 / num2);
		System.out.println(num1 % num2);
		System.out.println(num1 > num2);
		System.out.println(num1 <= num2);
		System.out.println(num1 == num2);
		System.out.println(num1 != num2);
	}
}
```

```java
// 실습2 OperTest2
public class OperTest2 {
	public static void main(String[] args) {
		// 증감연산자 : 증가연산자(++), 감소연산자(--)
		int su1, su2, su3, su4;
		su1 = 10;
		System.out.println(su1);
		System.out.println(++su1);
		System.out.println(++su1);
		System.out.println(++su1);
		System.out.println(--su1);
		
		su2 = 10;
		System.out.println(su2);
		System.out.println(su2++);
		System.out.println(su2++);
		System.out.println(su2++);
		System.out.println(su2--);
		
		su3 = 10;
		System.out.println(su3);	//10
		System.out.println(su3++);	//10
		System.out.println(++su3);	//12
		System.out.println(su3++);	//12
		System.out.println(--su3);	//12
		System.out.println(--su3);	//11
		
		su4 = 10;
		System.out.println(su4);	//10
		++su4;
		System.out.println(su4);	//10
		su4++;
		System.out.println(++su4);	//12
		System.out.println(su4++);	//12
		System.out.println(--su4);	//12
		System.out.println(--su4);	//11
	}
}
```

```java
// 실습3 OperTest3
public class OperTest3 {
	public static void main(String[] args) {
		int ivalue;
		char cvalue;
		double dvalue;
		boolean bvalue;
		
		ivalue = 100;
		cvalue = 'A';
		dvalue = 3.14;
		bvalue = true;
		
		System.out.println(ivalue);
		System.out.println(cvalue);
		System.out.println(dvalue);
		System.out.println(bvalue);
		
		ivalue = cvalue;
		System.out.println(ivalue);
		
		ivalue = (int)dvalue; 			// 강제 형변환 연산자
		System.out.println(ivalue);
		
	}
}
```

- **실습4 문제**

[if 문 사용 실습 ]

1. OperAndLab(&&연산자사용), OperOrLab(||연산자사용) 
   이라는 클래스를 각각 하나씩 생성한다.
2. grade 라는 변수를 int 타입으로 선언하고 1 부터 6 사이의 숫자를 
   추출하고 저장한다.
3. grade 의 값이 1 또는 2 또는 3이면 다음 결과를 출력한다.
   "x 학년은 저학년입니다."
   grade 의 값이 4 또는 5 또는 6이면 다음 결과를 출력한다.
   "x 학년은 고학년입니다."

```java
//실습4 OperAndLab & OperOrLab
public class OperAndLab {
	public static void main(String[] args) {
		int grade = 0;
		grade = (int)(Math.random() * 6) + 1;
		
		if(grade >= 1 && grade <= 3) {
			System.out.println(grade + "학년은 저학년입니다.");
		}
		else{
			System.out.println(grade + "학년은 고학년입니다.");
		}
	}
}

public class OperOrLab {
	public static void main(String[] args) {
		int grade = 0;
		grade = (int)(Math.random() * 6) + 1;
		
		if(grade == 1 || grade == 2 || grade == 3) {
			System.out.println(grade + "학년은 저학년입니다.");
		}
		else {
			System.out.println(grade + "학년은 고학년입니다.");
		}
	}
}
```

- 실습5 문제**

[if 문 사용 실습]

1. ConditionOperLab 이라는 클래스를 생성한다.
2. 1부터 5사이의 랜덤값을 추출한다.
3. 추출된 값이 1이면 300 과 50 의 덧셈 연산을 처리한다.
   추출된 값이 2이면 300 과 50 의 뺄셈 연산을 처리한다.
   추출된 값이 3이면 300 과 50 의 곱센 연산을 처리한다.
   추출된 값이 4이면 300 과 50 의 나눗셈 연산을 처리한다.
   추출된 값이 5이면 300 과 50 의 나머지 연산을 처리한다.
4. 출력 형식(단, 결과를 출력하는 수행문장은 한 번만 구현한다.)
   결과값 : XX

```java
// 실습5 ConditionOperLab
public class ConditionOperLab {

	public static void main(String[] args) {
		int num = 300;
		int num2 = 50;
		int rand = (int)(Math.random() * 6) + 1;
		
		if(rand == 1) {
			System.out.println("결과값 : " + num + num2);
		}
		else if(rand == 2) {
			System.out.println("결과값 : " + (num - num2));
		}
		else if(rand == 3) {
			System.out.println("결과값 : " + num * num2);
		}
		else if(rand == 4) {
			System.out.println("결과값 : " + num / num2);
		}
		else if(rand == 5) {
			System.out.println("결과값 : " + num % num2);
		}
	}
}
```

- **실습6 문제**

[연산자 실습]

1. TimeTest 라는 클래스를 생성한다.
2. time 이라는 변수를 선언하여 32150(초) 이라는 값을 초기화 한다.   
3. time 변수의 값으로 "XX시간 XX분 XX초" 형식으로 변환하여 출력한다.

```java
// 실습6 TimeTest
public class TimeTest {

	public static void main(String[] args) {
		int time = 32150;
		int hour, minute, second;

		minute = time/60;
		hour = minute/60;
		second = time%60;
		minute = minute % 60;
				
		System.out.println(hour + "시간" + minute + "분" + second + "초");

	}

}
```

```java
//실습7 RandomTest
public class RandomTest {

	public static void main(String[] args) {
//		System.out.println(Math.random()); // 0.0 <= n < 1.0
		double rand1 = Math.random();
		System.out.println(rand1);
		double rand2 = rand1 * 100;
		System.out.println(rand2);
		int rand3 = (int)rand2;
		System.out.println(rand3); // 0 ~ 99
		
		// rand1을 가지고 1부터 6사이의 난수를 만드는 식을 구현하고
		// sixNum 변수에 담아서 출력해 보기
		int sixNum = (int)(rand1 * 6) + 1;
		System.out.println(sixNum);
		
		// rand1을 가지고 1부터 45사이의 난수를 만드는 식을 구현하고
		// lottoNum 변수에 담아서 출력해 보기
		int lottoNum = (int)(rand1 * 45) + 1;
		System.out.println(lottoNum);
	}

}
```

```java
//실습8 IfTest1
public class IfTest1 {

	public static void main(String[] args) {
		int num = (int)(Math.random()*10) + 1;
		if(num % 2 == 0) {
			System.out.println(num + " : 짝수");
		}
		else {
			System.out.println(num + " : 홀수");
		}
	}
}

```

```java
// 실습9 IfTest2
public class IfTest2 {

	public static void main(String[] args) {
		System.out.println("문장1");
		System.out.println("문장2");
		
		if((int)(Math.random()*10) + 1 > 5) {
			System.out.println("문장3");
		}
		else {
			System.out.println("문장4");
			System.out.println("문장5");
		}
		System.out.println("문장6");
		
	}
}
```

```java
// 실습10 IfTest3
public class IfTest3 {

	public static void main(String[] args) {
		int month = (int)(Math.random()*12) + 1;

		if(month == 12 || month == 1 || month == 2) {
			System.out.println(month + " : 겨울");
		}
		else if(month == 3 || month == 4 || month == 5) {
			System.out.println(month + " : 봄");
		}
		else if(month == 6 || month == 7 || month == 8) {
			System.out.println(month + " : 여름");
		}
		else if(month == 9 || month == 10 || month == 11) {
			System.out.println(month + " : 가을");
		}
		
	}
}
```

```java
// 실습11 IfTest4
public class IfTest4 {

	public static void main(String[] args) {
		int score = (int)(Math.random()*101);
		
		if(score >= 90) {
			System.out.print(score + " : A");
			if(score >= 97) {
				System.out.println("+등급");
			}
			else if(score >= 94) {
				System.out.println("0등급");
			}
			else {
				System.out.println("-등급");
			}
		}
		else if(score >= 80) {
			System.out.print(score + " : B");
			if(score >= 87) {
				System.out.println("+등급");
			}
			else if(score >= 84) {
				System.out.println("0등급");
			}
			else {
				System.out.println("-등급");
			}
		}
		else if(score >= 70) {
			System.out.print(score + " : C");
			if(score >= 77) {
				System.out.println("+등급");
			}
			else if(score >= 74) {
				System.out.println("0등급");
			}
			else {
				System.out.println("-등급");
			}
		}
		else if(score >= 60) {
			System.out.print(score + " : D");
			if(score >= 67) {
				System.out.println("+등급");
			}
			else if(score >= 64) {
				System.out.println("0등급");
			}
			else {
				System.out.println("-등급");
			}
		}
		else {
			System.out.println(score + " : F등급");
		}
		System.out.println("수행종료!!");		
	}
}
```

- **실습12 문제**

[switch 문 사용 실습 ]

1. OperAndLab.java를 복사해서 SwitchLab1.java를 생성한다.
2. 다음 기능을 if 문이 아닌 switch 문으로 변경하여 구현한다.
   grade 의 값이 1 또는 2 또는 3이면 다음 결과를 출력한다.
   "x 학년은 저학년입니다."
   grade 의 값이 4 또는 5 또는 6이면 다음 결과를 출력한다.
   "x 학년은 고학년입니다."

```java
// 실습12 SwitchLab1
public class SwitchLab1 {

	public static void main(String[] args) {
		int grade = 0;
		grade = (int)(Math.random() * 6) + 1;
		
//		if(grade >= 1 && grade <= 3) {
//			System.out.println(grade + "학년은 저학년입니다.");
//		}
//		else{
//			System.out.println(grade + "학년은 고학년입니다.");
//		}
		
		switch (grade) {
		case 1:
		case 2:
		case 3:
			System.out.println(grade + "학년은 저학년입니다.");
			break;
		case 4:
		case 5:
		case 6:
			System.out.println(grade + "학년은 고학년입니다.");
			break;
		}
			
	}

}
```

- **실습13 문제**

[switch 문 사용 실습 ]

1. ConditionOperLab.java를 복사해서 SwitchLab2.java를 생성한다.
2. 다음 기능을 if 문이 아닌 switch 문으로 변경하여 구현한다.
   추출된 값이 1이면 300 과 50 의 덧셈 연산을 처리한다.
   추출된 값이 2이면 300 과 50 의 뺄셈 연산을 처리한다.
   추출된 값이 3이면 300 과 50 의 곱센 연산을 처리한다.
   추출된 값이 4이면 300 과 50 의 나눗셈 연산을 처리한다.
   추출된 값이 5이면 300 과 50 의 나머지 연산을 처리한다.
3. 출력 형식(단, 결과를 출력하는 수행문장은 한 번만 구현한다.)
   결과값 : XX

```java
// 실습13 SwitchLab2
public class SwitchLab2 {

	public static void main(String[] args) {
		int num = 300;
		int num2 = 50;
		int rand = (int)(Math.random() * 5) + 1;
		int result = 0;

		switch(rand) {
			case 1:
				result = num + num2;
				break;
			case 2:
				result = num - num2;
				break;
			case 3:
				result = num * num2;
				break;
			case 4:
				result = num / num2;
				break;
			default:
				result = num % num2;
		}
		System.out.println(result);
	}
}
```

```java
// 실습14 SwitchTest1
public class SwitchTest1 {

   public static void main(String[] args) {
      int num=(int)(Math.random()*10)+1;
      switch(num%2) {
      case 0 : System.out.println(num +" : 짝수");
               break;
      case 1 : System.out.println(num +" : 홀수");
      }
   }
}
```

```java
// 실습15 SwitchTest2
public class SwitchTest2 {

   public static void main(String[] args) {
      int month = (int)(Math.random()*12)+1;
      
      switch(month) { //식:변수, 연산식, 리턴값이 있는 메서드의 호출식(int,String)
                           // 반드시 하나의 값만 지정 가능 in case 
      case 12 :
      case 1 :
      case 2 : System.out.println(month + "월은 겨울");
               break;
      case 3: 
      case 4:
      case 5: System.out.println(month + "월은 봄");
               break;
      case 6: 
      case 7:
      case 8: System.out.println(month + "월은 여름");
               break;
      default: System.out.println(month+ "월은 가을");
      }
   }
}
```

```java
// 실습16 SwitchTest3
public class SwitchTest3 {

	public static void main(String[] args) {
		int score = (int)(Math.random()*101);
		
		switch(score / 10) {
			case 10:
			case 9:System.out.println(score + " : A등급");
				break;
			case 8:System.out.println(score + " : B등급");
				break;
			case 7: System.out.println(score + " : C등급");
				break;
			case 6: System.out.println(score + " : D등급");
				break;
			default:
				System.out.println(score + " : F등급");
		}
		System.out.println("수행종료!!");
	}

}
```
