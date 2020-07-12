# Day 15

##### ArrayTest

```java
package day15;

import java.util.Arrays;
import java.util.List;

public class ArraysTest {

	public static void main(String[] args) {
		int[] ary = { 2, 4, 3, 7, 21, 9, 98, 76, 74 };
		System.out.printf("ary 배열 원소들 : %s\n", Arrays.toString(ary));
		System.out.printf("ary 배열 크기 : %d\n", ary.length);

		Arrays.sort(ary);
		System.out.printf("소트후 ary 배열 원소들 : %s\n", Arrays.toString(ary));

		int idx = Arrays.binarySearch(ary, 21); 
		System.out.printf("21 이라는 값이 있는 원소의 인덱스 : %d\n\n", idx);

		int[] copyOfArray = Arrays.copyOf(ary, 11); 
		System.out.printf("copyOfArray 배열 크기: %d\n", copyOfArray.length);
		System.out.printf("copyOfArray 배열 원소들 : %s\n\n", Arrays.toString(copyOfArray));

		int[] copyOfRangeArray = Arrays.copyOfRange(ary, 5, 8); 
		System.out.printf("copyOfRangeArray  배열 원소들 : %s\n\n", Arrays.toString(copyOfRangeArray));

		int[] fillArray = new int[5]; 
		System.out.printf("fillArray (before): %s\n", Arrays.toString(fillArray));
		Arrays.fill(fillArray, 1);
		System.out.printf("fillArray (after): %s\n\n", Arrays.toString(fillArray));

		Integer[] objAry = new Integer[ary.length];
		for (int i = 0; i < ary.length; i++)
			objAry[i] = ary[i];
		List<Integer> integerList = Arrays.asList(objAry); 
		System.out.printf("리스트 크기 : %d\n", integerList.size());
		System.out.printf("리스트의 원소들 : ");
		for (Integer i : integerList) {
			System.out.printf("%d ", i);
		}
	}
}

```



##### SimpleDateFormatTest

```java
package day15;

import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class SimpleDateFormatTest {

	public static String timeToStrDate(long time) {
		DateFormat formatter = 
				new SimpleDateFormat("yyyy-MM-dd");
		return formatter.format(time);
	}

	public static Date parseStrDate(String strDate) throws ParseException {
		DateFormat formatter = 
				new SimpleDateFormat("yyyy년 MM월 dd일");
		return formatter.parse(strDate);
	}

	public static void main(String[] args) throws ParseException {
		System.out.println(timeToStrDate(new Date().getTime()));
		System.out.println(parseStrDate("2019년 12월 25일")); 		
	}
}

```



### URL

##### URLTest1

```java
package day15;


import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.URL;

public class URLTest1 {
	public static void main(String[] args) throws Exception {
		URL url = new URL("https://movie.naver.com/");
		InputStream is = url.openStream();
		BufferedReader br = new BufferedReader(new InputStreamReader(is, "UTF-8"));
		String line = null;
		while (true) {
			line = br.readLine();
			if (line == null)
				break;
			System.out.println(line);
		}
	}
}

```



##### URLTest2

```java
package day15;

import java.net.*;
import java.io.*;
public class URLTest2 {
	public static void main(String[] args) {
		try {
			URL req = new URL("http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1168064000");
			InputStream is = req.openStream();
			BufferedReader reader = new BufferedReader(
					                       new InputStreamReader(is, "UTF-8"));//한국어로 만들기 위해서
			String lineStr = "";
			while(true) {
				lineStr = reader.readLine();
				if(lineStr == null)
					break;
				System.out.println(lineStr);				
			}			
		} catch (MalformedURLException e) {
			System.out.println("URL문자열 오류 : "+e.getMessage());
		} catch (IOException e) {
			System.out.println("IO 오류 : "+e.getMessage());
		}
	}
}
```

##### URLTest 3

```java
package day15;

import java.net.*;
import java.io.*;
public class URLTest3 {
	public static void main(String[] args) {
		try {
			URL req = new URL("http://img.etnews.com/news_ebuzz/afieldfile/2012/01/04/c_bk010101_87984_3.jpg");
			InputStream is = req.openStream();
			FileOutputStream fos = new FileOutputStream("c:/iotest/duke.jpg");
			int input=0;
			while(true) {
				input = is.read();
				if(input == -1)
					break;
				fos.write(input);				
			}
			fos.close();
			System.out.println("duke.jpg가 성공적으로 생성되었습니다.");
		} catch (MalformedURLException e) {
			System.out.println("URL문자열 오류 : "+e.getMessage());
		} catch (IOException e) {
			System.out.println("IO 오류 : "+e.getMessage());
		} 
	}
}

```

##### URLTest 4

```java
package day15;

import java.net.*;
import java.io.*;
public class URLTest4 {
	public static void main(String[] args) {
		InputStream is = null;
		BufferedReader reader = null;
		BufferedWriter fw = null;
		try {
			URL req = new URL("http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1168064000");
			is = req.openStream();
			reader = new BufferedReader(
					                       new InputStreamReader(is, "utf-8")); 
			fw = new BufferedWriter(new OutputStreamWriter( // OutputStereamWriter에 Data Set을 올려준 거! 
					     new FileOutputStream("c:/iotest/weather.xml"), "utf-8")); //utf 파일로 내보낼려고
			String lineStr = "";
			while(true) {
				lineStr = reader.readLine();
				if(lineStr == null)
					break;
				fw.write(lineStr+"\r\n");				
			}	
			System.out.println("weather.xml이 성공적으로 생성되었습니다.");
		} catch (MalformedURLException e) {
			System.out.println("URL문자열 오류 : "+e.getMessage());
		} catch (IOException e) {
			System.out.println("IO 오류 : "+e.getMessage());
		}  finally {
			try {
				if (fw != null) 
					fw.close();
				if (reader != null) 
					reader.close();
				if (is != null) 
					is.close();
			} catch (IOException e) {
				e.printStackTrace();
			}			
		}
	}
}
```

