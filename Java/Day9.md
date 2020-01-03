# Day 9



## [상속]

* 자바의 모든 객체들은 상속이라는 객체지향언어의 특징을 지원한다.
* 자바에서 생상되는 모든 객체들은 기본적으로 java.lagn.Object 이라는 객체를 상속하게 된다.
* 클래스 헤더에 exetdns 라는 절을 사용하는 부모 클래스를 설정하는데 하나의 부모 클래스만 설정 가능하다.
* 조상부터 물려받은 메서드들은 필요에 따라 대체할 수 있따. 
  ***메서드 오버라이딩*** 이라고 한다.
* 어떤 클래스든 객체를 생성하여 해당 클래스만 메모리 할당하는 것이 아니라 조상 클래스들도 메모리를 할당한다.
* 자손클래스의 객체 생성시 메서드가 호출되면 바로 조상 클래스의 생성자도 호출된다. 
* 내부적으로 아규먼트 없는 생성자가 호출되는데 다른 생성자를 호출하려는 경우 
  *super()*라는 메서드를 사용한다.
* 객체를 참조하는 용도 : this, super
* 객체를 초기화하는 용도로 사용되는 생성자 메서드 호출에 : this(), super()
* this(), super() : 생성자 안에서만 호출 가능
* this, super: 객체 생성 시점에 초기화 된다.
                       static 메서드에서는 사용 불가하다.
                       non-static 메서드와 생성자 메서드에서만 사용 가능하다.

**Example)**

```java
package day9;
class A{
	A(){
		System.out.println("A 클래스를 객체로 생성합니다.");
	}
}
class B extends A{
	B(){
		System.out.println("B 클래스를 객체로 생성합니다.");
	}
}
class C extends B{
	C(){
		System.out.println("C 클래스를 객체로 생성합니다.");
	}
}
public class ABCTest {
	public static void main(String[] args) {
		new C ();
	}
}
```

Typically, except Object
호출되면 항상 조상 생성자부터 호출하고 내려온다.
***조상의 객체생성(초기화 하는 것까지가)을 먼저 해놓고 자손 객채생성을 해야한다.***

```java
class B extends A{
	B(int num){
///**Multiple markers at this line**(오류) C애서 오류가 난다.
/// - Syntax error on token ")", { expected after this token
/// - Implicit super constructor B() is undefined. Must explicitly invoke another 
    /// constructor
		System.out.println("B 클래스를 객체로 생성합니다.");
	}
}
public class C extends B{
	C(){
        super(100); // super 메소드를 꼭 사용해야 한다.
		System.out.println("C 클래스를 객체로 생성합니다.");
	}
}
```

#### The role of Compiler

* 생성자 없는 메소드는 생성자를 채워줬다

* 부모 지정하지 않은 애들은 java.lang.object를 자동으로 부모로 저장해주는

* 패키지명을 붙여주는 

* JAVA SOURCE를 읽고 자바 실행파일로 번역하는것

* Java의 파일은 byte code라고 말한당

  ***=>있어야 하는데 없는걸 채우는 역할을 하는 것이 Compiler!1***

  



## [제어자]

### = modifier(수정자, 한정자, 제어자)

* **접근 제어자: ** public, protected, (default), private

* **활용 제어자: ** final, static, abstract, transient, synchronized ..... (사용 방법을 제어하는 것)

  제어자란 클래스, 메서드, 변수앞에 설정되어 접근 가능 여부와 사용 방식을 제어하는 구문!! 

  ```java
  class 클래스명 extends 부모클래스명 {
      [제어자] 멤버변수 선언;
      
      [제어자] 생성자 메서드;
      
      [제어자] 메서드 정의
  }
  
  public, final, abstract class 클래스명 extends 부모클래스명{
      모든 접근제어자, final, static 멤버변수 선언
          모든 접근제어자->[제어자]생성자 메서드 정의
          
          모든 접근제어자, static, final, abstract ->[제어자]메서드 정의
  		변수일때 다 똑같다아
  }
  
  - 클래스에는 접근 제어자를 두 가지만 설정 가능: public, (default)
      public이 설정된 클래스 : 누구나
      (deafult) 클래스 : 동일 패키지의 클래스만 
  - final = 변경할 수 없는, 마지막의
  - abstract = 반드시 변경해야하는, 마지막 아닌, 미완성의
     => 제어자로서의 final 과 abstract은 반대다!!!)
          
  ex...!!!!!!!
  - final 클래스 = 상속 불가, 객체 생성 가능!
  - abstract 클래스 = 상속만 가능! 객체 생성 불가능!
          
  - public
    protected
    (deafult) - 동일 패키지 이어야만 접근 가능하다
    private - 자손이든 객체 생성한 클래스든 접근 불가
          	멤버가 정의된 클래스 내에서만 사용 가능
  ```

public이 안 붙어 있으면 동일 *패키지*에서만 사용 가능! 
깥은 패키지가 아니면 사용 불가 완전 불가

#### 	멤버변수 제어자

* **+:         public**

* **#:          protected**

* **(),~:       (default)**

* **-:           private**

- **sttatic, final을 함께 지정하여 상수를 만든다 **

  ```java
  pulblic class Math{
      public final static double PI=3.14159;
  	//public 이랑 final static 이랑 순서가 바껴도 괜찮당 
  }
  //멤버 변수인데 상수 중에 static으로 되어 있는 것들이 많다.
  
  Math.PI  
  Integer.MAX_VALUE
      // -메서드에
      //final :자손에 의해 오버라이딩이 불가능한 메서드를 정의하게된다
  	//abstract :자손에 의해 반드시 오버라이딩 해야 하는 메서드를 정의 
      			메서드의 헤더만 정의되고, 바디가 없는 메서드를 뜻한다.
      
  ```

  