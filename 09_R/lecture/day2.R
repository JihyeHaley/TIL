# matrix 실습
x1 <-matrix(1:8, nrow = 2)
x1 
x1<-x1*3
x1

sum(x1); min(x1);max(x1);mean(x1)

x2 <-matrix(1:8, nrow =3)
x2

(chars <- letters[1:10])

mat1 <-matrix(chars)
mat1; dim(mat1)
matrix(chars, nrow=1)
matrix(chars, nrow=5)
matrix(chars, nrow=5, byrow=T)
matrix(chars, ncol=5)
matrix(chars, ncol=5, byrow=T)
matrix(chars, nrow=3, ncol=5)
matrix(chars, nrow=3)


vec1 <- c(1,2,3)
vec2 <- c(4,5,6)
vec3 <- c(7,8,9)
mat1 <- rbind(vec1,vec2,vec3); mat1
mat2 <- cbind(vec1,vec2,vec3); mat2
mat1[1,1]
mat1[2,];mat1[,3]
mat1[2,,drop=F]
mat1[2,,drop=F];mat1[,3,drop=F]

rownames(mat1) <- NULL
colnames(mat2) <- NULL
mat1;mat2
rownames(mat1) <- c("row1","row2","row3")
colnames(mat1) <- c("col1","col2","col3") #이름, 인덱스 모두로 찾을 수 이따 
mat1
ls() #현재까지 만들어진 객체들의 DATA SET을 모두 보여주는거
mean(x2) #matrix의 모든 값들의 숫자값들을 보여준다. 
sum(x2)
min(x2)
max(x2)
summary(x2) #열단위로 summary했다.

mean(x2[2,]) #두번째 행의 모든 데이타를 가지고 평균을 내세요.
sum(x2[2,])
rowSums(x2); #행별로 sum을 보여준다.
colSums(x2); #열열별로 sum을 보여준다.
apply(x2, 1, sum); apply(x2, 2, sum)  #마지막 argument에 함수.
?apply
apply(x2, 1, max) #1 indicates row
apply(x2, 1, min)
apply(x2, 1, mean)

apply(x2, 2, max) #2 indicates colum
apply(x2, 2, min)
apply(x2, 2, mean)

#array 실습
a1 <- array(1:30, dim=c(2,3,5)) #2행 3열 5층
a1 

a1[1,3,4] # 1행 3열 4층 꺼내줘
a1[,,3]   # 3층에 있는거 다 꺼내줘
a1[,2,]   # 2열에 있는 모든거 다 꺼내줘
a1[1,,]   # 1행에 있는 모든거 다 깨내줘

getwd() #working directory보여줘라아

# factor 실습

score <- c(1,3,2,4,2,1,3,5,1,3,3,3)
class(score)
summary(score)

f_score <- factor(score)
class(f_score)
f_score
summary(f_score) #factor에 대하여 summary를 돌리면 각각데이터의 개수를 세어준다.
levels(f_score)

plot(score) #벡터 데이타
plot(f_score) #팩터 데이타


data1 <- c("월","수","토","월",
           "목","화")
data1
class(data1)
summary(data1)
day1 <- factor(data1)
day1
class(day1)
summary(day1)
levels(day1)

week.korabbname <- c("일", "월", "화",
                     "수", "목", "금", "토") 
day2 <- factor(data1, 
               levels=week.korabbname)
day2
summary(day2)
levels(day2)



btype <- factor(
  c("A", "O", "AB", "B", "O", "A"), 
  levels=c("A", "B", "O")) #AB 정해진 범주에 속하지 않는 애인데? 
                          #AB를 N/A로 만들어 보린다 
btype
summary(btype)
levels(btype)

gender <- factor(c(1,2,1,1,1,2,1,2), 
                 levels=c(1,2), 
                 labels=c("남성", "여성")) #1은 남성, 2는 여성으로 라벨링
gender
summary(gender)
levels(gender)

# 내장 데이터셋
data() #내장된 데이타를 확인할 수 있다
        # argument를 주면 사용가능한 상태로 만들어줌.
?iris ?head 
iris; head(iris);tail(iris) 
View(iris)
str(iris) #str은? 클래스와 다르게 개수는 알 수 있다. 

?data

#Dataframe 실습
no <- c(1,2,3,4)
name <- c('Apple','Banana','Peach','Berry')
qty <- c(5,2,7,9)
price <- c(500,200,200,500)
fruit <- data.frame(no, name, qty, price)
str(fruit)
View(fruit)

fruit[1,]  #matrix처럼
fruit[-1,]
fruit[,2]
fruit[,3] # fruit[,3, drop=F]
fruit[, c(3,4)] #열의 인덱스를 여러개 지정 
fruit[3,2] #factor형일때 level정보도 같이 제공해준다.
fruit[3,1]

fruit[,3]
fruit$qty
fruit[[3]]
fruit[3] # 숫자인덱스 하나만 주면-> 열의 인덱스로 인식
         # 데이터프레임 형식 유지

