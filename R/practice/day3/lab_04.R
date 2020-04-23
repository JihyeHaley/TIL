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
