hotel<-readLines('hotel.txt')
hotel
getwd()
library(KoNLP)

hotel %>%
  extractNoun %>%
  unlist %>%
  gsub("[[:punct:]]", "",.) %>%
  gsub("[a-zA-Z]","",.) %>%
  Filter(function(x){nchar(x)>=2},.)%>%
  table %>%
  sort (decreasing=T)%>%
  head(10)->hotel2
colnames(hotel2)<- c("noun","freq")
View(hotel2)


View(readLines('c:/HaleyDeveloper/Rstudy/hotel.txt'))
