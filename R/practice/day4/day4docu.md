### day4 실습



#### 문서-1

```
[ 문제1 ]
 다음 사양의 함수 countEvenOdd() 을 생성한다.
매개변수 : 1 개
 	리턴값 : 리스트
기능 : 숫자벡터를 아규먼트로 받아 짝수의 갯수와 홀수의 갯수를 카운팅하여 
리스트(각 변수명 : even, odd)로 리턴한다.
 	      전달된 데이터가 숫자 백터가 아니면 NULL 을 리턴한다.

[ 문제2 ]
다음 사양의 함수 vmSum() 을 생성한다.
	매개변수 : 1 개
      리턴 값 : 숫자벡터	
      기능 : 전달받은 아규먼트가 벡터인 경우에만 기능을 수행한다.
              벡터가 아니면 “벡터만 전달하숑!”라는 메시지를 리턴한다.
              벡터라 하더라도 숫자 벡터가 아니면 “숫자 벡터를 전달하숑!” 라는 
 	      메시지를 출력하고 0 을 리턴한다.
전달된 숫자 벡터의 모든 값을 더하여 리턴한다.


[ 문제3 ]
다음 사양의 함수 vmSum2() 을 생성한다.

	매개변수 : 1 개
      리턴 값 : 숫자벡터
      기능 : 전달받은 아규먼트가 벡터인 경우에만 기능을 수행한다.
              벡터가 아니면 “벡터만 전달하숑!”라는 메시지를 가지고 error 를 발생시킨다.
              벡터라 하더라도 숫자 벡터가 아니면 “숫자 벡터를 전달하숑!” 라는 
 	      메시지를 가지고 warning 을 발생시키고 0 을 리턴한다.
전달된 숫자 벡터의 모든 값을 더하여 리턴한다.

[ 문제4 ]
다음의 기능을 지원하는 함수 mySum()을 생성한다.

아규먼트 : 벡터 한 개
리턴값 : 리스트 한 개 또는 NULL

(1) 전달된 벡터에서 짝수번째 데이터들의 합과 홀수번째 데이터들의 합을 구하여 
     list 객체로 리턴하는데 각각 oddSum과 evenSum 이라고 변수명을 설정한다.

(2) 벡터가 온 경우에만 기능을 수행하며 벡터가 오지 않은 경우에는 "벡터만 처리 가능!!"이라는
     메시지로 에러를 발생시킨다.

(3) 전달된 벡터에 NA 값이 하나라도 존재하는 경우에는 "NA를 최저값으로 변경하여 처리함!!" 이라는 
     메시지를 경고를 발생시킨다. 그리고 NA 는 최저값으로 설정하여 기능을 수행한 후에 결과를 리턴한다.

(4) NULL이 온 경우에는 NULL을 리턴한다.

[ 문제5 ]
다음의 기능을 지원하는 함수 myExpr()을 생성한다.

아규먼트 : 함수 한 개
리턴값 : 한 개의 숫자값

(1) 아규먼트로 함수를 전달받는다. 
(2) 아규먼트가 함수가 아니면 "수행 안할꺼임!!" 이라는 메시지로 에러를 발생시킨다.
(3) 1부터 45 사이의 난수 6개를 추출하여 아규먼트로 전달된 함수를 호출하고 그 결과를
      리턴한다.




[ 문제6 ]
다음 사양의 함수 createVector1() 을 생성한다.

아규먼트 : 가변(숫자, 문자열, 논리형(데이터 타입의 제한이 없다.))
리턴 값 : 벡터

(1) 전달된 아규먼트가 없으면 NULL을 리턴한다.
(2) 전달된 아규먼트에 하나라도 NA 가 있으면 NA를 리턴한다.
(3) 전달된 데이터들을 가지고 벡터를 생성하여 리턴한다.

[ 문제7 ]
  다음 사양의 함수 createVector2() 을 생성한다.
	매개변수 : 가변(숫자, 문자열, 논리형(데이터 타입의 제한이 없다.))
      리턴 값 : 리스트객체
      기능 : 전달된 아규먼트가 없으면 NULL을 리턴한다.
          전달된 데이터들을 각 타입에 알맞게 각각의 벡터들을 만들고 리스트에 담아서 리턴한다.



[ 문제8 ] – 함수 문제 아님
iotest1.txt 파일에 저장된 데이터들을 읽고 다음과 같은 형식으로 결과를 출력하는
R 코드를 구현하고 test1.R 로 저장하여 제출한다.

      오름차순 : ….
      내림차순 : ….
      합 : ...
      평균 : ...      

[ 문제9 ] – 함수 문제 아님
iotest2.txt 파일에 저장된 데이터들을 읽고 다음과 같은 형식으로 결과를 출력하는
R 코드를 구현하고 test2.R 로 저장하여 제출한다.

     “가장 많이 등장한 단어는 XX 입니다.”



```



