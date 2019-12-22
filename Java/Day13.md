# Day13



#### Collection API : 데이터들을 저장하여 사용하는 방의 역할을 하는 API

* *Collection 클래스 : Collection API 들을 도와주는 도우미 클래스*



저장할 수 있는 데이터의 ***타입에 제한이 없***다.

저장할 수 있는 데이터의 ***갯수에 제한이 없***다.

* **List** :  저장되는 데이터의 ***순서를 유지***한다.
         :  저장되는 데이터의 ***중복을 허용***한다. 
         :  **내부적으로 복잡해서 *편집만 편*하다.**

  * **ArrayList, LinkedList, Vector**

    * 이 밑에 index에 설명된 거///

       - Type Parameters:
    
         `E` - the type of elements held in this collection
    
     
  
* **Set** : 저장되는 데이터의 ***순서를 유지하지 않***는다.

  ​      : 저장되는 데이터의 ***중복을 허용하지 않***는다. 

  * **HashSet, LikedHashSet**

  

* **Map** : 데이터 이름과 데이트 값을 쌍으로 저장한다.
           : 데이터 이름은 중복저장이 불가능하다.
          (키)

  * key-value 쌍으로 데이터 저장
  * **HashMap, Hashtable**



#### in 수업  GenericTest

```java
package day13;
import java.util.*;
public class GenericTest {
	public static void main(String[] args) {
		LinkedList list = new LinkedList(); // generist 구문을 사용해서 만들긴 했는데... type을 알려주지 않있아
		list.add("java");
        list.add("100");
		// list.add(100); // <- 이렇게 함, 오류가 된다.
//Exception in thread "main" java.lang.ClassCastException: java.lang.Integer cannot be cast to java.lang.String 
//이럴땐 try catch 해주면 된당
	at day13.GenericTest.main(GenericTest.java:16)
        // 100으로만 해도 오류가 안된다. object 이라서 cuz linkedlist로 정의하지 않아서
		list.add("servlet");
		list.add("jdbc");
		
		for(int i=0; i < list.size(); i++)
			System.out.println(list.get(i));//hashset 메서드는 추출을 할 수 없다...!!!
		System.out.println();		
		
		for(Object value : list) {// for each 문 뒤에 콜렉션 객체가 온다아
			String s = (String)value;		
			System.out.println(s);
		}
		System.out.println();		
		
		Iterator iter = list.iterator(); // this is interface
		while(iter.hasNext()){
			Object value = iter.next();
			String s = (String)value;		
			System.out.println(s);
		}
	}
}

```

### in 수업  GenericTestNew

조상에서 자손으로 갈때는 반드시 강제 형변환이 필요하다.

자손에서 조상으로 갈때는 형변환 할 필요가 없다.

```java
package day13;
import java.util.*;
public class GenericTestNew {
	public static void main(String[] args) {
		// 제네릭스 라는 구문이 적용되어 만들어진 클래스의 객체 생성시
		// 타입 파라미터라는 것을 사용한다. 
		LinkedList<String> list = new LinkedList<String>();  // 타입파라미터
        //<String>  라고 부른다.
		list.add("java");
		list.add("100"); 
		list.add("servlet");
		list.add("jdbc");
		
		for(int i=0; i < list.size(); i++)
			System.out.println(list.get(i));
		System.out.println();		
		
		for(String value : list) {			
			System.out.println(value);
		}
		System.out.println();
		
		Iterator<String> iter = list.iterator();
		while(iter.hasNext()){
			String s = iter.next();			
			System.out.println(s);
		}
	}
}


```

### ===> Generics 구문은 그래서

처리하는 객체에 대해서 견고하는 프로그램을 지원하고 

형변환에 있어서 자유롭다.





### 자료구조 클래스의 사용 방법

#### Array List

```java
ArrayList<String>list = new ArrayList<String>();

list.add("포도");                 호출 순서대로 데이터가 저장됩니다.

String st=list.get(2);          인덱스 2 위치에 있는 것을 리턴한다.

int num = list.size();          리스트에 있는 데이터의 수를 리턴합니다.

list.add(2, "키위");             인덱스 2 위치에 "키위"를 삽입합니다.
 
list.set(0, "오렌지");           인덱스 0 위치에 있는 데이터를 "오렌지"로 바꿉니다.

list.remove(1);                 인덱스 1위치에 있는 데이터를 삭제합니다.

list.remove("키위");            인덱스 "키위"를 데이터를 삭제합니다.
```



```java
int index = list.index()Of("사과");     //일치하는 것들이 없으면 -1를 리턴한다.
int index = list.lastIndexOf("사과");   // 마지막 "사과"의 위치를 리턴한다.

```



### Linked List

 부모가 list 이다.

arraylist랑 사용되는 것들은 동일하다.

