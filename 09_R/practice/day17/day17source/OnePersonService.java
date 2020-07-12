package rtest;

import org.rosuda.REngine.Rserve.RConnection;
import org.springframework.stereotype.Service;

@Service
public class OnePersonService {
	public String returnmap7(String path, String gu)  {
		RConnection r = null;
		String retStr = "";
		try {
			r = new RConnection();
			//System.out.println("start");
			r.eval("setwd('c:/HaleyDeveloper/Rstudy')");
			//System.out.println("test1");
			r.eval("library(Kormaps)");
			r.eval("library(dplyr)");
			r.eval("library(leaflet)");
			r.eval("library(htmlwidgets)");
			r.eval("DONG<-read.csv('data/one.csv')");
			r.eval("Encoding(names(korpopmap2)) <- 'UTF-8'");
			r.eval("Encoding(korpopmap2@data$name)<-'UTF-8'");
			r.eval("Encoding(korpopmap2@data$행정구역별_읍면동)<-'UTF-8'");
			
			r.eval("Encoding(names(korpopmap3)) <- 'UTF-8'");
			r.eval("Encoding(korpopmap3@data$name)<-'UTF-8'");
			r.eval("Encoding(korpopmap3@data$행정구역별_읍면동)<-'UTF-8'");
			
			
			r.eval("k3 <- korpopmap3");
			r.eval("guname <- '" + gu + "'");
			
			r.eval("gucodename<- korpopmap2@data[,c(\"name\",\"code.data\")]");
			r.eval("gucode <- gucodename[korpopmap2@data$name == guname, \"code.data\"]");
			r.eval("pattern <- paste0('^', gucode)");
			//System.out.println("test2");
			
			// grep : 이 데이터셋 안에 이 단어가 있는 것을 Index로 꺼내줌
			r.eval("k3@polygons <- k3@polygons[grep(pattern, k3@data$code.data)]");
			r.eval("k3@data <- k3@data[grep(pattern, k3@data$code.data),]");

			r.eval("k3@data$name <-gsub('·','',k3@data$name) ");
			r.eval("colnames(DONG)<-c('구별','name','일인가구')");
			//강동구 1인 가구 뽑기
			r.eval("dong <- DONG %>%filter(구별=='" + gu + "')");
			//System.out.println("test22");
			r.eval("guname <- iconv(guname, from='CP949', to='UTF-8')"); // iconv
			//System.out.println("test222");
			r.eval("k3@data<-merge(k3@data,dong,by.x='name',sort=FALSE)");
			r.eval("mymap <- k3@data");
			r.eval("mypalette <- colorNumeric(palette ='Set3' , domain = k3@data$'일인가구')");
			r.eval("mypopup <- paste0(mymap$name,'<br> 1인가구: ',k3@data$'일인가구')");
			r.eval("map7 <- NULL");
			//System.out.println("test3");
			r.eval("map7<-leaflet(k3) %>% " + 
					"			  addTiles() %>% " + 
					"			  setView(lat=37.52711, lng=126.987517, zoom=12) %>%" + 
					"			  addPolygons(stroke =FALSE," + 
					"			              fillOpacity = .7," + 
					"			              popup = mypopup," + 
					"			              color = ~mypalette(k3@data$'일인가구')) %>%" + 
					"			  addLegend( values = ~k3@data$'일인가구'," + 
					"			             pal = mypalette ," + 
					"			             title = '인구수'," + 
					"			             opacity = 1)");
			r.eval("map7");
			String fileName = path + "/index.html";
			System.out.println(path);
			r.eval("saveWidget(map7,'"+fileName+"',  selfcontained = F)");
			System.out.println("test5");
			retStr = r.eval("'index.html'").asString();
			System.out.println("test6");

		} catch (Exception e) {
			System.out.println(e);
			e.printStackTrace();
		} finally {
			r.close(); 
		}
		return retStr;
	}	
}

