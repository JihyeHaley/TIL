package rjavaapp;

import org.rosuda.REngine.REXPMismatchException;
import org.rosuda.REngine.REngineException;
import org.rosuda.REngine.Rserve.RConnection;

public class JavaRLab1 {
	public static void main(String[] args) throws REXPMismatchException, REngineException {
		RConnection rc = new RConnection(); 
		rc.eval("hotel<-readLines('C:/HaleyDeveloper/Rstudy/hotel.txt')");
		rc.eval("library(KoNLP)");
		rc.eval("library(dplyr)");
		rc.eval("hotel %>% extractNoun %>% unlist %>% gsub(\"[[:punct:]]\", \"\",.) %>% gsub(\"[a-zA-Z]\",\"\",.) %>% Filter(function(x){nchar(x)>=2},.) %>% table %>% sort (decreasing=T) %>% head(10) -> hotel2");	
		
		String[] xlist = rc.eval("names(hotel2)").asStrings(); 
		
		System.out.print("R 이 보내온 최빈 명사들 : ");
		
		for (int i = 0; i < xlist.length; i++) {
			if(i!=xlist.length-1)
				System.out.print(xlist[i] + ",");
			else
				System.out.print(xlist[i]);
		}
		rc.close();

	}

}
