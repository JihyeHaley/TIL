install.packages('ggplot2')
library(ggplot2)
p1 <- ggplot(data = iris, aes(x = Petal.Width, y= Petal.Length, col=Species)) + geom_point()
p2 <- ggplot(data = iris, aes(x = Sepal.Width, y= Sepal.Length, col=Species)) + geom_point() 
install.packages('gridExtra')
library(gridExtra)
grid.arrange(p1, p2, nrow = 1)


# 지도 시각화
install.packages("ggmap")
library(ggmap)
register_google(key='AIzaSyD8k2DWC_7yFHCrH6LDR3RfITsmWMEqC8c')

lon <- 126.9221322
lat <- 37.5268831
cen <- c(lon,lat)
mk <- data.frame(lon=lon, lat=lat)
map <- get_googlemap(center=cen, maptype="roadmap",zoom=1, marker=mk) #이 센터를 기준으로 한
Sys.sleep(1)
ggmap(map)
map <- get_googlemap(center=cen, maptype="roadmap",zoom=5, marker=mk)
Sys.sleep(1)
ggmap(map)
map <- get_googlemap(center=cen, maptype="roadmap",zoom=10, marker=mk)
Sys.sleep(1)
ggmap(map)
map <- get_googlemap(center=cen, maptype="roadmap",zoom=15, marker=mk)
Sys.sleep(1)
ggmap(map)
map <- get_googlemap(center=cen, maptype="satellite",zoom=16, marker=mk)
Sys.sleep(1)
ggmap(map)
map <- get_googlemap(center=cen, maptype="terrain",zoom=8, marker=mk)
Sys.sleep(1)
ggmap(map)
map <- get_googlemap(center=cen, maptype="terrain",zoom=12, marker=mk)
Sys.sleep(1)
ggmap(map)
map <- get_googlemap(center=cen, maptype="hybrid",zoom=16, marker=mk)
Sys.sleep(1)
ggmap(map)+labs(title="테스트임", x="경도", y="위도")

map <- get_map(location=cen, maptype="toner",zoom=12, marker=mk, source="google")
ggmap(map)
map <- get_map(location=cen, maptype="watercolor",zoom=12, marker=mk, source="stamen")
ggmap(map)
map <- get_map(location=cen, maptype="terrain-background",zoom=12, marker=mk, source="stamen")
ggmap(map)
map <- get_map(location=cen, maptype="roadmap",zoom=12, marker=mk, source="stamen")
ggmap(map)
map <- get_map(location=cen, maptype="terrain",zoom=12, marker=mk, source="stamen")
ggmap(map)
#map <- get_map(location=cen, maptype="roadmap",zoom=12, marker=mk, source="naver")
#ggmap(map)
#map <- get_map(location=cen, maptype="roadmap",zoom=12, marker=mk, source="osm")
#ggmap(map)


mk <- geocode("seoul", source = "google")
print(mk)
cen <- c(mk$lon, mk$lat)
map <- get_googlemap(center=cen, maptype="roadmap",zoom=11, marker=mk)
ggmap(map)
mk <- geocode(enc2utf8("부산"), source = "google")
cen <- c(mk$lon, mk$lat)
map <- get_googlemap(center=cen, maptype="roadmap",zoom=11, marker=mk)
ggmap(map)
multi_lonlat <- geocode(enc2utf8("강남구 역삼동 테헤란로 212"), source = "google")
mk <- multi_lonlat
cen <- c(mk$lon, mk$lat)
map <- get_googlemap(center=cen, maptype="roadmap",zoom=16)
ggmap(map) + 
  geom_point(aes(x=mk$lon, y=mk$lat), alpha=0.4, size=5, color="pink") +
  geom_text(aes(x=mk$lon, y=mk$lat, label="우리가 공부하는 곳", vjust=0, hjust=0))


# 제주도

names <- c("용두암","성산일출봉","정방폭포",
           "중문관광단지","한라산1100고지","차귀도")
addr <- c("제주시 용두암길 15",
          "서귀포시 성산읍 성산리",
          "서귀포시 동홍동 299-3",
          "서귀포시 중문동 2624-1",
          "서귀포시 색달동 산1-2",
          "제주시 한경면 고산리 125")
gc <- geocode(enc2utf8(addr))
gc

df <- data.frame(name=names,
                 lon=gc$lon,
                 lat=gc$lat)
