k2 <- korpopmap2
k3 <- korpopmap3
k2@data[c("C행정구역별_읍면동", "행정구역별_읍면동")] #변수명만 줘도 works 
k3@data[c("C행정구역별_읍면동", "행정구역별_읍면동")]

# 서대문구의 구코드 출력
k2@data[k2@data$C행정구역별_읍면동 == '11130', 
        c("C행정구역별_읍면동", "행정구역별_읍면동")]

# 서대문구에 속한 동의 코드 출력 --> 추출됨
seodong<-k3@data[grep('^11130', k3@data$C행정구역별_읍면동),  #SO, grep을 활용해서 !!!!! 올려버려!!
        c("C행정구역별_읍면동", "행정구역별_읍면동")]
View(seodong)

# 서대문구의 동 뽑기 
seoname <- '서대문구'

seogucode <- k2@data[k2@data$name == seoname, "code.data"]
pattern <- paste0('^', seogucode)


k3@data<-k3@data[grep(pattern, k3@data$code.data),]
k3@polygons<-k3@polygons[grep(pattern, k3@data$code.data)] 

View(k3@data)
# 서대문구구 데이터만 뽑음
#k3@data<-k3@data[c(193:207),] 


k3@data$name<-gsub('·','',k3@data$name)  #동에있는 -데이터 없애기
colnames(DONG)<-c('구별','name','일인가구')
dong <- DONG %>%filter(구별=='서대문구')

k3@data<-merge(k3@data,dong,by.x='name',sort=FALSE)
mymap <- k3@data
#mypalette <- colorNumeric(palette ='RdYlBu' , domain = k3@data$'일인가구')
#mypalette <- colorNumeric(palette ='PuRd' , domain = k3@data$'일인가구')
mypalette <- colorNumeric(palette ='Set3' , domain = k3@data$'일인가구')
mypopup <- paste0(mymap$name,'<br> 1인가구: ',k3@data$'일인가구')

map9 <- NULL
map9<-leaflet(k3) %>% 
  addTiles() %>% 
  setView(lat=37.52711, lng=126.987517, zoom=12) %>%
  addPolygons(stroke =FALSE,
              fillOpacity = 0.7,
              popup = mypopup,
              color = ~mypalette(k3@data$일인가구)) %>% 
  addLegend( values = ~k3@data$일인가구,
             pal = mypalette ,
             title = '인구수',
             opacity = 1)
map9		 #한 지역에 관한 가구수를 뽑아 내기 위해서 
saveWidget(map9, file="oneMap.html")
