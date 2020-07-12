# Day 3

``` java
L - value = r-value
(변수)        (식)

double    int
long       char
int         (int)double   
char       (char)int
```

l-value는 변수만 온다.
r-value는 식만 올 수 있다.
BUT 이 둘은 반드시 타입이 똑같아야한다.

둘이 타입이 다르면 형태를 반드시 변환해줘야한다.



l-value=r-value
변수      식
실수      정수
(자동으로 형이 변환된다)

- 자동 형 변환규칙.
  .without order, they are automaticallly chaning the type.
  rule 1. 정수에서 실수
  rule 2. 사이즉 적은 타입에서 큰 타입으로 !!!!


{see below for the size}
	byte                1
	short               2
	float int           4 
	double long      8

```java
   [e.g. 대입 연산]
double       ->         int
long          ->         char
int            ->    (int)double <= 이 친구는 강제로 형 변환 필요
char          ->    (char)int    

    c.f. boolean은 그 어떤 형태로 변환 할 수 없다!!

   [e.g. 식]
v1    +     v2
int          int         => int
long       long       => long
        float       float       => float
int         double    => doubl
int         char       => int
int         long       => long
long      float        => float

   c.f. char       char        => int
```

- 중첩된 for문 : 구구단

```java
상수; 초기화된 값이 고정되는 변수


for: 횟수에 반복, 값의 변화에 따른 반복
while: 조건에 따른 반복


for(초기식:조건식:증감식)
	반복문장

초기식:
while (조건식) {
	반복문장;
	증감식;
}
```

```java
// 실습 1 ForTest1
public class ForTest1 {

	public static void main(String[] args) {
		for(int num = 1; num <= 20; num++) {
			System.out.print(num +" ");
		}
		System.out.println();
		for(int num = 20; num >= 1; num--) {
			System.out.print(num + " ");
		}
		System.out.println();
		for(int num = 20; num >= 1; num-=3) {
			System.out.print(num + " ");
		}
		System.out.println();
		int num;
		for(num = 10; num >= 1; num-=3) {
			System.out.print(num + " ");
		}
		System.out.println();
		System.out.println(num);

	}
}
```

```java
// 실습2 ForTest2
public class ForTest2 {
   public static void main(String[] args) {

      for(int i=1;i<=50;i++) {
         System.out.println(Math.random()*10);
      }
   }
}
```

```java
//실습 3 ForTest3
public class ForTest3 {
   public static void main(String[] args) {
      for(int i=1;i<=50;i++) {
         System.out.println(Math.random()*10);
      }

   }
}
```

```java
// 실습4 ForTest4
public class ForTest4 {

	public static void main(String[] args) {
		// 10부터 1까지의 숫자에 대하여 숫자값과 해당 숫자의 제곱값을
		// 행단위로 출력해 보자

		for (int n = 10; n >= 1; n--) {
			System.out.println(n + " : " + n * n);
		}
		System.out.println("-----------------");
		// 10부터 20까지의 숫자에 대하여 3씩 증가시키면서 숫자값과
		// 해당 숫자의 제곱값을 행단위로 출력해 보자
		for (int n = 10; n <= 20; n+=3) {
			System.out.println(n + " : " + n * n);
		}
		System.out.println("-----------------");

	}
}
```

```java
// 실습5 ForTest5
public class ForTest5 {

	public static void main(String[] args) {
		// 1부터 10까지의 합을 출력
		int sum = 0;
	
		 for(int n = 1; n <= 10; n++) { sum = sum + n; } 
		 System.out.println("sum = " + sum);
		 
		 for(int n = 1; n <= 10; n++) { 
			 sum = sum + n;
			 System.out.println("sum = " + sum);
		 } 
	}
}
```

```java
// 실습6 ForTest6
public class ForTest6 {
	public static void main(String[] args) {
		// A ~ Z 까지 출력해 보자
		char munja = 'A';
		for (int i = 1; i <= 26; i++) {
			System.out.print(munja++ + " ");
		}
		System.out.println("\n------------------------");
		for (munja = 'A'; munja <= 'Z'; munja++) {
			System.out.print(munja + " ");
		}
		System.out.println("\n------------------------");
		munja = 'A';
		for (int i = 1; i <= 26; i++) {
			System.out.print(munja + " ");
			munja += 1;
		}
		System.out.println("\n------------------------");
		munja = 'A';
		for (int i = 1; i <= 26; i++) {
			System.out.print(munja + " ");
			munja = (char)(munja + 1); // 괄호로 묶어 주지 않으면 연산자 우선 순위 때문에 error난다.
		}
		System.out.println("\n------------------------");
	}
}
```

