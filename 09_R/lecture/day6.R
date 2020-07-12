# 정규표현식 사용
word <- "JAVA javascript Aa 가나다 AAaAaA123 %^&*"
gsub("", "", word)
gsub("A", "", word) 
gsub("a", "", word) 
gsub("Aa", "", word) 
gsub("(Aa)", "", word) 
gsub("(Aa){2}", "", word) #?? matches exactly 2 times
gsub("[Aa]", "", word) 
gsub("[가-힣]", "", word) 
gsub("[^가-힣]", "", word) #??
gsub("[&^%*]", "", word) 
gsub("[[:punct:]]", "", word) 
gsub("[[:alnum:]]", "", word) #[A-z0-9]
gsub("[1234567890]", "", word) #[[:digit]] = \\d 
gsub("[0-9]", "", word) #[[:digit]] = \\d 
gsub("\\d", "", word) #[[:digit]] = \\d 
gsub("[[:digit:]]", "", word) #[[:digit]] = \\d 
gsub("[^[:alnum:]]", "", word) #???
gsub("[[:space:]]", "", word) 


#selenium 설치
install.packages("RSelenium")
library(RSelenium)

remDr <- remoteDriver(remoteServerAddr = "localhost",
                      port=4445, browserName="chrome")
remDr$open()

remDr$navigate("http://www.google.com/")

#입력하기 강제로
webElem <- remDr$findElement(using="css", "[name='q']")
webElem$sendKeysToElement(list("JAVA", key="enter"))

naver<- ("http://www.naver.com/")
remDr$navigate(naver) #페이지 랜더링링
webElem<- remDr$findElement(using="css", "[name='query']")
webElem$sendKeysToElement(list("연세대학교", key="enter"))

remDr$navigate("http://www.selenium.dev/")



# [ 네이버 웹툰 댓글 읽기 ]
url<-'http://comic.naver.com/comment/comment.nhn?titleId=570503&no=135'
remDr$navigate(url)

#단수형으로 노드 추출
more<-remDr$findElement(using='css','#cbox_module > div > div.u_cbox_sort > div.u_cbox_sort_option > div > ul > li:nth-child(2) > a')
more$getElementTagName()
more$getElementText()
more$clickElement() #CLICK EVENT 강제발생

# 2페이지부터 10페이지까지 링크 클릭하여 페이지 이동하기 
for (i in 4:12) {
  nextCss <- paste0("#cbox_module>div>div.u_cbox_paginate>div> a:nth-child(",i,") > span")
  nextPage<-remDr$findElement(using='css',nextCss)
  nextPage$clickElement()
  Sys.sleep(2)
}

#복수형으로 노드 추출 
url<-'http://comic.naver.com/comment/comment.nhn?titleId=570503&no=135'
remDr$navigate(url)

#베스트 댓글 내용 읽어오기
bestReviewNodes<-remDr$findElements(using ="css selector","ul.u_cbox_list span.u_cbox_contents")
sapply(bestReviewNodes,function(x){x$getElementText()})

#전체 댓글 링크 클릭후에 첫 페이지 내용 읽어오기
totalReview <- remDr$findElement(using='css','#cbox_module > div > div.u_cbox_sort > div.u_cbox_sort_option > div > ul > li:nth-child(2) > a')
totalReview$clickElement()
totalReviewNodes<-remDr$findElements(using ="css selector","ul.u_cbox_list span.u_cbox_contents")
sapply(totalReviewNodes,function(x){x$getElementText()})
