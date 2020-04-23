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