#### 정답-1

lab_07.r

```r
#문제1
countEvenOdd<- function(p1){
  even<-0
  odd<-0
  if(is.numeric(p1)){
    for(data in p1){
      if(data%%2==0)
        even<-even+1
      else if(data%%2==1)
        odd<-odd+1
    }
  }else if(!is.numeric(p1)){
    return()
  }
  return (list(even=even, odd=odd))
}


p1<- c("1","@")
p2<- c(1:4)
countEvenOdd(p1)
countEvenOdd(p2)

#문제2
vmSum<-function(data){
  sum<-0
  if(is.vector(data)&&!is.list(data)){
    if(all(is.numeric(data))){
      result<-sum(data)
    }else{
      print("숫자벡터만 전달하숑!!!")
      result<-0
    }
  }else{
    result <- "벡터만 전달하숑!!!"
  }
  return(result)
}
  
vmSum(p1) #숫자벡터를 입력하숑
vmSum(p2) #정상작동
p3 <- list(a=1,2,b=3,4,5)
vmSum(p3) #벡터 아닌걸로 하고 싶은데

#문제3 
vmSum2<-function(num){
  sum<-0
  if(!is.vector(num)){
    stop("벡터만 전달하숑!")
  }else if(is.vector(num)){
    for(i in 1:length(num)){
      if(!is.numeric(num[i])){
        warning("숫자 벡터를 전달하숑!")
        return(0)
      }else{
        sum<-sum+num[i]
      }
    }
    return(sum)
  }
} 

vmSum2(p1) #숫지벡터를 입력하숑
vmSum2(p2) #정상작동
p3 <- list(a=1,2,b=3,4,5)
vmSum2(p3) #벡터 아닌걸로 하고 싶은데

#문제4
mySum<-function(p1){
  oddSum<-0
  evenSum<-0
  if(is.vector(p1)){
    for(i in 1:length(p1)){
      if(is.na(p1[i])){
        warning("NA를 최저값으로 변경하여 처리함")
        p1[is.na(p1)]<-min(any(!is.na(p1))) #새로운 것!
      }else if(is.numeric(p1[i])){
        if(i%%2==1){
          oddSum<-oddSum+p1[i]
        }else if(i %%2==0){
          evenSum<-evenSum+p1[i]
        }
      }
    }
    return(cat("oddsum", oddSum, "evensum", evenSum,"\n"))
  }else if(is.null(p1)){
    return()
  }else{
    stop("벡터만 처리가능!!")
  }
}
mySum(c(1:4)) #정상
mySum(c(1,NA,5,3)) #NA

#문제5
myExpr<-function(arg1){
  r.num<- sample(1:45, 6)
  return(r.num)
}
myExpr(2)

#문제5- 모범답안
myExpr <- function(X){
  if(is.function(x)){
    num <- sample(1:45,6)
    return (x(num))
  }else{
    stop("수행 안할거임!!")
  }
}
myExpr(sum)

#문제6
createVector1<-function(...){
  data<-c(...)
  result<-NULL
  if (length(data)==0)  #NULL리턴턴
    result <- NULL
  else if(!length(data)==0){
    for (i in 1: length(data)) {
      if(is.na(data[i]))
        result <- NA #NA리턴
      else
        result <-data #vector return
    }
  }
  return(result)
}
createVector1(c(1,2,3,4,5))
createVector1(c(1,2,NA))
createVector1()

#문제6- 모범답안
createVector1<- function(...){
  data<-c(...)
  result<-NULL
  if(length(data)==0){
    result<-NULL
  }else if(any(is.na(data))){
    result<- NA
  }else{
    result<-data
  }
  return(result)
}c
createVector1(c(1,2,3,4,5))
createVector1(c(1,2,NA))
createVector1()


#문제7
createVector2<-function(...){
  data<-list(...)
  numeric <-NULL
  character <-NULL
  logical <-NULL
  
  if(length(data)==0){
    return()
  }
  
  else{
    for(i in data){
        if(is.numeric(i)){
          numeric <-c(numeric, i)
        }
        else if(is.character(i)){
          character<- c(character, i)
        }
        else if(is.logical(i)){
          logical<- c(logical, i)
        }
    }
    result<-list(NUMERIC=numeric, CHARACTER=character, LOGICAL=logical)
    return(result)
  }

}

createVector2(1,2,3,T,"dd")


```



