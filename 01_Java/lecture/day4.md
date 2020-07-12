# Day4

[자바의 산술 이항 연산의 특징] - 교재 92 페이지

   (1) int 타입보다 작은 타입들(byte, short, char)은 int 타입으로 변환하여 연산
   (2) 두 항의 타입이 다를 때 하나로 일치해서 연산(표현 범위가 적은 타입에서 큰타입으로)

```java
    표현 범위의 관계 : int < long < float < double
```

[배열: array]

- 동일한 타입의 데이터들의 집합

- 배열을 만드는 방법

- 배열을 사용하는 방법

- 여러개의 데이터들을 프로그램에서 다뤄야 할 때 변수를 여러개 선언하여 사용하는 것은 비효율적이다. (코딩, 수행)

- 배열을 만드는 방법

  - 배열로 구성하려는 데이터들의 타입
  - 배열로 구성하려는 데이터들의 최대 갯수

  new 데이타타입[크기]

  ```java
  new int [10] --------- 0
  new char [26] ------- '\u0000'
  new double [5] ----- 0.0
  new long [1]    ----- 0L
  new boolean[10] --- false
  
  {값1, 값2, 값3 ...}
  {10,20,30}, {4,1,5,7,8,1,3}, {'a', 'b', 'c'), {true}
  ```

- 배열을 사용하는 방법
  배열을 사용하기 위해서는 배열을 만든 다음 변수에 담는다.
  배열변수가 필요하다.

```java
타입[] 변수명; 타입 변수명 [];
	int a1[]; int[] a2' char[] a3; boolean a4[];
	
	int a1[] = new int [10];
	int a2[] = {10, 20,30};

	a1[0], a1[1], a2[1].........a1[9]

	배열변수명 [인덱스] // 인덱스는 0부터 지정
	배열을 구성하는 데이터들 : " 엘리먼트(element)", 요수, 원소
	배열변수.length : 배열변수 대입된 배열의 요소갯수
	
	System.out.println(a1[0]);
	System.out.println(a1[1]);
	System.out.println(a1[2]);

	System.out.println(a1[9]);

	a1[0] = 1000;
	a1[1] = 999;
	a1[9] += 10;

	for (int i=0;i<a1.length: i++)
        System.out.println(a1[i]);
```

```java
// 실습1 CharacterTest1
public class CharacterTest1 {
	public static void main(String[] args) {
		char v1 = 65;
		char v2 = 'A';
		char v3 = 0x41; // 영(공)엑스
		char v4 = '\u0041'; // 유니코드
		System.out.println((char)(v1+1)); // 형변환 (타입명)
		System.out.println((char)(v2+1));
		System.out.println((char)(v3+1));
		System.out.println((char)(v4+1));
		
		System.out.println();
		System.out.println((++v1)); // 형변환 (타입명)
		System.out.println((++v2));
		System.out.println((++v3));
		System.out.println((++v4));
		
		System.out.println();
		System.out.println((v1+=1)); // 형변환 (타입명)
		System.out.println((v2+=1));
		System.out.println((v3+=1));
		System.out.println((v4+=1));
		
		System.out.println();
		int v5 = 65;
		int v6 = 'A';
		int v7 = 0x41;
		int v8 = '\u0041';
		System.out.println(v5);
		System.out.println(v6);
		System.out.println(v7);
		System.out.println(v8);
	}
}
```

```java
// 실습2 ArrayTest1_1
//foreach
public class ArrayTest1_1 {

	public static void main(String[] args) {
		int a1[] = new int[10];
		System.out.println(a1.length);
		int a2[] = {10, 20, 30};
		System.out.println(a2.length);
		
		//System.out.println();
		for(int i = 0; i < a1.length; i++) {
			System.out.print(a1[i] + " ");
		}
		System.out.println();
		for(int data : a1) {
			System.out.print(data + " ");
		}
		System.out.println();
		for(int i = 0; i < a2.length; i++) {
			System.out.print(a2[i] + " ");
		}
		System.out.println();
		for(int data : a2) {
			System.out.print(data + " ");
		}
		System.out.println();
		
		for(int i = 0; i < a1.length; i++) {
			a1[i] = (i + 1) * 100;
		}
		System.out.println();
		for(int i = 0; i < a1.length; i++) {
			System.out.print(a1[i] + " ");
		}
		System.out.println();
		for(int data : a1)
			System.out.print(data + " ");
		System.out.println();
//		a2[3] = 100;

	}
}
```

