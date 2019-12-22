# Day14

### [입출력 (I/O) 프로그래밍 API]

- java.io.javax.nio

- File:  시스템에 존재한느 파일에 대한 처리, 정보 추출...

- 입력용 API, 출력용 AP

- 입력단위: 바이트 단위, 문자 단위

  ​				(1.0)                  (1.1)

  ​                --------------------------> 문자단위 IO API로 꼭 변화해야 한다! 

- 스트림 이라는 논리적인 구조를 이용한다. // IO API로 만들기 위해서 이렇게 해준다. 

  입력스트림과 출력 스트림으로 구분한다.

  

- Class 이름에.... 

  - xxxInputStream, xxxOutputStream  : 바이트 스트림
  -  xxx.Reader, xxxWrtier : 문자 스트림 

- **문자스트림**

  -  FileReader, FileWriter - 파일 오픈 기능 
  - BufferReader, BufferedWriter

- **바이트스트림**

  - FileInputStream, FileOutputStream - 파일 오픈 기능
  - DataInputStream, DataOutputStream
  - ObjectInputStream, ObjectOutputStream

- InputStreamREader. OutputStreamWriter





## 정규표현식

/s  	  :  공백을 의미하는 

\* 		:  0개 이상

ab*    :   

