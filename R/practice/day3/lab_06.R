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
