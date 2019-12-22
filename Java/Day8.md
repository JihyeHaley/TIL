# Day8



### static(정적, 고정)

* 제어자
* 멤버변수와 메서드 앞에 지정 가능하다.
* static을 설정한 멤버변수와 메서드는 객체생성을 하지 않아도 자동으로 메모리 영역을 할당하거나 호출 가능한 상태가 된다.
* 다른 클래스에서 또 다른 클래스의 static 타입의 멤버를 사용할 때는 
  **클래스명.멤버명**
* 클래스에 정의되는 멤버들중 어떤 멤버에  static 부여 하는가?
* verbose:class : JVM 옵션
  클래스 로딩 정보를 보여주면서 자바 프로그램을 수행시켜라!!



### 블록 스코프

```Java
 메서드 헤더 {
     int a;
     //int b;
     if(...){
          int b;
         :
     }
     //블록을 벗어나는 변수는 더이상 사용될 수 없다.
     int c;
     int b;
   
	}
```



## JVM의 메모리 구조

### 메서드 영역ㅓ

* 클래스 정보와 클래스 변수가 저장되는 곳



### 호출스택

* 메서드의 작업공간. 메서드가 호출되면 메서드 수행에 필요한 메모리공간을 할당받고 메서드가 종료되면 사용하던 메모리를 반환한다.



### 힙

* 인스턴스가 생성되는 공간. new연산자에 의해서 생성되는 배열과 객체는 모두 여기에 생성된다.



## 재귀 호출

* ㅇㄹ
* ㅘ



## 클래스메서드(static 메서드)와 인스턴스메서드

* **인스턴스 메서드**

  - 인스턴스 생성 후, '참조변수.메서드이름()'으로 호출

  * 인스턴스변수나 인스턴스메서드와 관련된 작업을 하는 메서드
  * 메서드 내에서 인스턴스변수 사용 가능

* **인스턴스 메서드**
  * 객체생성없이 '클래스이름.메서드이름()'으로  호출
  * 인스턴스변수나 인스턴스메서드와 관련없는 작업을 하는 메서드
  * 메서드 내에서 인스턴스변수 사용불가
  * 메서드 내에서 인스턴스변수를 사용하지 않는다면 static을 붙이는 것을 고려한다.



``` Java
class MyMath2 {
	long a, b;// non static 멤버변수 사용 안함.
	
	long add() {	// 인스턴스메서드
		return a + b; // non static 사용
	}

	static long add(long a, long b) { // 클래스메서드(static메서드)
		return a + b;
	}
}
// argu 없으면 객체생성해서 변수에 담아서 변수.method로 해야한다.
```



``` Java
class MyMathTest2 {
	public static void main(String args[]) {
		System.out.println(MyMath2.add(200L,100L); // 클래스메서드 호출
		MyMath2 mm = new MyMath2(); // 인스턴스 생성
		mm.a = 200L;
		mm.b = 100L;
		System.out.println(mm.add()); // 인스턴스메서드 호출
	}
}
```



### 표준입력 (Standard Inupt)

* 포그램이 수행하는 동안 필요로 하는 데이터를 시스템의 표준 입력장치로부터 받아오는 것
  **표준 입력 장치 -  키보드**
  **~~표준 출력 장치 - 모니터~~**

  

* Java에서는 표준입력을 어떻게 처리 하느냐 ...

  * **System.in**
  * **System.in.read()**

  Java 5 (JDK 1.5)

  java.util.Scanner 클래스 제공하여 좀 더 편하게 데이터를 입력받을 수 있게  **API**를 추가했다.

​			Scanner scan = new Scanner(System.in);

​			scan.next()            

​			scan.nextLine()	<- 한 행을 읽어오는 것

​			scan.nextInt()       <- 

​			scan.nextDouble()

**ScannerTest1: 한 행에만 입력**

```java
package day8;
import java.util.Scanner;
public class ScannerTest2 {
	public static void main(String[] args) {
		System.out.print("입력 : ");
		Scanner sc = new Scanner(System.in);
		String a,b,c,d;
		a = sc.nextLine();
		b = sc.nextLine();
		c = sc.nextLine();
		d = sc.nextLine();
		System.out.println("a = [" + a + "]");
		System.out.println("b = [" + b+ "]");
		System.out.println("c = [" + c+ "]");
		System.out.println("d = [" + d+ "]");	
		sc.close();
	}
}
**ScannerTest1: 한 행에만 입력**
```

**ScannerTest2: 한 행과 열에 입력**

```java
package day8;
import java.util.Scanner;
public class ScannerTest1 {
	public static void main(String[] args) {
		System.out.print("입력 : ");
		Scanner sc = new Scanner(System.in);
		String a,b,c,d;
		a = sc.next();
		b = sc.next();
		c = sc.next();
		d = sc.next();
		System.out.println("a = [" + a + "]");
		System.out.println("b = [" + b+ "]");
		System.out.println("c = [" + c+ "]");
		System.out.println("d = [" + d+ "]");
		sc.close();
	}
}
```

**ScannerTest3: 정수 2개, 실수 2개 덧셈**

```java
package day8;
import java.util.Scanner;
public class ScannerTest3 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("두 개의 숫자(정수)를 입력해 주세요 : ");
		int number1 = sc.nextInt();
		int number2 = sc.nextInt();
		System.out.printf("합 : %d%n", number1 + number2);// \n
		System.out.print("두 개의 숫자(실수)를 입력해 주세요 : ");
		double number3 = sc.nextDouble();
		double number4 = sc.nextDouble();
		System.out.printf("합 : %.2f%n", number3 + number4);
		sc.close();
	}
}
```

* **cf.** 

   입력해야하는 형태가 안나왔을 때 나오는 오류 (친해져야 함!)

  ```java
  Exception in thread "main" java.util.InputMismatchException
  	at java.util.Scanner.throwFor(Scanner.java:864)
  	at java.util.Scanner.next(Scanner.java:1485)
  	at java.util.Scanner.nextInt(Scanner.java:2117)
  	at java.util.Scanner.nextInt(Scanner.java:2076)
  	at day8.ScannerTest3.main(ScannerTest3.java:7)
  ```

  

**ScannerTest4: 4개 받기**

```java
package day8;
import java.util.Scanner;
public class ScannerTest4 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.printf("데이터를 입력하세요 : ");
		String str1 = sc.next();
		String str2 = sc.next();
		sc.nextLine();  // 입력버퍼에 남아있는 개행문자를 청소하는 기능
		String line1 = sc.nextLine();
		String line2 = sc.nextLine();
		System.out.printf("[%s] [%s] [%s] [%s]", str1, str2, line1, line2);
		sc.close();
	}
}
```



## 상속구문

* (멤버가 없어도 class를 만들 수 있다.)

* **java.lang.Object ;**
  자동으로 부모는 Object이 된다. Object에 있는 것들을 물려받음

  

  * ```java
    class Parent{ //java.lang.Object
        public String toString(){
            return "Parent 클래스의 객체 입니다";
        }
    }
    ```

  * ```java
    class Child extends Parent{
    	public String toString() {
    		return "Child 클래스의 객체입니다";
    	} /// extends 는 Child가 Parents를  부모로 받는 다는 뜻!
          // 부모에 toString이 있따!
    
    }
    ```

  * ```
    
    ```

  * 

* **super**
  조상 객체를 쓰는 아이!

* **toString()**;
  호출을 하면 엄마를 자동 도출

* **java.util.Date d=new java. util.Date();**
  import문을 대신할 수 있다.

  

  