<hr>

#### 문서-2

```
# 제어문
[문제1]
1. grade 라는 변수에 1부터 6사이의 난수를 추출하여 저장한다. 
2. grade 의 값이 1 또는 2 또는 3이면 다음 결과를 출력한다.
   "x 학년은 저학년입니다."
   grade 의 값이 4 또는 5 또는 6이면 다음 결과를 출력한다.
   "x 학년은 고학년입니다."
[문제2]
1. choice 라는 변수에 1부터 5사이의 난수를 추출하여 저장한다. 
   )
2. 추출된 값이 1이면 300 과 50 의 덧셈 연산을 처리한다.
    추출된 값이 2이면 300 과 50 의 뺄셈 연산을 처리한다.
    추출된 값이 3이면 300 과 50 의 곱셈 연산을 처리한다.
    추출된 값이 4이면 300 과 50 의 나눗셈 연산을 처리한다.
    추출된 값이 5이면 300 과 50 의 나머지 연산을 처리한다.

3. 출력 형식(단, 출력문장은 한 번만 구현한다.)
    결과값 : XX


[문제3]
1. count 라는 변수에 3부터 10사이의 난수를 추출하여 저장한다. 
2. 1부터 3사이의 난수를 추출한다.(deco)
3. deco가 1이면 "*"을  count 값만큼 출력한다.
  deco가  2이면 "$"을  count 값만큼 출력한다.
  deco가  3이면 "#"을  count 값만큼 출력한다.

[문제4] – switch() 함수로 문제를 해결한다.
1. score 라는 변수에 0~100 사이의 난수를 저장한다.
2. score 의 값이 90~100 이면 level 변수에 “A 등급”을 저장한다.
score 의 값이 80~89 이면 level 변수에 “B 등급”을 저장한다.
score 의 값이 70~79 이면 level 변수에 “C 등급”을 저장한다.
score 의 값이 60~69 이면 level 변수에 “D 등급”을 저장한다.
score 의 값이 59 이하면 level 변수에 “F 등급”을 저장한다.
3. 결과를 다음 형식으로 출력한다.
        “xx 점은 x 등급입니다.”

[문제5] 제어문 사용이 필수는 아님 (^^)
다음과 같이 영문자 대문자와 소문자로 구성되는 원소들을 갖는 벡터 alpha 를 생성하여 벡터의 내용을 화면에 출력한다.
 	“Aa” “Bb” …………………….. “Zz”

```



#### 정답-2

lab_05.r

