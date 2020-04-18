#R studying
v1 <- c(4, 1, 8, 6, 10)
print(v1) 
#간격을 조정하려면 argument줘서 해결
v1 
#변수명만 실행시키면 자동적으로 print함수 적용된다.

?rep
rep(1, 100)
rep(1:3, 5)
rep(1:3, times=5) #keyword parameter
rep(1:3, each=5)

LETTERS
letters
month.name
month.abb
pi

LETTERS;letters;month.name;month.abb;pi

LETTERS[1]; LETTERS[c(1)]; 
LETTERS[3:5]; LETTERS[5:3];
LETTERS[-1]; LETTERS[c(-2,-4)] #빼고 다 출력 

length(LETTERS)
length(month.name)
length(pi)


x <- c(10,2,7,4,15)
x
print(x)
class(x)
rev(x)  #거꾸로
range(x) # 최소 최대 
sort(x) #x 함수에는 변화가 없을 것.
sort(x, decreasing = TRUE)
sort(x, decreasing = T)
#x <- sort(x) # 함수에 다시 담을 수 있다.
order(x) #인덱스 넘버로 최대 최소를 순서대로 표현해준다.
?order


x[3] <- 20
x
x + 1
x <- x + 1
max(x);min(x);mean(x);sum(x)
summary(x) #원소의 타입에 따라서 summary의 기준은 모두 다르다!

x[c(2,4)] # x[2], x[4]
x[c(F,T,F,T,F)] #인덱스랑 MACHING해서 TRUE만 꺼낸다!
x[c(T,F)] # 반복
x > 5 #원소마다 숫자가 5보다 크면 True 작으면 False (논리형으로 답변)
x[x > 5] # TFTFT로 되어 있어서 그 조건을 만족하는 원소값을 꺼낸다.
          #TFTFT가 x>5 라서
x[x > 5 & x < 15] #&& 두개 연산자를 쓰면 안된다.
                  #&& 는 값이 한개 있을때 비교할 때 쓴다.
#x[x > 5 | x < 15]

names(x) #원소마다 이름이 부여되어 있는 vector
names(x) <- LETTERS[1:5] #대문자 ABCD
names(x) <- NULL #적용을 취소시키는 
x[2] # 
x["B"] # NA 


# &, &&
c(T, T, F, F) & c(T, F, T, F)
c(T, T, F, F) | c(T, F, T, F)
c(T, T, F, F) && c(T, F, T, F)
c(T, T, F, F) || c(T, F, T, F)


ls() #method 개수
rm(x) #remove
x
class(x)

rainfall <- c(21.6, 23.6, 45.8, 77.0, 
              102.2, 133.3,327.9, 348.0, 
              137.6, 49.3, 53.0, 24.9)
names(rainfall) <- LETTERS[1:12]
rainfall > 100 #논리형으로 답변
rainfall[rainfall > 100] #해당하는 것을 값을 출력한다.

which(rainfall > 100) # 해당하는 인덱스 값을 보여준다.
month.name[which(rainfall > 100)]
month.abb[which(rainfall > 100)]

month.korname <- c("1월","2월","3월",
                   "4월","5월","6월",
                   "7월","8월","9월",
                   "10월","11월","12월")
month.korname[which(rainfall > 100)]

which.max(rainfall)
which.min(rainfall)
month.korname[which.max(rainfall)]
month.korname[which.min(rainfall)]


sample(1:20, 3) # 몇 개 꺼낼건지?
sample(1:45, 6)
sample(1:10, 7)
sample(1:10, 7, replace=T)

count <- sample(1:100,7)
month.korname <- c("일요일", "월요일", "화요일",
                   "수요일", "목요일", 
                   "금요일", "토요일")

paste(month.korname, count, sep = ":") #sep 의 default는 공백
#paste함수는 문자형을 결합할 때 사용한다. 
month.korname[which.max(count)]
month.korname[which.min(count)]
month.korname[which(count > 50)]

paste(month.korname, count, sep = " : ")

paste("I'm","Duli","!!") #sep를 주지 않으면 모두 결합해버린다.
paste("I'm","Duli","!!", sep="")
paste0("I'm","Duli","!!") #paste0은 space가 없다.

fruit <- c("Apple", "Banana", "Strawberry")
food <- c("Pie","Juice", "Cake")
paste(fruit, food)

paste(fruit, food, sep="")
paste(fruit, food, sep=":::")
paste(fruit, food, sep="", collapse="-") #여러 컬럼들을 하나의 문자열로 만든다.
paste(fruit, food, sep="", collapse="")
paste(fruit, food, collapse=",")
