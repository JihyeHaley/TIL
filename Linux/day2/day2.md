# Linux day2

:grey_question: linux cmd 에서는 .java 는 만들 수 있지만, javac [file name]으로 실행시키는 내장 프로그램 없음

:grey_question: 꺽세 괄호가 있으면 후자에 있는 파일명으로 만들어서 보여준다. (*cf.* 2개 - append)

:question: 명령1 **|** 명령2

​	ex. cat a.txt b.txt | more : 파일이 아무리 길어도 페이지를 나눠서 보여준다


## ::bookmark_tabs:  Terminal

* ```
  [centos@master ~]$ 
  ```

  * master은 컴퓨터 이름
  * centos는 운영체제 이름

  

* **pwd** : print working directory



* **ls** : list

  *  **ls -l** , **ll**

    * ```
      ls -l  // '-l'은 옵션 , 자세한 정보를 보고싶을 때
      ```

    * ```
      ll
      ------------------------------------------------------
      합계 0
      drwxr-xr-x. 2 centos centos 6  4월 27 09:32 공개
      drwxr-xr-x. 2 centos centos 6  4월 27 09:32 다운로드
      ```

  * **ls -a**

    * ```
      ls -a // 'all'은 옵션, 모두 보여줘
      ------------------------------------------------------
      .   .ICEauthority  .bash_profile  .cache   .esd_auth  .mozilla  다운로드  바탕화면  사진  음악
      ..  .bash_logout   .bashrc        .config  .local     공개      문서      비디오   서식
      ```

  * **ls -al**

    * ```
      ls -al // 'a,l 모두 적용', 모든 파일을 길게 보여줘
      ------------------------------------------------------
      drwx------. 14 centos centos 4096  4월 27 09:32 .
      drwxr-xr-x.  3 root   root     19  4월 24 20:54 ..
      -rw-------.  1 centos centos  310  4월 27 09:32 .ICEauthority
      -rw-r--r--.  1 centos centos   18  6월 10  2014 .bash_logout
      .
      .
      .
      ```




* wc  [something] [filename.확장자]

  * word count 

  

* **mkdir** , make directory

  * mkdir xxx

    * ```
      mkdir imsi
      ll
      ------------------------------------------------------
      drwxrwxr-x. 2 centos centos 6  4월 27 10:53 imsi
      ```
      
      * sub folder로 만들고 싶으면 /로 표현
      
        ```
        mkdir -p /def/fhg
        ```
  
* rmdir

  * directory 삭제

    ```
    rmdir adc
    ```

    

* **rm**

  * rm [file name]
  * rm *.java <- .java로 하는 모든 파일 삭제 
    * rm -i [file name] : 는 deaflt:  it asks till finishing <- 번거로움
    * rm **-f** [file name] :를 주면  force delete 가능  
    * rm -r [file name]: recursive and 하위 디렉토리까지 다 삭제 <- it asks
    * rm -r**f** [file name]: recursive and 하위 디렉토리까지 다 삭제 <- it automatically remove

* cp

  *  cp  [a file] [b file] : 이름 바꿔서 복사 

    

* touch

  * 폴더만 있고 내용은 없는 것 
  * 내용은 없어서  size 는 0

  

*  mv : file move

  * mv : 디렉토리로 이동 or 이름을 변경해서 이동 

  

* cat

  * conCATenate : 파일을 나열해서 보여준다.
  * **꺽세괄호를 주면은**
    * cat a.txt b.txt **>** c.txt
      * 꺽제활호 **뒤**에 있는 이름으로 출력한다. => create new file
    * It adapts to ll too like below
      * ll > filelist.txt 
        * ll 내용이 filelist.txt로 파일을 **새로** 만들어서 나오게 한다.

* more

  * 텍스트 형식으로 작성된 파일을 페이지 단위로 화면에 출력



* less



* clear 
  *  현재 사용중인 터미널 화면을 깨끗하게 지워준다.

* process
  * process status프로세스 : 현재 수행중인 프로그램

* 종료

  * ```
    shutdown -P +10 // 10분후에 꺼져
    shutdown -r 22:00 //오후 10시에 꺼져
    shutdown -c // 예약한 시간 취소
    shutdown -k +15 // 15분 후에 서버에 접속한 사람들 다 나가
    ```

    

* 로그아웃

  * ```
    logout
    exit
    ```



* 홈으로

  * ```
    cd + enter : 홈디렉토리로 옮겨갈 수 있다.
    ```

  * ```
    cd centos : 홈디렉토리로 옮겨갈 수 있다.
    ```

    

* 에디터 사용

  * ed
    
  * vi

    * ```
    vi [파일이름.txt]
      ```
  
      * ### **i or a  누르면 끼워넣기로 변경됨** insert

      * ### **i or a  누르면 끼워넣기로 변경됨 append**

      * **esc : 명령모드으로** (명령모드 상태로만 실행해야하는 명령어)

        * dd : 행전체 삭제
      *  t : 글자만 삭제
        * yy : 복사
        * p: 붙여넣기
        * :wq + enter : 저장하고 끝냄
        * :q + enter: 저장 **않고** 끝냄? 물어봄
        * :q! :저장 **않고 강제로 끝**
        * :1 : 첫번째 행
        * :n : n 번째 행으로 이동 
        * shift + g : 마지막 행 
        * ^  : 현재 행의 처음
        * $ : 현재 행의 마지막
        * /xxx : xxx 찾기
        * x : 현재 커서가 위치한 글자 삭제
        * X : 현재 커서가 위치한 앞 글자 삭제
  
        

  * **cat [file name]** or **head [file name]** or **tail [file name]**

    * file의 내용을 볼 수 있도록 보여주는 
  * head (앞에서 10줄)
    * tail (뒤에서10줄)
  
  * ```
  gedit
    ```
  
    