```r
#문제1 
grade <- sample(1:6,1)

if(grade==1 | grade==2 | grade==3){
  cat(grade,"학년은 저학년입니다.", "\n")
}else{
  cat(grade,"학년은 고학년입니다.", "\n")
}

#문제2
choice<-sample(1:5,1)
num1<-c(300)
num2<-c(50)
if(choice==1){
  cat("결과값 :", num1+num2, "\n")
}else if(choice==2){
  cat("결과값 :",num1-num2, "\n")
}else if(choice==3){
  cat("결과값 :",num1*num2, "\n")
}else if(choice==4){
  cat("결과값 :",num1%/%num2, "\n")
}else{
  cat("결과값 :",num1%%num2, "\n")
}


#문제3
count<- sample(3:10,1)
deco<-sample(1:3,1)
i<-1

if(deco==1){
  for(i in 1:count)
    cat("*")
}else if(deco==2){
  for(i in 1:count)
    cat("$")
}else if(deco==3){
  for(i in 1:count)
    cat("#")
}

#문제4
#a
score <- sample(0:100,1)
score

level <- switch(EXPR=as.character(score%/%10),
                "10"=,"9"="A",
                "8"="B",
                "7"="C",
                "6"="D",
                "F")
cat(score,"점은", level,"등급입니다.")

#b
score <- as.character(score)
level <- switch(EXPR=score, 
    "90"=,"91"=,"92"=,"93"=,"94"=,"95"=,"96"=,"97"=,"98"=,"99"=, "100"="A등급",
    "80"=,"81"=,"82"=,"83"=,"84"=,"85"=,"86"=,"87"=,"88"=,"89"="B등급",
    "70"=,"71"=,"72"=,"73"=,"74"=,"75"=,"76"=,"77"=,"78"=, "79"="C등급",
    "60"=,"61"=,"62"=,"63"=,"64"=,"65"=,"66"=,"67"=,"68"=, "69"="D등급","F등급")
cat(score, "점은", level,"등급입니다.","\n")


#문제5
#my answer
big<-LETTERS[1:26]
snall<-letters[1:26]
i<-1

for(i in 1:26){
  alpha[i]<-paste(LETTERS[i],letters[i],sep="")
}

#friend1
for(i in 1:length(LETTERS)){
  alpha[i]<-paste(LETTERS[i], letters[i], sep="")
}
alpha

#friend2
alpha<- paste(LETTERS, letters, sep="")
alpha
cat(alpha)

#oliver
for(i in 1:26){
  cat("\"", big[i], small[i],"\"","", sep="")
}

```





<hr>

#### 문서-3