cen <- c(mean(df$lon),mean(df$lat))
map <- get_googlemap(center=cen,
                     maptype="roadmap",
                     zoom=10,
                     size=c(640,640),
                     marker=gc)
ggmap(map) 

ggmap(map) + geom_text(data=df,               
                       aes(x=lon,y=lat,colour="magenta"),               
                       size=3,                
                       label=df$name) + guides(color=F)



# 공공 DB 활용 

install.packages("XML")
library(XML)
API_key  <- "%2BjzsSyNtwmcqxUsGnflvs3rW2oceFvhHR8AFkM3ao%2Fw50hwHXgGyPVutXw04uAXvrkoWgkoScvvhlH7jgD4%2FRQ%3D%3D"
bus_No <- "472"
url <- paste("http://ws.bus.go.kr/api/rest/busRouteInfo/getBusRouteList?ServiceKey=", API_key, "&strSrch=", bus_No, sep="")
doc <- xmlParse(url)
top <- xmlRoot(doc) ; top
df <- xmlToDataFrame(getNodeSet(doc, "//itemList[1]")); df
busRouteId <- df$busRouteId
busRouteId
url <- paste("http://ws.bus.go.kr/api/rest/buspos/getBusPosByRtid?ServiceKey=", API_key, "&busRouteId=", busRouteId, sep="")
doc <- xmlParse(url)
top <- xmlRoot(doc); top
df <- xmlToDataFrame(getNodeSet(doc, "//itemList")); df
# 구글 맵에 버스 위치 출력
df$gpsX <- as.numeric(as.character(df$gpsX))
df$gpsY <- as.numeric(as.character(df$gpsY))
gc <- data.frame(lon=df$gpsX, lat=df$gpsY);gc
cen <- c(mean(gc$lon), mean(gc$lat))
map <- get_googlemap(center=cen, maptype="roadmap",zoom=12, marker=gc)
ggmap(map)


library(dplyr)
library(ggmap)
library(ggplot2)

geocode('Seoul', source = 'google')
geocode('Seoul', source = 'google', output = 'latlona')
geocode(enc2utf8('서울'), source = 'google')
geocode(enc2utf8('서울'), source = 'google', output = 'latlona')
geocode(enc2utf8('서울&language=ko'), source = 'google', output = 'latlona')

#mutate_geocode(data.frame, address_column_name, source = 'google')
station_list = c('시청역', '을지로입구역', '을지로3가역', '을지로4가역', 
                 '동대문역사문화공원역', '신당역', '상왕십리역', '왕십리역', '한양대역', 
                 '뚝섬역', '성수역', '건대입구역', '구의역', '강변역', '잠실나루역', 
                 '잠실역', '신천역', '종합운동장역', '삼성역', '선릉역', '역삼역', 
                 '강남역', '2호선 교대역', '서초역', '방배역', '사당역', '낙성대역', 
                 '서울대입구역', '봉천역', '신림역', '신대방역', '구로디지털단지역', 
                 '대림역', '신도림역', '문래역', '영등포구청역', '당산역', '합정역', 
                 '홍대입구역', '신촌역', '이대역', '아현역', '충정로역')
station_df = data.frame(station_list, stringsAsFactors = FALSE)
station_df$station_list = enc2utf8(station_df$station_list)
# 다음 행은 한번만 수행시키셩
station_lonlat = mutate_geocode(station_df, station_list, source = 'google')
station_lonlat
save(station_lonlat, file="station_lonlat.rda")
#load("station_lonlat.rda")

seoul_lonlat = unlist(geocode('seoul', source = 'google'))
?qmap

qmap('seoul', zoom = 11)
qmap(seoul_lonlat, zoom = 11, source = 'stamen', maptype = 'toner')
seoul_map <- qmap('Seoul', zoom = 11, source = 'stamen', maptype = 'toner')
seoul_map + geom_point(data = station_lonlat, aes(x = lon, y = lat), colour = 'green',
                       size = 4)



# 지도 응용
df <- read.csv("data/전국전기차충전소표준데이터.csv", stringsAsFactors=F)       
str(df)
head(df)
df_add <- df[,c(13, 17, 18)]
names(df_add) <- c("address", "lat", "lon")
View(df_add)

map_korea <- get_map(location="southKorea", zoom=7, maptype="roadmap") 
ggmap(map_korea)+geom_point(data=df_add, aes(x=lon, y=lat), alpha=0.5, size=2, color="red")