```java
// 실습7 ForTest7
public class ForTest7 {

	public static void main(String[] args) {
		for(int dan = 1; dan <= 9; dan++) {
			for(int num = 1; num <= 9; num++) {
				System.out.print(dan + "x" + num + "="+dan*num +'\t');
			}
			System.out.println();
		}
	}
}

```

```java
// 실습8 ForTest8
public class ForTest8 {

	public static void main(String[] args) {
		for(int dan = 1; dan <= 9; dan++) {
			for(int num = 1; num <= 9; num++) {
				System.out.print(dan+"x"+num+"="+dan*num+"\t");
			}
			System.out.println();
		}
	}
}
```

```java
// 실습9 ForTest9
public class ForTest9 {

	public static void main(String[] args) {
		final char DECO = '&';
		int rand = (int)(Math.random()*6 + 5);
		
		for(int i = 1; i <= rand; i++) {
			for(int j = 1; j <= i; j++) {
				System.out.print(DECO);
			}
			System.out.println();
		}
	}
}
```

```java
// 실습10 WhileTest1
public class WhileTest1 {

	public static void main(String[] args) {
		int sum = 0;
		int i = 0;
		while(sum < 100) {
			i = (int)(Math.random()*50) + 1;
			sum += i;
			System.out.println("sum = " + sum);
		}
	}
}
```

```java
// 실습11 WhileTest2
public class WhileTest2 {

	public static void main(String[] args) {
		System.out.println("main() 수행 시작");
		char munja = '가';
		while(munja <= '나') {
			System.out.println(munja);
			munja++;
		}
		System.out.println("main() 수행 종료");
	}
}
```

```java
// 실습12 WhileTest3
public class WhileTest3 {
	public static void main(String[] args) {
		int lottoNum;
		while(true) {
			lottoNum = (int)(Math.random() * 6) + 1;
			if(lottoNum == 3) {
				System.out.println("당첨!! ㅋㅋㅋ : " + lottoNum);
				break;
			}
			else {
				System.out.println("재시도!! ㅠㅠㅠ : " + lottoNum);
			}
		}
		System.out.println("수행 종료..." + lottoNum);
	}
}
```

- ****

  **실습13 문제**

1. ForLab1 이라는 클래스를 만든다.

2. 다음과 같은 결과가 출력되도록 구현한다.

   1 2 3 4 5 6 7 8 9 10

```java
// 실습13 ForLab1
public class ForLab1 {
	public static void main(String[] args) {
		for(int i = 1; i <= 10; i++) {
			System.out.print(i + " ");
		}
		System.out.println();

	}
}
```

- **실습14 문제**

1. ForLab2 이라는 클래스를 만든다.

2. 다음과 같은 결과가 출력되도록 구현한다.

   9 : 홀수
   8 : 짝수
   7 : 홀수
   6 : 짝수
   5 : 홀수
   4 : 짝수

```java
// 실습14 ForLab2
public class ForLab2 {
	public static void main(String[] args) {
		for(int i = 9; i >= 4; i--) {
			if(i % 2 == 0) {
				System.out.print(i + " : 짝수");				
			}
			else {
				System.out.print(i + " : 홀수");
			}
		}
		System.out.println();
	}
}
```

- **실습15 문제**

1. ForLab3 이라는 클래스를 만든다.

2. 1부터 10사이의 난수를 하나 추출한다.

3. 30부터 40사이의 난수를 하나 추출한다.

4. 첫번째 난수부터 두번째 난수 까지의 숫자들 중에서 짝수의 합을 구해
   다음 형식으로 출력한다.

   X 부터 Y 까지의 짝수의 합 : XX