```
# 함수 정의와 활용

[ 문제 1 ]
다음 사양의 함수 exam1( )을 생성한다.
    매개변수 : 없음
    리턴 값 :  1개
    기능 : “Aa” “Bb” ~ “Zz” 등으로 구성된 벡터를 리턴한다.
결과 출력은 함수를 호출한 다음 리턴값을 받아서 호출한 쪽에서 한다.
   

[ 문제 2 ]
다음 사양의 함수 exam2( )을 생성한다.
    매개변수 : 1 개
    리턴 값 :  1개
    기능 : 아규먼트로 숫자 한 개를 받는다. 
1 부터 이 숫자 값까지의 합을 구해서 리턴한다.
결과 출력은 함수를 호출한 다음 리턴값을 받아서 호출한 쪽에서 한다.


[ 문제 3 ]
다음 사양의 함수 exam3( )을 생성한다.
    매개변수 : 2 개
    리턴 값 :  1개
    기능 : 전달받은 2개의 데이터 중에서 큰 값에서 작은 값의 차를 리턴
           두 값이 동일하면 0 을 리턴한다.
           예를 들어
           10, 20 이 전달되면 ---> 10 리턴
           20, 5 가 전달되면 ---> 15 리턴
           5, 30 이 전달되면 ---> 25 리턴
           6, 3 이 전달되면  ---> 3 리턴
           결과 출력은 함수를 호출한 다음 리턴값을 받아서 호출한 쪽에서 한다.




[ 문제 4 ]
다음 사양의 함수 exam4( )를 생성한다.
    매개변수 : 3 개
    리턴 값 :  1개
기능 : 아규먼트를 숫자 연산자 숫자 순으로 전달받는다.
            (연산자는 +, -, *, %/%, %% 를 받는 것으로 정한다)
            전달된 두 개의 숫자에 대하여 연산을 처리하고 그 결과를 리턴한다.

           단,
           다른 연산자가 전달되면 "규격의 연산자만 전달하세요"를 리턴한다.
           %/% 와 %%  가 전달된 경우에 한해서 첫 번째 숫자가 0이면 "오류1" 이라고 리턴한다.
           %/% 와 %%  가 전달된 경우에 한해서 두 번째 숫자가 0이면 "오류2" 라고 리턴한다.
           함수를 호출하여 리턴된 결과를 출력하는 것은 호출한 쪽에서 한다.


[ 문제5 ]
다음 사양의 함수 exam5( )을 생성한다.
    매개변수 : 2 개(한 개는 필수, 또 다른 한 개는 선택(기본값 설정)
    리턴 값 :  없음(NULL 리턴)
기능 : 첫 번째 아규먼트는 숫자를 두번째 아규먼트는 문자를 입력받아서
           숫자의 개수만큼 문자를 출력하는 기능을 처리한다.(행바꿈 없이)
           문자가 전달되지 않으면 기본값은 "#" 로 처리한다.
           숫자로 음의 값이 전달되면 아무것도 출력하지 않는다.


[ 문제6 ]
다음 사양의 함수 exam6( )를 생성한다.
   매개변수 : 1 개
   리턴 값 :  없음(NULL 리턴)
기능 : 아규먼트로 전달되는 벡터에는 학생들의 점수(0~100)가 들어 있다.
           점수에 따라서 결과를 출력한다.
           85~100 "상"
           70~84  "중"
           ~69    "하"
           출력형식 : "xx 점은 x등급입니다." 
           NA 값이 존재하는 경우엔
                          "NA 는 처리불가" 를 출력한다.
           모든 출력은 print() 함수를 사용한다.

   exam6(c(80, 50, 70, 66, NA, 35))


```



#### 문서-3

lab_06.r