map_seoul <- get_map(location="seoul", zoom=11, maptype="roadmap")       
ggmap(map_seoul)+geom_point(data=df_add, aes(x=lon, y=lat), alpha=0.5, size=5, color="blue")


#leaflet 그리기

install.packages("leaflet")
library(leaflet)
library(dplyr)
library(ggmap)

seoul_lonlat<-geocode("seoul")

# 지도 배경 그리기 

leaflet()

# 지도 배경에 타일깔기
leaflet() %>% addTiles() 

# 지도 배경에 센터 설정하기
map0 <- leaflet() %>% setView(lng = seoul_lonlat$lon, lat = seoul_lonlat$lat, zoom = 16)  
map0

# 지도 배경에 센터 설정하고 타일깔기
map1 <- map0 %>% addTiles() 
map1

mk <- multi_lonlat
lon <- mk$lon
lat <- mk$lat
msg <- '<strong><a href="http://www.multicampus.co.kr" style="text-decoration:none" >멀티캠퍼스</a></strong><hr>우리가 공부하는 곳 ㅎㅎ'
map2 <- leaflet() %>% setView(lng = mk$lon, lat = mk$lat, zoom = 1) %>% addTiles() %>% 
  addCircles(lng = lon, lat = lat, color='green', popup = msg )
map2

map2 <- leaflet() %>% setView(lng = mk$lon, lat = mk$lat, zoom = 18) %>% addTiles() %>% 
  addCircles(lng = lon, lat = lat, color='green', popup = msg )
map2

map2 <- leaflet() %>% setView(lng = mk$lon, lat = mk$lat, zoom = 5) %>% addTiles() %>% 
  addCircles(lng = lon, lat = lat, color='green', popup = msg )
map2

map2 <- leaflet() %>% setView(lng = mk$lon, lat = mk$lat, zoom = 1) %>% addTiles() %>% 
  addCircles(lng = lon, lat = lat, color='green', popup = msg )
map2


content1 <- paste(sep = '<br/>',"<b><a href='https://www.seoul.go.kr/main/index.jsp'>서울시청</a></b>",'아름다운 서울','박원순 시장님 화이팅!!')
map3<-leaflet() %>% addTiles() %>%  addPopups(126.97797, 37.56654, content1, options = popupOptions())
map3

content2 <- paste(sep = '<br/>',"<b><a href='http://www.snmb.mil.kr/mbshome/mbs/snmb/'>국립서울현충원</a></b>",'1955년에 개장', '2013년 ‘서울 미래유산’으로 등재')
map3<-leaflet() %>% addTiles() %>%  addPopups(c(126.97797, 126.97797),  c(37.56654, 37.50124) , c(content1, content2), options = popupOptions(closeButton = FALSE) )
map3

wifi_data = read.csv('data/wifi_data.csv', encoding = 'utf-8', stringsAsFactors = FALSE)
View(wifi_data)
leaflet(wifi_data) %>% 
  setView(lng = seoul_lonlat[1], 
          lat = seoul_lonlat[2], 
          zoom = 11) %>% 
  addTiles() %>% 
  addCircles(lng = ~lon, lat = ~lat)


leaflet(wifi_data) %>% 
  setView(lng = seoul_lonlat[1], lat = seoul_lonlat[2], zoom = 11) %>% 
  addProviderTiles('Stamen.Toner') %>% 
  addCircles(lng = ~lon, lat = ~lat)


leaflet(wifi_data) %>% 
  setView(lng = seoul_lonlat[1], lat = seoul_lonlat[2], zoom = 11) %>% 
  addProviderTiles('CartoDB.Positron') %>% 
  addCircles(lng = ~lon, lat = ~lat)

leaflet(wifi_data) %>% 
  setView(lng = seoul_lonlat[1], lat = seoul_lonlat[2], zoom = 11) %>% 
  addProviderTiles('Stamen.Toner') %>% 
  addCircles(lng = ~lon, lat = ~lat, popup = ~div)
?colorFactor

telecom_color = colorFactor('Set1', wifi_data$div)
telecom_color(wifi_data$div)
str(telecom_color)
mode(telecom_color)

leaflet(wifi_data) %>% 
  setView(lng = seoul_lonlat[1], lat = seoul_lonlat[2], zoom = 11) %>% 
  addProviderTiles('Stamen.Toner') %>% 
  addCircles(lng = ~lon, lat=~lat, popup = ~div, color = ~telecom_color(div))