```java
// 실습15 ForLab3
public class ForLab3 {
	public static void main(String[] args) {
		// rand 범위 설정
		// 곱셈의 수는 최댓값 - 최솟값 + 1
		// 덧셈의 수는 최솟값
		int randValue1 = (int)(Math.random() * 10 + 1); 
		int randValue2 = ((int)(Math.random() * 11) + 30); // 30 ~ 40
		int sum = 0;
		

		for(int i = randValue1; i <= randValue2; i++) {
			if(i % 2 == 0) {
				sum += i;
			}
		}
		System.out.println("X 부터 Y 까지의 짝수의 합 :" + sum);
	}
}
```

- **실습16 문제**

1. ForLab4 이라는 클래스를 만든다.
2. 3부터 10사이의 난수를 추출한다.(첫 번째 난수)
3. 1부터 3사이의 난수를 추출한다.(두 번째 난수)
4. 두 번째 난수값이 1이면 "*"을 첫 번째 난수값의 갯수로 하나의 행에 출력한다.
   두 번째 난수값이 2이면 "$"을 첫 번째 난수값의 갯수로 하나의 행에 출력한다.
   두 번째 난수값이 3이면 "#"을 첫 번째 난수값의 갯수로 하나의 행에 출력한다.

```java
// 실습16 ForLab4
public class ForLab4 {
	public static void main(String[] args) {
		int randValue1 = (int)(Math.random() * 8 + 3);// + randTemp;
		int randValue2 = (int)(Math.random() * 3 + 1);
	
//		System.out.println(randValue1);
//		System.out.println(randValue2);
		if(randValue2 == 1) {
			for(int i = 0; i < randValue1; i++) {
				System.out.print("*");				
			}
			System.out.print("\n");
		}
		else if(randValue2 == 2) {
			for(int i = 0; i < randValue1; i++) {
				System.out.print("$");				
			}
			System.out.print("\n");
		}
		else if(randValue2 == 3) {
			for(int i = 0; i < randValue1; i++) {
				System.out.print("#");				
			}
			System.out.print("\n");
		}
	}
}
```

- **실습17 문제**

1. ForLab5 이라는 클래스를 만든다.

2. int 타입으로 evenNum 변수와 oddNum 변수를 선언한다.

3. 1 부터 100 까지의 값 중에서 
   짝수의 합은 evenNum 에 누적하고 
   홀수의 합은 oddNum 에 누적한다.

4. 수행 결과는 다음과 같이 출력한다.

   1부터 100까지의 숫자들 중에서 
   짝수의 합은 XXX 이고 
   홀수의 합은 YYY 이다.

```java
// 실습17 ForLab5
public class ForLab5 {
	public static void main(String[] args) {
		int evenNum = 0;
		int oddNum = 0;
		
		for(int i = 1; i <= 100; i++) {
			if(i % 2 == 0) {
				evenNum += i;
			}
			else {
				oddNum += i;
			}
		}
		System.out.println("1부터 100까지의 숫자들 중에서");
		System.out.println("짝수의 합은 " + evenNum + " 이고");
		System.out.println("홀수의 합은 " + oddNum + " 이고");
	}
}
```

- **실습18 문제**

[모양 출력(중첩 for)]

1. ForLab6 라는 클래스를 만든다.

2. char 타입으로 상수를 하나 만들어 '&'로 초기화 한다.

3. 5부터 10사이의 난수를 하나 추출한다.

4. 추출된 숫자가 5라면 반복문을 사용하여 다음과 같이 출력한다.

   &
   &&
   &&&
   &&&&
   &&&&&

     추출된 숫자가 7이라면 반복문을 사용하여 다음과 같이 출력한다.

   &
   &&
   &&&
   &&&&
   &&&&&
   &&&&&&
   &&&&&&&

```java
// 실습18 ForLab6
public class ForLab6 {

	public static void main(String[] args) {
		final char DECO = '&';
		int rand = (int)(Math.random()*6 + 5);
		
		for(int i = 1; i <= rand; i++) {
			for(int j = 1; j <= i; j++) {
				System.out.print(DECO);
			}
			System.out.println();
		}

	}

}

```

- **실습19 문제**

[모양 출력(중첩 for)]

1. ForLab7 라는 클래스를 생성한다.

2. STAR 라는 상수를 만든고 '*'으로 초기화 한다.

3. 다음과 같은 결과가 되도록 구현한다.

   *******

   ******

   *****

   ****

   ***

   **
   *