```r
#[ 문제 1 ]
#다음 사양의 함수 exam1( )을 생성한다.
#매개변수 : 없음
#리턴 값 :  1개
#기능 : “Aa” “Bb” ~ “Zz” 등으로 구성된 벡터를 리턴한다.
#결과 출력은 함수를 호출한 다음 리턴값을 받아서 호출한 쪽에서 한다.

exam1<-function(){
  big<-LETTERS[1:26]
  small<-letters[1:26]
  for(i in 1:26){
    alpha<-cat("\"", big[i], small[i],"\""," ", sep="")
  }
  return(alpha)
}

exam1<- function(){
  alpha <- paste(LETTERS,letters, sep="")
  return(alpha)
}

exam1()

#[ 문제 2 ]
#다음 사양의 함수 exam2( )을 생성한다.
#매개변수 : 1 개
#리턴 값 :  1개
#기능 : 아규먼트로 숫자 한 개를 받는다. 
#1 부터 이 숫자 값까지의 합을 구해서 리턴한다.
#결과 출력은 함수를 호출한 다음 리턴값을 받아서 호출한 쪽에서 한다.


exam2<-function(num){
  sum<-0
  for (i in 1:num){ #뎅터 값을 가지고 벡터 만들어줌
    sum<-sum+i
  }
  print(random.num)
  return(sum)
}

random.num<-sample(1:100,1)
exam2(random.num)



#[ 문제 3 ]
#다음 사양의 함수 exam3( )을 생성한다.
#매개변수 : 2 개
#리턴 값 :  1개
#기능 : 전달받은 2개의 데이터 중에서 큰 값에서 작은 값의 차를 리턴
#두 값이 동일하면 0 을 리턴한다.
#예를 들어
#10, 20 이 전달되면 ---> 10 리턴
#20, 5 가 전달되면 ---> 15 리턴
#5, 30 이 전달되면 ---> 25 리턴
#6, 3 이 전달되면  ---> 3 리턴
#결과 출력은 함수를 호출한 다음 리턴값을 받아서 호출한 쪽에서 한다.

exam3<- function(p1, p2){
  if(p1==p2){
    value<-0
  }else if(p1>p2){
    value<- p1-p2
  }else{
    value<-(p2-p1)
  }
  return(value)
}
r.num<-sample(1:10,2)
exam3(r.num[1], r.num[2])

#[ 문제 4 ]
#다음 사양의 함수 exam4( )를 생성한다.
#매개변수 : 3 개
#리턴 값 :  1개
#기능 : 아규먼트를 숫자 연산자 숫자 순으로 전달받는다.
#(연산자는 +, -, *, %/%, %% 를 받는 것으로 정한다)
#전달된 두 개의 숫자에 대하여 연산을 처리하고 그 결과를 리턴한다.

#단,
#다른 연산자가 전달되면 "규격의 연산자만 전달하세요"를 리턴한다.
#%/% 와 %%  가 전달된 경우에 한해서 첫 번째 숫자가 0이면 "오류1" 이라고 리턴한다.
#%/% 와 %%  가 전달된 경우에 한해서 두 번째 숫자가 0이면 "오류2" 라고 리턴한다.
#함수를 호출하여 리턴된 결과를 출력하는 것은 호출한 쪽에서 한다.

exam4 <- function(num1, p1, num2){
  if(p1=="+"){
    value <- (rr.num[1]+rr.num[2])
  }else if(p1=="-"){
    value <- (rr.num[1]-rr.num[2])
  }else if(p1=="*"){
    value <- (rr.num[1]*rr.num[2])
  }else if(p1=="%/%" | p1=="%%"){
    if(rr.num[1]==0 & rr.num[2]!=0){
      value <-("error1")
    }else if(rr.num[2]==0 & rr.num[1]!=0){
      value <-("error2")
    }else{
      if(p1=="%/%"){
        value <-(rr.num[1]%/%rr.num[2])
      }else{
        value <-(rr.num[1]%%rr.num[2])
      }
    }
  }else{
    value<- "규격의 연산자만 전달하세요."
  }
  return (value)
}

rr.num <- sample(0:10,2)
cat("your number is", rr.num[1], rr.num[2], "\n")
exam4(rr.num[1],"-",rr.num[2])

# 0/0 = nan
# ?/0 = infinite

#문제5
exam5<-function(num, p1="#"){
    if(num<0){
      nothing<-cat("nothing to be commited")
      return(nothing)
    }else{
      for(i in 1:num)
        cat(p1,"", sep="")
    }
}
  
exam5(7,"z")


#문제6


exam6 <- function(...){
  data<-list(...)
  for(item in data){
    if(is.numeric(item)){
      if(item<=100 & item>=85){
        grade <-c("상")
      }else if(item<85 & item>=70){
        grade <-c("중")
      }else{
        grade <-c("하")
      }
      print(paste(item, "점은", grade, "등급입니다."))
    }
   
    else{
      print("NA는 처리불가")
    }
    
  }
}


exam7<- function(x){
  for(data in x){
    if(is.na(data)){
      print("NA는 처리불가")
    }else{
      if(data>=85){
        grade<-"상"
      }else if(data>=70){
        grade<-"중"
      }else{
        grade <- "하"
      }
    }
  }
  print(paste0(x,'점은', grade,"등급입니다.", sep=''))
  return() #NULL을 리턴하고 싶다면!
}
exam7(c(90, 35,  50, 60, NA))
exam6(100, NA, 50, 40, 32 )

```





