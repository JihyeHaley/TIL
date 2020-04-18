#LIST
v<-c(1,2,3)
l<-list(1,2,3) 
#list만들때 쓰는 대표함수는 list
v*3 #vector은 연산을 할 수 있지만, list는 안된다.
l*3 #error #wrapping 되서 들어갔기 때문에에
    #unlist해서 잠깐 사용하고 바꾸는 방법도 있다.
v[1] *3
l[1] *3 #wrapping된 상태로는 calculation이 안된다.
l[[3]] *3 #포장을 벗기거나 $를 이용해서 

lds <- list(1,2,3) 
lds
lds+100
unlist(lds)
unlist(lds)+100
lds[1]
lds[1]+10
lds[[1]]+10

names(lds) <- LETTERS[1:3]
lds
#아래 3가지는 다 똑같은 반응
lds[[2]]
lds[["B"]]
lds$B

a<-list(
  a = 1:3,
  b = "a string",
  c = pi,
  d = list(-1,-5)
)

a[1]
a[[1]] # a[["a"]]
a$a
a[[1]][1] #1
a$a[1] # 
a[1]+1
a[[1]]+1
a[[1]][2] <- 100 #대입
new_a <- unlist(a[1])
a[1]; new_a #이름없는 벡터가 출력
names(a) <- NULL
names(new_a) <- NULL



ls()
length(ls())
save(list=ls(),file="all.rda") # varience will save in "all.rda" of rexam
rm(list=ls())
ls()
load("all.rda")
ls()

#read file data
nums <- scan("data/sample_num.txt")
word_ansi <- scan("data/sample_ansi.txt",what="")
words_utf8 <- scan("data/sample_utf8.txt", what="",encoding="UTF-8")
words_utf8_new <- scan("data/sample_utf8.txt", what="")
lines_ansi <- readLines("data/sample_ansi.txt")
lines_utf8 <- readLines("data/sample_utf8.txt",encoding="UTF-8")#반드시 대문자로 줘야한다.

df2 <- read.table("data/product_click.log")
#read.table - seperate 문자로 지정, 
#read.csv - comma(,)로 구분
str(df2)
head(df2)
summary(df2$V2)
?print


for(data in month.name) 
  print(data)

for(data in month.name) 
  cat(data)

sum <- 0
for(i in 5:15){
  if(i%%10==0){
    break
  }
  sum <- sum + i
  print(paste(i,":",sum))#결합기능이 없으니깐 paste함수써서!
}


sum <-0
for(i in 5:15){
  if(i%%10==0){
    next;  #continue 와 기능이 똑같당!!!!
  }
  sum <- sum + i
  print(paste(i,":",sum))
}

sumNumber <- 0
while(sumNumber <= 20) { 
  i <- sample(1:5, 1) 
  sumNumber <-sumNumber+i; 
  cat(sumNumber,"\n")
} 

repeat {
  cat("ㅋㅋㅋ\n")
}


sumNumber <- 0
repeat { 
  i <- sample(1:5, 1) 
  sumNumber <-sumNumber+i; 
  cat(sumNumber,"\n")
  if(sumNumber > 20)
    break;
}


#제어문
#if else
randomNum <-sample(1:10,1)
if(randomNum>5){
  cat(randomNum,":5보다 크군요","\n")
}else{
  cat(randomNum,":5보다 작거나 같군요","\n")
}

if(randomNum%%2 == 1){
  cat(randomNum,";홀수\n")
}else{
  cat(randomNum,";짝수","\n")
}


if(randomNum%%2 == 1){
  cat(randomNum,";홀수","\n")
}else{
  cat(randomNum,";짝수","\n")
}

score <- sample(0:100, 1)  # 0~100 숫자 한 개를 무작위로 뽑아서
if (score >=90){
  cat(score,"는 A등급입니다","\n")
}else if (score >=80){
  cat(score,"는 B등급입니다","\n")
}else if (score >=70){
  cat(score,"는 C등급입니다","\n")
}else if (score >=60){
  cat(score,"는 D등급입니다","\n")
}else {
  cat(score,"는 F등급입니다","\n")
}

#for문
#for 실습
for(data in month.name) 
  print(data)
for(data in month.name)print(data);print("ㅋㅋ")
for(data in month.name){print(data);print("ㅋㅋ")}

for(n in 1:5)
  cat("hello?","\n")

for(i in 1:5){
  for(j in 1:5){
    cat("i=",i,"j=",j,"\n")
  }
}
# 구구단
for(dan in 1:9){
  for(num in 1:9){
    cat(dan,"x",num,"=",dan*num,"\t") # \n : 개행문자, \t : 탭문자
  }
  cat("\n")
}


