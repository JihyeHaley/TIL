package naverapp;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
public class AppExam {
	
    public static void main(String[] args) throws Exception {
    	
    	Class.forName("oracle.jdbc.driver.OracleDriver");
    	Connection conn = DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:XE","pmkim","pmkimbear");
    	Statement stmt = conn.createStatement();
    	ResultSet rs = stmt.executeQuery("select good_name,good_price from goods where rownum <= 10");
    	
    	while(rs.next()) {
    		System.out.println(Integer.parseInt(rs.getString(2).replace(",", "")));
    	}
 
    	/*
    	CartDAO cdao = new CartDAO();
    	List<GoodsEventShopMemberVO> list = new ArrayList<GoodsEventShopMemberVO>();
        list = cdao.goodsAll();
        */
    	
    }
}
