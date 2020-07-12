#문제1

str(airquality)
dim(airquality) #행, 열의 개수만 볼려면면

#문제2

x <- 1:5
y <-seq(2,10,2)
df1 <- data.frame(x,y)
colnames(df1) <- c('x','y')
rownames(df1) <- c(1,2,3,4,5)
df1


#문제3
col1 <- c(1,2,3,4,5)
col2 <- c('a', 'b','c','d','e')
col3 <- seq(6,10,1)
df2 <- data.frame(col=1:5, col2=letters[1:5], col3=seq(6,10,1))
df2<-data.frame(col1, col2, col3)

#문제4
df3 <- data.frame(
  제품명=c('사과', '딸기', '수박'), 
  가격=c(1800, 1500, 3000), 
  판매량=c(24,38,13), stringAsFactors=F) #자동으로 팩터형으로 바뀌니깐.

#문제5
mean(df3$가격)
mean(df3$판매량)

#문제6
df4 <-data.frame(
  name=c("Potter", "Elsa", "Gates", "Wendy", "Ben"), 
  gender=c(factor(c("M","F","M","F","M"))),
  math=c(85,76,99,88,40))

is.character(name); is.factor(gender); is.numeric(math)
df4$stat=c(76, 73, 95, 82, 35)

df4$score=df4$math+df4$stat

df4$grade=ifelse(df4$score>=150, 'A', 
                 ifelse(df4$score>=100, 'B',
                        ifelse(df4$score>=70, 'C','D')))

#문제7
str(emp)

#문제8
emp[c(3,4,5),]

#문제9
emp[,"ename",drop=F] 

#문제10
emp[,c("ename","sal"),drop=F] 

#문제11
subset(emp, select=c('ename', 'sal', 'job'), subset=(emp$job=="SALESMAN"))

#문제12
subset(emp, select=c('ename', 'sal', 'empno'), subset=(sal>=1000 & sal<=3000))
subset(emp, select=c('ename', 'sal', 'empno'), subset=(emp$sal>=1000 & sal<=3000))

#문제13
subset(emp, select=c('ename', 'job', 'sal'), subset=(emp$job!='analyst'))


#문제14??
subset(emp, select=c('ename', 'job'), subset=(emp$job =="salesman" | emp$job=="analyst"))       
emp[emp$job=="salesman" & emp$job =="analyst", c("ename","sal")]

#문제15
subset(emp,select=c('ename','sal'),is.na(emp$comm)) 

subset(emp, is.na(comm), c(ename, job))

#문제16 ??
emp[order(emp$sal, decreasing=F),]

## 문제 16번 응용 
sort(emp$sal)
order(emp$sal) #index로 추출
