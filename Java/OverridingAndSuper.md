# 오버라이딩

### 오버라이딩의 조건

1. 오버라이딩의 조건1
   * 선언부가 같아야 한다. (이름/ 매개변수/ 리턴타입)

2. 오버라이딩의 조건2
   * 접근제어자를 좁은 범위로 변경할 수 없다.
   * 조상의메서드가 protected범위라면, 범위가 같거나 넓은 protected or public으로만 변경할 수 있다.

3. 오버라이딩의 조건3
   * 조상클래스의 메서드보다 많은 수의 예외를 선언할 수 없다.



##### e.g.) 오버라이딩, 오버로딩

~~~java

class Point{
	int x;
	int y;
	
	String getLocation() {
		return "x: " +x + ", y: "+ y;
	}
}

class Point3D extends Point{
	int z;
	String getLocation() {//it is called as overriding
		return "x: " +x + ", y: "+ y +", z: "+z;
  }
}
public class ClassTest2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
~~~





## 오버로딩 vs 오버라이딩

##### 오버로딩(over loading)

* 기존에 없는 새로운 메서드를 정의하는 것 (new)

##### 오버라이딩(overriding)

* 상속받은 메서드의 내용을 변경하는 것(change, modify)



### ♡오버로딩 & 오버라이딩  정리!♡

~~~java
class Parent {
  void parentMethod(){
  }
class Child extends Parents{
  void parentMethod(){} // 오버라이딩
  void parentMethod(int i){} // 오버로딩
  
  void childMethod(){} 
  void childmethod(int i){} // 오버로딩
  void childMethod() {} // 에러!! 중복정의!
}
}
~~~



# Super

#### this 

- 인스턴스 자신을 가리키는 참조변수. 인
  - 인스턴스의 주소가 저장되어 있음
  - 모든 인스턴스 메서드에 지역변수로 숨겨진 채로 존재

#### super

* this 와 같음.
  * 조상의 멤버와 자신의 멤버를 구별하는데 사용



##### e.g.) this, super

~~~java
class Parent{
  int x=10;
}

class Child extends Parent {
  int x=20l
    void method(){
    System.out.println("x="+x);
    System.out.println("this.x="+this.x);
    System.out.println("super.x="+super.x);
  }
}
~~~

~~~java
class Parent{
  int x=11;
}
class Child extends Parent {
  void method(){
    System.out.println("x= "+x);
    System.out.println("this.x= "+this.x);
    System.out.println("super.x= "+super.x);
  }
}

public static void main (String args[]){
  Child c= new Child();
  c.metohod();
}
~~~



#### Super - 조상의 생성자

* 자손클래스의 인스턴스를 생성하면, 자손의 멤버와 조상의 멤버가 합쳐진 하나의 인스턴스가 생성된다.
* 조상의 멤버들도 초기화되어야 하기 때문에 자손의 생성자의 첫 문장에서 조상의 생성자를 호출해야 한다.

~~~java
Object클래스를 제외한 모든 클래스의 생성자 첫 줄에는 생성자(같은 클래스의 다른 생성자 또는 조상의 생성자)를 호출해야한다.
  nevertheless 컴파일러가 자동적으로 'super();'를 생성자의 첫 줄에 삽입한다.
~~~

~~~java
class Point{
  int x;
  int y;
  
  Point(){
    this(0,0);
  }
  Point(int x, int y){
    this.x=x;
    this.y=y;
  }
}

.... it becomes below
  
class Point extneds Object{
  int x;
  int y;
  
  Point(){
    this.(0,0);
  }
  
  Point(int x, int y){ //<- this kind of code is calle "생성자"111
    super(); // 
    this.x=x; // object()
    this.y=y;
  }
}
~~~

~~~java
class Point{
  int x;
  int y;
  
  Point (int x, int y){
    super(); // super()을 반드시 호출!! 자동적으로 되거나 내가 해줘야지요
    this.x=x;
    this.y=y;
  }
  String getLocation(){
    return "x: "+ x+", y: "+y;
  }
}

class Point3D extends Point{
  int z;
  
  Point3D(int x, int y, int z){
    super();  //  super(x,y);
    this.x=x; //  this.z=z; 
    this.y=y; //  위 두개의 // 코드처럼 줄일 수도 있다. :)
    this.z=z; //
    
    String getLocation (){// 오버라이딩
      return "x: "+x+", y: "+ y+ ", z:"+ z;
  }
}

//이제 main으로 가쟈
class PointTest{
  public static void main(String args[]){
    Point3D p3 = new Point3D(1,2,3);
  } // IF YOU ADD'{}' 
    // at the end of Point3D p3 = new Point3D(1,2,3) 
    // THIS SHOULD BE ERRORED.
}
~~~