bb <- F
for(i in 1:9){
  for(j in 1:9){
    if(i*j>30){
      bb<-T
      break
    } 
    cat(i,"*",j,"=",i*j,"\t")
  }
  cat("\n")
  if(bb) #bb가 TRUE이면
    break
}

#while문
i<-1
while(i <= 10){
  cat(i,"\n")
  i <- i+1
}
cat("종료 후 :",i,"\n")

i<-1
while (i<=10) {
  cat(i,"\n")
}

i<-1
while (i<=10) {
  cat(i,"\n")
  i<-i+2
}

i<-1
while (i<=10) {
  cat(i,"\n")
  i<-i+1
}

#switch 문을 대신하는 함수
month <- sample(1:12,1)
month <- paste(month,"월",sep="") # "3월"  "3 월"
result <- switch(EXPR=month,
                 "12월"=,"1월"=,"2월"="겨울",
                 "3월"=,"4월"=,"5월"="봄",
                 "6월"=,"7월"=,"8월"="여름",
                 "가을")
cat(month,"은(는) ",result,"입니다\n",sep="")

num <- sample(1:10,1)
num
switch(EXPR = num,"A","B","C","D")
#1이면A, 2이면B,3 이면C... 4 이상이면 아무것도 안나와!

for(num in 1:10){
  cat(num,":",switch(EXPR = num,"A","B","C","D"),"\n")
}
#캐릭터로 바꿔서 지정하면 원하는 결과물 만들 수 이따.
#AS.CHARACTER 을 활용해서
#paste0(num,"")보다는 as.character

for(num in 1:10){
  num <- as.character(num)
  cat(num,":",switch(EXPR = num,
    "6"=,"7"="A","8"="B","9"="C","10"="D","ㅋ"),"\n")
}






# 함수 정의와 활용

func1 <- function() {
  xx <- 10   # 지역변수
  yy <- 20
  return(xx*yy)
}
func1()

result <- func1()
result
#오류발생


func2 <- function(x,y) {
  xx <- x
  yy <- y
  return(sum(xx, yy))
}

func2()
func2(5,6) # 식 : 연산식, 호출식, 변수, 리터럴

func3 <- function(x,y) {
  #x3 <- x+1
  #y3 <- y+1
  x4 <- func2(x+1, y+1)  # 값(식) : 변수, 리터럴, 연산식, 호출식
  return(x4)
}

func3(9, 19)  # 30

func4 <- function(x=100, y=200, z) {
  return(x+y+z)
}
func4() #error
func4(10,20,30)
func4(x=1,y=2,z=3)
func4(y=11,z=22,x=33)
func4(z=1000) #기본값이 있기 때문에 it works even only when z is available 

# 쉬트에 있는 함수 코드
f1 <- function() print("TEST")
f1()
r <- f1()
r


f2 <- function(num) {print("TEST"); print(num) }
f2(100)
f2() # error


f3<- function (p="R") print(p)
f3() #매개변수를 이미 지정해줘서 R이 튀어나온다.
f3(p="PYTHON")
f3("java")


f4<- function (p1="ㅋㅋㅋ",p2) for(i in 1:p2) print(p1)
f4(p1="abc", p2=3)
f4("abc", 3) 
f4(5) #인자가 2개가 있어야 하는데 1개만 주어줘서 ERROR
f4(p2=5) 


f5<- function(...) { 
  print("TEST"); 
  data <- c(...); 
  print(length(data))}
f5(10, 20, 30)
f5("abc", T, 10, 20)  #Cuz Vector, parameters are all changed to characters.


f6<- function(...) {
  print("수행시작")
  data <- c(...)
  for(item in data) {
    print(item)
  }
  return(length(data))
}
f6()
f6(10)
f6(10,20)
f6(10,20,30)
f6(10,'abc', T, F)



f7<- function(...) {
  data <- c(...)
  sum <- 0;
  for(item in data) {
    if(is.numeric(item))
      sum <- sum + item
    else
      print(item)
  }
}
f7(10,20,30)
f7(10,20,'test', 30,40) #all are changed to characteristic.
#so there are no sum results

f8<- function(...) {
  data <- list(...) #cuz it is list
  sum <- 0;
  for(item in data) {
    if(is.numeric(item))
      sum <- sum + item
    else
      print(item)
  }
  return(sum)
}

f8(10,20,30)
f8(10,20,"test", 30,40) #list이기 때문에