```java
LinkedList<String>list = new  LinkedList<String>();

list.add("포도") ; 처음으로 add 메소드 호출하면 그 데이터가 저장된다.
list.add("딸기") ; add 메소드를 또 호출하면 마지막 데이터와 서로 가리키는 식으로 저장됩니다.
list.add("복숭아") ; add 메소드를 또 호출하면 마지막 데이터와 서로 가리키는 식으로 저장.

String str = list.get(2);    인덱스 2위치에 있는 "키위"를 리턴합니다.
list.add (2, "키위");         인덱스 2 위치에 "키위"를 삽입합니다.
list.remove(1);              인덱스 1위치에 있는 데이터를 삭제합니다.

 
Iterator<String>iterator = list.iterator();
String str= iterator.next();     // next메소드가 더 이상 데이터가 없으면
								// NoSuchElementException을 발생합니다.
    
    
for(String str: list){
    //반복 실행부분
}
    

**데이터 순차 접근을 효율적을 하는 방법
    
```



### STACK (스택)

: 데이터를 넣은 순서의 역순으로만 꺼낼 수 있는 자료 구조

: 스택으로 사용할 수 있는 클래스 : **LinkedList** 클래스



```java
LinkedList<Integer>stack = new LinkedList<Integer>();
list.addLast(new Integer(12));
list.addLast(new Integer(59));
list.addLast(new Integer(7)); // 먼저 들어온 메소르를 제일 바닦에 저장한다.
			// 타입 파라미터에 해당하는 데이터를 넘겨주엉 한다.

//<데이터 제거하지 않고 꺼내는 방법>
Integer obj = getLast(); //  스택의 제일 위에 있는 것을 리턴한다.
//더 작성해야 한다.


```



### Que (큐)



## 

:

```

```

### HashSet 클래스

```java
HashSet<String> set= new HashSet<String>();
set.add("자바"); // 데이터들의 순서를 저장하지 않는다.
int num=set.size(); // 집합에 있는 데이터의 수를 리턴한다.

Iterator<String> iterator = set.iterator();
while (iterator.hasNext()){
    String str = iterator.next();
    //데이터 처리 부분
}

//들어온 데이터 내용이 똑같으면 false....
```



### 실습 나 틀린거

```java
package day13;
import java.util.*;
public class LottoMachine2 {

	public static void main(String[] args) {
		HashSet<Object> lotto = new HashSet<Object>();
		int num[]= new int[10];
		int rand1 = (int)Math.random()*30+1;
		for(int i=0;i<10;i++) {
			num[i]=rand1;
			lotto.add(rand1);
		}
		System.out.print("[");
//		for(int i=0;i<num.length;i++) {
//			lo.add("num[i]");
//		}
		Iterator put = lotto.iterator();
		while (put.hasNext()) {
			System.out.print(put.next()+ " ");
		}
//		Iterator<Object>iterator = lotto.iterator();
//		while (iterator.hasNext()) {
//			System.out.print(iterator.next()+ " ");
//		}
		System.out.print("]");
	}
}
```



### 실습  정답 1)  Iterator 안쓴거

```java
package day13;
import java.util.*;
public class LottoMachine2 {

	public static void main(String[] args) {
		HashSet<Integer> lotto = new HashSet<Integer>();
		Random rand = new Random();
		while(lotto.size()!=10) {
			lotto.add(rand.nextInt(30)+1);
		}
		 System.out.print("오늘의 로또 번호 : " + lotto);
//		
//		Iterator<Integer> iter = lotto.iterator();
//		System.out.printf("오늘의 로또 번호: [%d",iter.next());
//		
	}
}
```

### 실습 정답2)  Iterator  쓴거

```Java
package day13;
import java.util.*;
public class LottoSeon {

	public static void main(String[] args) {
		HashSet<Integer> set = new HashSet<Integer>();
		Random rand = new Random();
		while(set.size() != 10) {
			set.add(rand.nextInt(30) + 1);	
		}
		Iterator<Integer> iter = set.iterator();
		System.out.printf("오늘의 로또 번호 : [%d", iter.next());
		while(iter.hasNext()) {
			int temp = iter.next();
			System.out.printf(", %d", temp);
		}
		System.out.print("]");
    }
}
```



## 해쉬 테이블

* 해쉬 테이블로 사용할 수 있는 클래스 : HashMap 클래스
* 해쉬 테이블 생성 방법

```java
HashMap<Strng, Integer> hashtable = new HashMap<String, Integer>;
    // 키의 타입 데이터의 타입을 두가지 줘야 한다. // 키의 타입 데이터의 타입을 두가지 줘야 한다.

```