```java
// 실습3 ArrayTest1
public class ArrayTest1 {

	public static void main(String[] args) {
		int a1[] = new int[10];
		System.out.println(a1.length);
		int a2[] = {10, 20, 30};
		System.out.println(a2.length);
		
		//System.out.println();
		for(int i = 0; i < a1.length; i++) {
			System.out.print(a1[i] + " ");
		}
		System.out.println();
		for(int i = 0; i < a2.length; i++) {
			System.out.print(a2[i] + " ");
		}
		
		for(int i = 0; i < a1.length; i++) {
			a1[i] = (i + 1) * 100;
		}
		System.out.println();
		for(int i = 0; i < a1.length; i++) {
			System.out.print(a1[i] + " ");
		}
//		a2[3] = 100;
	}
}
```

```java
// 실습4 ArrayTest2
public class ArrayTest2 {

	public static void main(String[] args) {
		int a1[] = new int[5];
		a1[0] = 33;
		a1[1] = 20;
		a1[2] = 15;
		a1[3] = 40;
		a1[4] = 7;
		System.out.println(a1[0]);
		System.out.println(a1[a1.length - 1]);
		
		for(int i = a1.length-1; i>= 0; i--) {
			System.out.print(a1[i] + " ");
		}
		System.out.println();
		
		for(int i = 0; i < a1.length; i+=2) {
			System.out.print(a1[i] + " ");
		}
		System.out.println();
	}
}
```

```java
// 실습5 ArrayTest3
public class ArrayTest3 {

	public static void main(String[] args) {
		int a1[] = {3, 10, 2, 9, 5, 11, 12, 1};
		int max;
		// a1 배열변수에 할당된 배열의 요소중 최댓값
		max = a1[0];
		for(int i = 1; i < a1.length; i++) {
			if(a1[i] > max) {
				max = a1[i];
			}
		}
		System.out.println("최댓값 : " + max);
		int min;
		// a1 배열변수에 할당된 배열의 요소중 최솟값
		min = a1[0];
		for(int i = 1; i < a1.length; i++) {
			if(a1[i] < min) {
				min = a1[i];
			}
		}
		System.out.println("최솟값 : " + min);
	}
}
```

```java
// 실습6 ArrayTest4
public class ArrayTest4 {

	public static void main(String[] args) {
		int a1[] = {3, 10, 2, 9, 5, 11, 12, 1};
		
		// a1 배열변수에 할당된 배열의 요소중 최댓값
		
		for(int i = 0; i < a1.length; i+=2) {
			System.out.println(a1[i] + " ");
		}
			System.out.println();
	}
}
```

```java
// 실습7 BreakTest
public class BreakTest {

	public static void main(String[] args) {
		//boolean flag = false;
		done: for(int dan = 1; dan <= 9; dan++) {
			for(int num = 1; num <= 9; num++) {
				if(dan*num > 30) {
					//flag = true;
					break done;
				}
				System.out.print(dan+"x"+num+"="+dan*num+"\t");
			}
			System.out.println();
			//if(flag == true) break;
		}
	}
}
```

- **실습8 문제**

1. ArrayLab1 이라는 클래스를 하나 만든다.
2. ary 라는 int 타입의 배열 변수를 선언하고 10개의 엘리먼트를 갖는 배열을 생성하여 대입한다.
3. 배열의 값들을 하나의 행에 다음 형식으로 출력한다.
   0 0 0 0 0 0 0 0 0 0
4. 생성된 배열에 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 을 각각의 element 로 저장한다.
5. 배열의 값들을 하나의 행에 다음 형식으로 출력한다.
   10 20 30 40 50 60 70 80 90 100
6. 배열의 값들을 하나의 행에 다음 형식으로 출력한다.
   100 90 80 70 60 50 40 30 20 10
7. 배열의 값들을 하나의 행에 다음 형식으로 출력한다.
   20 40 60 80 100

