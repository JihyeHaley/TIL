### [4/28일 수업 내용 순서]

1. IP 주소 고정  [이것이 리눅스다]  p 117  step4
2. JDK 1.8 설치 . 
3. Eclipse 설치
4. Tomcat 설치



----------------------------------------------------------------------------------

[IP주소 고정시키기]

1. VMWare , m1 , root로 로그인(root, password)

2. 터미널 키기

3. whoami 명령어 수행 : 어떤 계정인지 알랴줌

4. date 명령어 : 현재 시간정보 보여줌

5. pwd  : /home 밑에 아이디 명으로 보여줌... root 계정은, /root  

6. ls

7. ifconfig  :  현재 부여된 아이피 주소 확인 -----> 이 아이피 주소 개인마다 다름.  고정되어 있는 것이 아니다

   =======> 이것을 고정 시키고자 함 !

   

   eno16777728 : 네트 워크 카드에 부여되는 이름 (p 118  , 여기서 잠깐 참조!)

8.  cd /etc/sysconfig/network-scripts/

9. pwd

10. ls

    ----------------------------->ifcfg-eno16777728  파일 열어서, vi 수행

11.  vi ifcfg-eno16777728 

12.  BOOTPROTO = dhcp

    dhcp란?   동적 호스트 구성 프로토콜 (구글링 참조)

    

    insert 해서 아래 대로 수정하기 

    

    BOOTPROTO=none
    IPADDR=192.168.111.120
    NETMASK=255.255.255.0
    GATEWAY=192.168.111.2
    DNS1=192.168.111.2

     

    변경후 저장. 

    : wq

    

13. systemctl restart network

14. ifconfig 명령 수행해서 아이피 주소 우리가 설정한 대로 잘 되어 있는지 확인하기 !

    

     inet 192.168.111.120  netmask 255.255.255.0  broadcast 192.168.111.255

15.  firefox 띄워서 naver 브라우저 잘 수행되는지 보기 

    --------------------------------------------------------------------------------------------------------------------------------

    

[ JDK 1.8 설치하기]

1. oracle.com/java/technologies 접속
2. [Java SE 8u251] 클릭
3. JDK 다운로드 클릭

​       리눅스 버전 설치 

[ jdk-8u251-linux-x64.tar.gz](https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html#license-lightbox)

로그인 해야함. 미리 내려 받아놓으심 . 미리 알랴 주시지^^^^^^^^^

빅데이터플랫폼 파일 가면 있쩌여~



------------------------------------------------------------------------------------------------------------------------------------------------------

16. cd
17. pwd
18. ls
19. mkdir tools 툴즈 폴더 만들기
20. cd tools
21. ls
22.  home 들어가서 tools 폴더에   빅데이터플랫폼에 있는  jdk, eclipse, hadoop, tomcat  복사해서 붙여넣기

23.  작업관리자 들어가서  OracleServiceXE 중지 시키기~

---------------------------------------------------------------------------------------------------------------------

24. hostname ----> master 나옴

    master로 안되어 있으면 

    hostnamectl set-hostname master 명령어  입력 

25.  선생님이 나눠주신 hadoop 자료에 6페이지  3. JDK 를 설치한다 그대로 수행하기

    ---->

     tar ( 여러 명령어를 묶어 놓은 것)

​        tar.gz (묶어서 압축 까지 한 것을 의미)

​        tar xvf (압축 푸는 거) z(압축 풀어서 수행까지)

​		-------->

​        mv  jdk1.8.0_131  명령어 다음 ,  ln -s jdk1.8.0_131 java 사이에

​       cd /usr/local 명령어 수행 넣어주기!!

​		------------->

​         vi /etc/profile  하고

​        insert 해서 , 그 파일 제일 아래에  박스 안에 있는 내용 추가하고 저장후 나와서 다음 명령어 수행()

​         export  JAVA_HOME 

​         export PATH    추가해주기

​		----------------------------->

​        java -version 명령어 수행,

​        버전 1.8.0_131로 되어 있나 확인하기!  

--------------------------------------------------------------------------------------------------------------------------------------------------------------

26.  cd

27.  cd tools

28.  su centos :  user centos로 바꾸는 명령어

29. cd 

30. cd imsi

31. ls

32. javac Example.java

33. java Example

    --------> 현재시간 정보 나옴

32. Ctrl + D  하면  exit 해서 나옴

33.  tar xvfz e 하고 tab 하고 명령어 수행

34.  ls 하면

    --------------> eclipse  설치 되어 있는거 보여짐

35. cd eclipse

36. ls

37. ./eclipse 하면, 이클립스 창 수행됨. launch 하기 

38.  이클립스 죽을때 까지  사용중이던 터미널은 대기 상태, 

     다른 작업 수행하고 싶으면   다른 터미널 띄우면 됨.

    ----------------------------------------------------------------------------------------------------------------------

39. 이클립스로 가서,

    File -> New -> Other -> Java Project

    Project Name : JavaExam

40. src -> 오른쪽 버튼 -> New -> class 

    FirstApp  , main 클릭

41. System.out.println (" Hello Linux !!") 출력해보깅~ 

     Run 버튼 수행하면 Console 창에 나오게 됨.  

-------------------------------------------------------------------------------------------------------------------------------------------------

42. 다른 터미널 띄워서

43. pwd

44. cd tools

45. tar xvfz a 탭 해서 tomcat 설치

46. ls

47. ls a 탭 

    --------------------------------------------------------------------------------------------------------------------------------------------

48.  이클립스에 등록하기 : New -> Other -> Server-> Apache -> Tomcat 9.0 -> Browse -> apache 9.0.22 

49.  server.xml   ,  63행 port= 8000으로 바꾸기

50. New->Other -> Web -> Dynamic Web Project 

    linuxedu 만들고 next

    general 뭐시기 체크 

    

51. linuxedu -> WebContent , 오른쪽 버튼 클릭-> New-> html file 

    first. html 이름으로

52. First.html 에서

    <h1>태그에  안녕하세요? 리눅스의 웹 서비스입니다
    
    </h1>

    치고 ,  

    servers , ADD and REMOVE 에서 

     linuxedu 등록 . Tomcat 기동

53. firefox 브라우저 에서

    192.168.111.120:8000/linuxedu/first.html

    localhost:8000/linuxedu/first.html    둘다 쳐서 확인해보기 !

54.  리눅스 나가서, 크롬창에서

    http://192.168.111.120:8000/linuxedu/first.html   .....안돼!!!ㅡ_ㅡ 

    ------> 해결방법

55. 방화벽 종료와 중단 ( 선생님이 주신 탬플릿  9 페이지 19.방화벽 종료와 중단 참조!)

    systemctl stop firewalld

    systemctl disable firewalld  

    -------------> 다시 크롬창 가보면 접근 되어 있음 ! 싱기방기동방싱기