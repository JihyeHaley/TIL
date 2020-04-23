#문제1
vec <- seq(10,38, 2)

m1 <-matrix(vec, nrow=3, byrow=TRUE)
m1 <- matrix(seq(10,38, 2), nrow=3, byrow=TRUE); m1

m2 <- m1+100

m_max_v <- max(m1)
m_min_v <- min(m1)
row_max <- apply(m1, 1, max)
col_max <- apply(m1, 2, max)

m_max_v; m_min_v; row_max; col_max

#문제2
n1 <-c(1,2,3)
n2 <-c(4,5,6)
n3 <-c(7,8,9)

m2<-cbind(n1,n2,n3); colnames(m2) <- NULL; m2

#문제3

m3 <- matrix(1:9, nrow=3, byrow=TRUE); m3

#문제4

rownames(m3) <- c("row1", "row2", "row3")
colnames(m3) <- c("col1", "col2", "col3")
m4<- m3 ;m4

#문제5
a<- letters[1:6]
alpha <- matrix(a, nrow=2); alpha

b<- c('x','y','z')
alpha2 <- rbind(alpha, b); rownames(alpha2) <- NULL; alpha2

c<- c('s', 'p')
alpha3 <- cbind(alpha2, c); colnames(alpha3)<-NULL; alpha3

#문제6
a<- array(1:24, dim=c(2,3,4))

a[2,3,4] 
a[2,,]
a[,1,] 
a[,3,]
a*100 
a[,,4]*100
a[1,2:3,] 
a<- a[2,,2]+100 
a<- a[,,1]-2 ;a
a<- a*10
rm(a)
