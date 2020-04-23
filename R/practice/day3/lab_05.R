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
