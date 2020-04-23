#문제1
v1<- c(1:10)
v2<- v1*2
max_v <- max(v2)
min_V <- min(v2)
avg_v <- mean(v2)
sum_v <- sum(v2)
v3<-v2[-5]
v1; v2; v3; max_v; min_V; avg_v; sum_v

#문제2
v4<- seq(1,9,2)
v5<- rep(1, 5)
v6<- rep(1:3, 3)
v7<- rep(1:4, each=2)

#문제3
nums <- sample(1:100, 10)
sort(nums)
nums <-rev(sort(nums)) #sort(nums, decreasing=T)
nums[nums>50]
which(nums <= 50)
which.max(nums)
which.min(nums)

#문제4
v8 <- seq(1,10,3)
names(v8) <- LETTERS[1:4]

#문제5
score<- sample(1:20, 5)
myFriend<- c("둘리", "또치", "도우너", "희동", "듀크")
paste(score, myFriend, sep = "-")# sep이 없으면 blank,
paste0(score, myFriend)# paste0은 다닥다박 붙어서 unless sep
myFriend[which.max(score)]
myFriend[which.min(score)]
myFriend[which(score>10)]