* 100개의 통으로 구성된 해쉬 테이블 생성하기

  ```java
  HashMap<String, Integer> hashtable = new HashMap<String, Integer>(100);
  											// 100개의 토으로 구성된 해쉬 테이블을 생성한다.
  hashtable.put("해리", newInteger(95));
  // 키 값("해리")으로 통 번호(5)를 계산하여 그 통에 키 값과 데이터를 넣습니다. 
  
  Integer num = hashtable.get("해리"); // "해리" 는 키값
  // 키 값으로 통 번호를 계산하고, 그 통 안에서 키 값과 일치하는 데이터를 찾아서 리턴합니다.
  리턴리턴리턴리턴리턴리턴리턴리턴리턴리턴리턴리턴리턴!!!!!!!!!!!!!
  
  hashtable.remove("해리");
  //키 값으로 통 번호를 계산하고 해당 통에서 키 값과 일치하는 데이터를 찾아서 삭제합니다.
  // 다 모여 있다는 것을 알고 있는 것이 hash algorithm 이라고 한다!!!!
  // hashmap이라는 애가 다 찾아서 해주는 거얌
  ```

  * 오후 첫번째 실습 HashMapLab1 (내 정답 오답)

```java
package day13;
import java.util.Scanner;
import java.util. *;

public class HashMapLab1 {

	public static void main(String[] args) {
		HashMap<String, Integer> hashTable = new HashMap<String, Integer>(5);
		
		Scanner sc = new Scanner(System.in);
		String country;
		int population;
		
		for (int i=0; i<5;i++) {
			System.out.print("나라이름을 입력하세요 : ");
			country = sc.next();
			System.out.print("인구 수를 입력하세요 : ");
			population = sc.nextInt();
			
			if(hashTable.containsKey(country)==true){
				System.out.println("나라명 "+country+"는 이미 저장되어있습니다.");
				i=i-1;
			}	
			else if (hashTable.containsKey(country)==false){
				hashTable.put(country, new Integer(i));
				System.out.println("저장되었습니다.");
			}
			
			if (i==4) {
				System.out.println("5개가 모두 입력되었습니다. \n 입력된 데이터: ");
			}
		}
		Set<String> keySet = hashTable.keySet(); // keySet = key의 리턴값들만 모아둘거다. 키는 키대로 발류는 발류대로
		Iterator<String> iterKey = keySet.iterator();
		while (iterKey.hasNext()) {
			String key = iterKey.next();
			System.out.print(key+"("+hashTable.get(key)+")");
			
		}
 
//		  5개가 모두 입력되었습니다.
//		  입력된 데이터 : XX(nn), XX(nn)....
//
	}
}

```

* 오후 첫번째 실습 HashMapLab1 (모범답안)

```java
package day13;
import java.util.Scanner;
import java.util. *;

public class HashMapLab1 {

	public static void main(String[] args) {
		HashMap<String, Integer> hashTable = new HashMap<String, Integer>(5);
		
		Scanner sc = new Scanner(System.in);
		String country;
		int population;
		
		for (int i=0; i<5;i++) {
			System.out.print("나라이름을 입력하세요 : ");
			country = sc.next();
			System.out.print("인구 수를 입력하세요 : ");
			population = sc.nextInt();
			
			if(hashTable.containsKey(country)==true){
				System.out.println("나라명 "+country+"는 이미 저장되어있습니다.");
				i=i-1;
			}	
			else if (hashTable.containsKey(country)==false){
				hashTable.put(country, new Integer(i));
				System.out.println("저장되었습니다.");
			}
			if (i==4) {
				System.out.println("5개가 모두 입력되었습니다. \n 입력된 데이터: ");
			}
		}
		
		Iterator<String> it =hashTable.keySet().iterator();
		
		int value=0;

		while(true) {
			country=it.next();
			value=hashTable.get(country);
			System.out.printf("%s(%d)", country, value);
			if(it.hasNext()) System.out.print(",");
			else break;

	}

}
```

* 오후 두번째 실습 (내 정답 오답)

  ```java
  package day13;
  
  import java.util.*;
  
  class CreateList {
  	ArrayList<Integer> arrayList = new ArrayList<Integer>();
  
  	public ArrayList<Integer> convertList(int array[]) {
  		for(int ii=0;ii<array.length;ii++) 
  			arrayList.add(array[ii]);
  		
  		int num = arrayList.size();
  		for (int i = num; i > 0; i--) 
  			System.out.println(array[i]);
  			return arrayList;
  
  	}
  }
  
  public class ListTest {
  
  	public static void main(String[] args) {
  		CreateList createList = new CreateList();
  		int array[]= {3,4,2,5,2,3,6,7,5,7,9};
  		createList.convertList(array); // 클래스 객체를 써서  접근을 하거야!! 
  		
  		for (int ij=array.length;ij>0;ij--) {
  			System.out.println(arrayz);
  		}
  		
  	}
  
  }
  ```

*  오후 두번째 실습 (모범답안)

  ```java
  ???
  ```

  