```java
// 실습8 ArrayLab1
public class ArrayLab1 {

	public static void main(String[] args) {
		int ary[] = new int[10];
		for(int i = 0; i < 10; i++) {
			System.out.print(ary[i] + " ");
		}
		System.out.println();
		for(int i = 0; i < 10; i++) {
			ary[i] = (i + 1) * 10;
		}
		for(int i = 0; i < 10; i++) {
			System.out.print(ary[i] + " ");
		}
		System.out.println();
		for(int i = 9; i >= 0; i--) {
			System.out.print(ary[i] + " ");
		}
		System.out.println();
		for(int i = 1; i < 10; i+=2) {
			System.out.print(ary[i] + " ");
		}
	}
}
```

- **실습8 문제**

1. ArrayLab2 라는 클래스를 하나 만든다.

2. 10개의 숫자(정수)를 저장할 수 있는 배열을 하나 만든다.

3. 각각의 원소에  4부터 20사이의 난수를 추출하여 저장한다.

4. 모든 원소의 합을 구한다.

5. 다음과 같은 형식으로 출력한다.

   모든 원소의 값 : x,x,x,x,x,x,x,x,x,x
   모든 원소의 합 : x

```java
// 실습9 ArrayLab2
public class ArrayLab2 {
	public static void main(String[] args) {
		int arr[] = new int[10];
		int rand;
		int sum = 0;
		System.out.print("모든 원소의 값  : ");
		for(int i = 0; i < 10; i++) {
			rand = (int)(Math.random()*17 + 4);
			arr[i] = rand; 
			System.out.print(arr[i]);
			if(i == 9) break;
			System.out.print(", ");
		}
		System.out.println();
		for(int i = 0; i < 10; i++) {
			sum += arr[i];
		}
		System.out.println("모든 원소의 합  : " + sum);
	}
}

```

- **실습10 문제**

1. ArrayLab3 라는 클래스를 하나 만든다.

2. 'J', 'a', 'v', 'a' 라는 원소들로 구성되는 char 타입의 배열을
   만든다.

3. 각 원소들의 값에서 대문자는 소문자로 소문자는 대문자로 
   변환한다.

4. 수행 결과 :

   변환된 배열 : j,A,V,A

```java
// 실습10 ArrayLab3
public class ArrayLab3 {

	public static void main(String[] args) {
		char arr[] = {'J', 'a', 'v', 'a'};
		
		for(int i = 0 ; i < arr.length; i++) {
			if(arr[i] >= 'a' && arr[i] <= 'z') {
				arr[i] -=32;
			}
			else if(arr[i] >= 'A' && arr[i] <= 'Z') {
				arr[i] +=32;
			}
		}
		
		System.out.print("변환된 배열 : ");
		for(int i = 0; i < arr.length; i++) {
			if(i != arr.length - 1) System.out.print(arr[i] + ", ");
			else System.out.println(arr[i]);
		}
	}
}
```

- **실습11 문제**

1. ArrayLab4 이라는 클래스를 하나 만든다.

2. 10 개의 원소를 갖는 int 타입의 배열을 생성한 후에 이 배열의 
   각각의 원소값으로 1부터 26 사이의 난수를 추출하여 저장한다.

3. 10개의 원소를 갖는 char 타입의 배열을 생성한다.

4. 2번에서 생성한 배열의 각각의 원소값의 3번에서 생성한 배열의
   원소값으로 저장하는데 이 때는 
   1이면 'A', 2 이면 'B', ... 26이면 'Z'를 저장한다.

5. 두 배열의 원소값을 다음과 같이 출력한다.

   10,1,3,21,6,8,11,26,22,19
   J,A,C,U,F,H,K,Z,V,S

```java
// 실습11 ArrayLab4
public class ArrayLab4 {
	public static void main(String[] args) {
		int arr[] = new int[10];
		char arrChar[] = new char[10];
		for(int i = 0; i < 10; i++) {
			arr[i] = (int)(Math.random()*26 + 1);
			if(i != 9) System.out.print(arr[i] + ", ");
			else System.out.print(arr[i]);
		}
		
		System.out.println();
		for(int i = 0; i < 10; i++) {
			arrChar[i] = (char)(arr[i] + '@');
			if(i != 9) System.out.print(arrChar[i] + ", ");
			else System.out.print(arrChar[i]);
		}
	}
}
```