str(fruit$qty) #
str(fruit[3]) #dataframe 으로 보여준다.

# dataframe exam1
english <- c(90, 80, 60, 70)
math <- c(50, 60, 100, 20)
classnum <- c(1,1,2,2)
df_midterm <- data.frame(
  english, math, classnum)
df_midterm
str(df_midterm)
colnames(df_midterm)
rownames(df_midterm)
names(df_midterm) #열우선
mean(df_midterm$english) #영어성적의 평균
mean(df_midterm$math) #수학성적의 평균

df_midterm2 <- data.frame(
  c(90, 80, 60, 70), 
  c(50, 60, 100, 20), 
  c(1,1,2,2)) #문제는..!! column 명이 complex..
colnames(df_midterm2)
rownames(df_midterm2)
names(df_midterm2)
df_midterm2
df_midterm2 <- data.frame(
  영어=c(90, 80, 60, 70), 
  수학=c(50, 60, 100, 20), 
  클래스=c(1,1,2,2)) #열 이름이 복잡함을 방지하는 방법.
df_midterm2
df_midterm2$영어

df <- data.frame(var1=c(4,3,8), 
                 var2=c(2,6)) # 오류, 개수가 안맞아서
df <- data.frame(var1=c(4,3,8), 
                 var2=c(2,6,1))
str(df)
df$var_sum <- df$var1 + df$var2 #동시에 추가하고 작업할 수 있따. 
df$var_mean <- df$var_sum/2
df$result <- ifelse(df$var1>df$var2, 
                    "var1이 크다", "var1이 작다")
              #ifelse 함수쓰는데, 1번째는 true면, 2번째는 false는
getwd() # setwd('xxx')

#csv파일열기
score <- read.csv("data/score.csv") #csv= comma seperate value
score
str(score)
score$sum <- 
  score$math+score$english+score$science
score$result <- ifelse(score$sum >= 200, 
                       "pass", "fail")
score

summary(score$result) # character라서 result의 총 개수만 알려준다. 
table(score$result) #factor형이냐 character형이냐에 따라서 summary결과가 달라진다.
summary(factor(score$result)) #factor로 바꿔서 summary해주면 result의 사에 결과를 알ㄹ려준다.
score$result = factor(score$result) #result를 factor형으로 바꿈
str(score)
summary(score) #연속되지 않은 데이타 = "이산형" 데이타
score$id = as.character(score$id) #이산형은 character로 바꿔주는
score$class = factor(score$class)

score$grade<-ifelse(score$sum >= 230,"A",
                    ifelse(score$sum >= 215,"B", 
                           ifelse(score$sum >=200,"C","D")))
score

# order() 와 sort()
v <- c(10,3,7,4,8)
sort(v)
order(v)

emp <- read.csv(file.choose(),
                stringsAsFactors = F)
emp
str(emp)

# emp에서 직원 이름
emp$ename
emp[,2]
emp[,"ename"] 
emp[,2, drop=FALSE] 
emp[,"ename",drop=F] 
emp[2]
emp["ename"] 

# emp에서 직원이름, 잡, 샐러리
emp[,c(2,3,6)]
emp[,c("ename","job","sal")]
subset(emp,select = c(ename, job, sal))
?subset; head(emp); head(emp, n=1)
# emp에서 1,2,3 행 들만
emp[1:3,]
emp[c(1,2,3),]

# ename이 "KING"인 직원의 모든 정보
emp[9,] 
emp$ename=="KING" #논리형 답변
emp[c(F,F,F,F,F,F,F,F,T,F,F,F,
      F,F,F,F,F,F,F,F),] #TRUE일때만 행을 꺼내
emp[emp$ename=="KING",]
subset(emp,subset=emp$ename=="KING") 
subset(emp,emp$ename=="KING") 

# 커미션을 받는 직원들의 모든 정보 출력
emp[!is.na(emp$comm),]
subset(emp,!is.na(emp$comm)) #!is.na() 함수도 이따 

# select ename,sal from emp where sal>=2000
subset(emp, select=c("ename","sal"), 
       subset= emp$sal>= 2000)
subset(emp, emp$sal>= 2000, 
       c("ename","sal"))
emp[emp$sal>=2000,c("ename","sal")]

# select ename,sal from emp where sal between 2000 and 3000
subset(emp, select=c("ename","sal"), subset=(sal>=2000 & sal<=3000))
emp[emp$sal>=2000 & emp$sal <=3000, c("ename","sal")]


#논리연산자로 대답해준다.
y <- c(0,25,50,75,100)
z <- c(50, 50, 50, 50,50)
y == z
y != z
y > z
y < z
y >= z
y <= z
y == 50 # c(50, 50, 50, 50, 50) #작은애를 큰애한테 맞춘다.
y > 50

num1 <- 11 # c(11)
num2 <- 3  # c(3)
num1 / num2
num1 %% num2 #나머지    %%
num1 %/% num2 #몫       %/%
