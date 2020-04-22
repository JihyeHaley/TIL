package rjavaapp;

import org.rosuda.REngine.REXP;
import org.rosuda.REngine.REXPMismatchException;
import org.rosuda.REngine.REngineException;
import org.rosuda.REngine.RList;
import org.rosuda.REngine.Rserve.RConnection;

public class JavaRLab2 {

	public static void main(String[] args) throws REXPMismatchException, REngineException {
		RConnection rc = new RConnection();
		REXP x = rc.eval("imsi<-source"
				+ "('C:/HaleyDeveloper/Rstudy/lab.R'); "
				+ "imsi$value");
		RList list = x.asList();
		int size = list.size(); // 행의 개수 
		int length = list.at(0).length();
		int arrayRows = size;
		int arrayCols = length;
		
		//10행 2열 
		String[][] full = new String[arrayRows][2]; // 데이터프레임의 변수 갯수로 행의 크기를 정한다.
		
		
		for (int i = 0; i < arrayRows; i++) {
			full[i] = list.at(i).asStrings();
		}
		
		System.out.println("R 이 보내온 최빈 명사들 : ");
		for (int i = 0; i < arrayRows; i++) {
			for (int j = 0; j < arrayCols; j++) {
				System.out.print(full[i][j] + "\t");
			}
			System.out.println();
		}
		rc.close();
	}
}
