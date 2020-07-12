### day3 실습



#### 문서-1

```
[문제1] 다음과 같이 값이 구성되는 리스트를 정의하여 L1 에 저장한다.
 
 3000 을 추출하여 2를 곱한 후에 result1 변수에 저장한다.

[문제2] 다음과 같이 값이 구성되는 리스트를 정의하여 L2 에 저장한다.
 

[문제3] 다음 리스트에서 A를 "Alpha"로 대체한다.(L3)
	list(c(3,5,7), c(“A”, “B”, “C”))

[문제4] 다음 리스트에서 첫 번째 원소(alpha)의 각 값에 10을 더하여 출력한다.(L4)
	list(alpha=0:4, beta=sqrt(1:5), gamma=log(1:5))


[문제5] 다음 리스트는 math, writing, reading의 중간고사 및 기말고사 점수이다. (L5)
전체 평균을 계산하여 출력한다.
     (힌트 : unlist() 함수를 활용한다. unlist() : 리스트를 벡터형식의 데이터셋으로 풀어주는 함수)
	list(math=list(95, 90), writing=list(90, 85), reading=list(85, 80))

[문제6] 힌트 : 연산자를 잘 활용해 봅시다요…
1. time 이라는 변수에 32150 이라는 값(초)을 초기화 한다.   
2. time 변수의 값으로 "XX시간 XX분 XX초" 형식으로 변환하여 출력한다.




```



#### 정답-1

lab_04.r

```r
#문제1
L1 <-list(
  name="scott",
  sal=3000)
result1<-L1$sal*2
result1<-L1[[2]]*2
result1

#문제2
L2 <- list(
    "scott",
    c(100,200,300))

L2[[1]]<- "scott"
L2[[2]]<- c(100, 200, 300)

#문제3
L3<-list(c(3,5,7), c("A", "B", "C"))
L3[[2]][1]<-"Alpha"

#문제4
L4<-list(
    alpha=0:4,
    beta=sqrt(1:5),
    gamma=log(1:5)
  )

L4$alpha
L4[[1]]<-L4[[1]][1]+10;
L4[[2]][1]+10; L4[[3]][1]+10 ; 
L4

#문제5
L5<-list(
    math=list(95,90),
    writing=list(90, 85),
    reading=list(85,50))
L5_avg <- sum(unlist(L5))/6
L5 <- unlist(L5)
L5_avg <- mean(L5)
L5_avg

#문제6
time <-c(32150)
t.cal <- list(
  hr=time, 
  min=time, 
  sec=time)
t.cal[[1]][1] <- 32150%/%3600
t.cal[[2]][1] <- (32150%%3600)%/%60
t.cal[[3]][1] <- ((32150%%3600)%%60)

it.is<-c(t.cal[[1]][1]%%3600,
         (t.cal[[2]][1]%%3600)%%60, 
         ((t.cal[[3]][1]%%3600)%%60))

unit<-c("시간", "분", "초")

paste(it.is, unit, sep="", collapse=" ")

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