```java
// 실습19 ForLab7
public class ForLab7 {

	public static void main(String[] args) {
		final char STAR = '*';
		for(int i = 1; i <= 7; i++) {
			for(int j = 7; j >= i; j--) {
				System.out.print(STAR);
			}
			System.out.println();
		}
	}
}
```

- **실습20 문제**

[모양 출력(중첩 for)]

1. ForLab8 라는 클래스를 생성한다.

2. 다음과 같은 결과가 되도록 구현한다.

   A
   BC
   DEF
   GHIJ
   KLMNO

```java
// 실습20 ForLab8
public class ForLab8 {
	public static void main(String[] args) {
		char STAR = 'A';
		for(int i = 1; i <= 5; i++) {
			for(int j = 1; j <= i; j++) {
				System.out.print(STAR++);
			}
			System.out.println();
		}
	}
}
```

- **실습21 문제**

1. WhileLab1 라는 클래스를 생성한다.
2. 5부터 10사이의 난수를 추출한다.
3. 1부터 추출된 숫자값까지의 각 숫자들의 제곱값을 행단위로 출력한다.
   (하나의 클래스안에 for 와 while 로 각각 구현한다.)
   ===>  7이 추출되면
    [ for 결과 ]
     1 -> 1
     2 -> 4
     3 -> 9
     4 -> 16
     5 -> 25
     6 -> 36
     7 -> 49
    [ while 결과 ]
     1 -> 1
     2 -> 4
     3 -> 9
     4 -> 16
     5 -> 25
     6 -> 36
     7 -> 49

```java
// 실습21 WhileLab1
public class WhileLab1 {
	public static void main(String[] args) {
		int rand = (int)(Math.random()* 6 + 5);
		System.out.println("[for 결과]");
		for(int i = 1; i <= rand; i++) {
			System.out.println(i + " -> " + i * i);
		}
		System.out.println("[while 결과]");
		int i = 1;
		while(i <= rand) {
			System.out.println(i + " -> " + i * i);
			i++;
		}	
	}
}
```

- **실습22 문제**

1. WhileLab2 이라는 클래스를 생성한다.

2. 다음 기능을 반복해서 수행하는 프로그램을 구현하며
   반복문으로 while 문을 사용한다.

   1부터 6사이의 두개 난수를 추출하여 각각 pairNum1, pairNum2 에 저장한다.

   추출된 두 개의 숫자가 서로 다르면 값의 크기를 비교하여 
   "pairNum1이 pairNum2 보다 크다." 또는 "pairNum1이 pairNum2 보다 작다." 
   출력한다.

   추출된 두 개의 숫자가 동일하면 "게임 끝"이라는 메시지를 출력하고 종료한다.

```java
// 실습22 WhileLab2
public class WhileLab2 {
	public static void main(String[] args) {
		while (true) {
			int pairNum1 = (int) (Math.random() * 6 + 1);
			int pairNum2 = (int) (Math.random() * 6 + 1);
			if (pairNum1 != pairNum2) {
				if (pairNum1 > pairNum2) {
					System.out.println("pairNum1이 pairNum2 보다 크다.");
				} else {
					System.out.println("pairNum1이 pairNum2 보다 작다.");
				}
			} else {
				System.out.println("게임끝");
				break;
			}
		}
	}
}
```

- **실습23 문제**

[while 문으로 무한루프 처리]

1. WhileLab3 라는 클래스를 생성한다.

2. 0부터 30사이의 난수를 추출한다.
   추출된 숫자가 1이면 'A', 2 이면 'B', ... 26이면 'Z' 를 출력하는데
   계속 난수 추출과 출력을 반복하다가 난수가 0이 추출되거나
   27~30이 추출되면 반복을 끝낸다.

   반복하는 동안 출력형식 :  	B(2)
   												 A(1)
   												 D(4)
   		  										  :
   마지막에는 "수행횟수는 x 번입니다"를 출력하고 종료한다.

```java
// 실습23 WhileLab3
public class WhileTest3 {

	public static void main(String[] args) {
		int lottoNum;
		while(true) {
			lottoNum = (int)(Math.random() * 6) + 1;
			if(lottoNum == 3) {
				System.out.println("당첨!! ㅋㅋㅋ : " + lottoNum);
				break;
			}
			else {
				System.out.println("재시도!! ㅠㅠㅠ : " + lottoNum);
			}
		}
		System.out.println("수행 종료..." + lottoNum);
	}
}

```
