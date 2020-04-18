install.packages("KoNLP")
# 패키지 설치가 잘 됩니까요?ㅜㅜ
# 2020.04.16 현재 안됩니다요...ㅜㅜ
# 강사컴의 KoNLP.zip을 복사해서 사용합니다.
# KoNLP.zip의 압축을 해제하고 생성된 KoNLP폴더를
# C:\Users\student\Documents\R\win-library\3.6 에
# 복사합니다.
# 그리고 나서 다음에 제시된 패키지들을 하나하나
# 설치합니다.
install.packages("Sejong")
install.packages("hash")
install.packages("rJava")
install.packages("tau")
install.packages("RSQLite")
install.packages("devtools")
install.packages("Rcpp")
# KoNLP 로드

library(KoNLP)

# 한번 수행하면 더 이상 수행할 필요가 없어용(오래 걸려)
useSystemDic()
useSejongDic()
useNIADic()

word_data <- readLines("book/애국가(가사).txt")
word_data

word_data2 <- sapply(word_data, extractNoun, USE.NAMES = F)
word_data2

word_data3 <- extractNoun(word_data)
word_data3

add_words <- c("백두산", "남산", "철갑", "가을", "달")
buildDictionary(user_dic=data.frame(add_words, rep("ncn", length(add_words))), replace_usr_dic=T)

word_data3 <- extractNoun(word_data)
word_data3

undata <- unlist(word_data3)
undata

word_table <- table(undata)
word_table

undata2 <- Filter(function(x) {nchar(x) >= 2}, undata)
word_table2 <- table(undata2)
word_table2

final <- sort(word_table2, decreasing = T)

head(final, 10)

extractNoun("대한민국의 영토는 한반도와 그 부속도서로 한다")
SimplePos22("대한민국의 영토는 한반도와 그 부속도서로 한다")
SimplePos09("대한민국의 영토는 한반도와 그 부속도서로 한다")



# 워드 클라우드
install.packages("wordcloud")
library(wordcloud)
install.packages("wordcloud2")
library(wordcloud2)


(words <- read.csv("data/wc.csv",stringsAsFactors = F))
head(words)
?windowsFonts
windowsFonts(lett=windowsFont("휴먼옛체"))
wordcloud(words$keyword, words$freq,family="lett")
wordcloud(words$keyword, words$freq, 
          min.freq = 2,            #최소 개수가 n 개 이사인 것 만 출력하겠어
          random.order = TRUE,    #출력 하는 위치가 랜덤
          rot.per = 0.5,          #rot.per -> rotation 가로새로
          scale = c(4, 0.3),        #출력된느 폰트의 크기     
          colors = rainbow(7))
wordcloud2(words, fontFamily = "휴먼옛체")
wordcloud2(words,rotateRatio = 1)
wordcloud2(words,rotateRatio = 0.5)
wordcloud2(words,rotateRatio = 0)
wordcloud2(words,size=0.5,col="random-dark")
wordcloud2(words,size=0.5,col="random-dark", figPath="book/peace.png")
wordcloud2(words,size=0.7,col="random-light",backgroundColor = "black")
wordcloud2(data = demoFreq)
wordcloud2(data = demoFreq, shape = 'diamond')
wordcloud2(data = demoFreq, shape = 'star')
wordcloud2(data = demoFreq, shape = 'cardioid')
wordcloud2(data = demoFreq, shape = 'triangle-forward') #모양을 정할 수 있따.
wordcloud2(data = demoFreq, shape = 'triangle')
result<-wordcloud2(data = demoFreq, shape = 'pentagon')
library("htmlwidgets")
saveWidget(result,"tmpwc.html",selfcontained = F)
head(demoFreq)
str(demoFreq)

# 트위터 글 워드클라우드
library(rtweet) 
appname <- "edu_data_collection"
api_key <- "RvnZeIl8ra88reu8fm23m0bST"
api_secret <- "wTRylK94GK2KmhZUnqXonDaIszwAsS6VPvpSsIo6EX5GQLtzQo"
access_token <- "959614462004117506-dkWyZaO8Bz3ZXh73rspWfc1sQz0EnDU"
access_token_secret <- "rxDWfg7uz1yXMTDwijz0x90yWhDAnmOM15R6IgC8kmtTe"
twitter_token <- create_token(
  app = appname,
  consumer_key = api_key,
  consumer_secret = api_secret,
  access_token = access_token,
  access_secret = access_token_secret)

key <- "취업"
key <- enc2utf8(key)
result <- search_tweets(key, n=100, token = twitter_token)
str(result)
content <- result$retweet_text
content <- gsub("[[:lower:][:upper:][:digit:][:punct:][:cntrl:]]", "", content)   

word <- extractNoun(content)
cdata <- unlist(word)
cdata

cdata <- Filter(function(x) {nchar(x) < 6 & nchar(x) >= 2} ,cdata)
wordcount <- table(cdata) 
wordcount <- head(sort(wordcount, decreasing=T),30)

par(mar=c(1,1,1,1))
wordcloud(names(wordcount),freq=wordcount,scale=c(3,0.5),rot.per=0.35,min.freq=1,
          random.order=F,random.color=T,colors=rainbow(20))

