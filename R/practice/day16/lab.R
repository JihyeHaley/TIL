hotel<-readLines('c:/HaleyDeveloper/Rstudy/hotel.txt')
library(KoNLP)
library(dplyr)
hotel %>%
  extractNoun %>%
  unlist %>%
  gsub("[[:punct:]]", "",.) %>%
  gsub("[a-zA-Z]","",.) %>%
  Filter(function(x){nchar(x)>=2},.)%>%
  table %>%
  sort (decreasing=T)%>%
  head(10)%>%
  data.frame->hotel2
colnames(hotel2)<- c("noun","freq")
hotel2
