# Package 패키지

##### 서로 관련된 클래스와 인터페이스의 묶음.

##### 클래스가 물리적으로 클래스파일(*. class)인 것처럼, 패키지는 물리적으로 폴더이다. 

##### 패지는 서브패키지를 가질 수 있으며, '.'으로 구분한다.

##### 클래스의 실제 이름(full name)은 패키지명이 포함된 것이다. 

 ( Stringg 클래스의 full name은 java.lang.String);

##### rt.jar는 Java API의 기본 클래스들을 압축한 파일

(JDK설치경로 \jre\lib에 위치)

***한 패키지 안에서는 public은 딱 한개!!!***



# Import문

##### 사용할 클래스가 속한 패키지를 지정하는데 사용

##### import문을 사용하면 클래스를 사용할 때 패키기명을 생략할 수 있다.

~~~java
import java.util.*;
class ImportTest{
  java.util.Date today = new java.util.Date();
}
class ImportTest{
  Date today = new Date();
}
~~~

***In fact, String, Object, System, Thread는!!! import하지 않고도 사용할 수 있오***



##### e.g.) Import 문

~~~java
import java.util.Calendar;
import java.util.Date;
import java.util.Arraylist;
// = import java.util.*;

// 주의사항!!!! 
import java.util.*; 
!= 
import java.text.*;
~~~



!!!이름이 같은 클래스가 속한 두 패키지를
    import할 때는 클래스 앞에 패키지 명을 붙여줘야 한다.

~~~java
import java.sql.*;  // java.sql.Date
import java.util.*; // java.util.Date

public class ImportTest{
  public static void main(String[] args){
    java.util.Date today = new java.util.Date();
  }
}
~~~

