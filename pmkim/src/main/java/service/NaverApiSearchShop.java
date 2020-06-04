	package service;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLEncoder;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.HashMap;
import java.util.Map;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

public class NaverApiSearchShop {
	//scheduling 으로 바꾸는거까지 하기
    public static void main(String[] args) throws Exception{
        String clientId = "FZqBsDALM8L8w7aa_vY5"; //애플리케이션 클라이언트 아이디값"
        String clientSecret = "RDK08h85bB"; //애플리케이션 클라이언트 시크릿값"

        String text = null;
        Map<String, String> requestHeaders = new HashMap<>();
        String responseBody = null;
        
        Class.forName("oracle.jdbc.driver.OracleDriver");
    	Connection conn = DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:XE","pmkim","pmkimbear");
    	Statement stmt = conn.createStatement(ResultSet.TYPE_SCROLL_INSENSITIVE,ResultSet.CONCUR_READ_ONLY);
    	PreparedStatement ptmt = conn.prepareStatement("insert into GOODS_CATEGORY values (?,?,?,?)");
    	ResultSet rs = stmt.executeQuery("select good_id, good_name from goods");
    	//rs.last();
    	//System.out.println(rs.getRow());
    
    	while(rs.next()) {
    		System.out.println(rs.getString(2));
        
	    	try {
	            text = URLEncoder.encode(rs.getString(2), "UTF-8");
	        } catch (UnsupportedEncodingException e) {
	        	System.out.println("kkkkkkkkkkk");
	            throw new RuntimeException("검색어 인코딩 실패",e);
	        }
	    	
	        String apiURL = "https://openapi.naver.com/v1/search/shop?query=" + text;    // json 결과
	        //String apiURL = "https://openapi.naver.com/v1/search/blog.xml?query="+ text; // xml 결과
	
	        requestHeaders.put("X-Naver-Client-Id", clientId);
	        requestHeaders.put("X-Naver-Client-Secret", clientSecret);
	        responseBody = get(apiURL,requestHeaders);
	        
	        //System.out.println(responseBody);
	        
	        try {
	        	JSONParser jsonParser = new JSONParser();
	        	JSONObject jsonObj = (JSONObject) jsonParser.parse(responseBody);
	            JSONArray itemsArray = (JSONArray) jsonObj.get("items");
	        	JSONObject tempObj;
	        	if(itemsArray.isEmpty()) {
	        		ptmt.setString(1, rs.getString(1));
		        	ptmt.setString(2, "기타");
		        	ptmt.setString(3, "기타");
		        	ptmt.setString(4, "기타");
	        	}else {
	        		/*
	        		System.out.println(itemsArray.getClass());
	        		if(itemsArray.isEmpty()) {
	        			System.out.println("Fail");
	        		}
	        		if(itemsArray.equals("[]")) {
	        			System.out.println("test");
	        		}
	        		System.out.println(itemsArray);
					*/
	        		tempObj = (JSONObject) itemsArray.get(0);
	        		ptmt.setString(1, rs.getString(1));
		        	ptmt.setString(2, tempObj.get("category1").toString());
		        	ptmt.setString(3, tempObj.get("category2").toString());
		        	ptmt.setString(4, tempObj.get("category3").toString());
	        	}
	        	/*
	        	System.out.println("아이템 카테고리1 : " + tempObj.get("category1"));
	        	System.out.println("아이템 카테고리2 : " + tempObj.get("category2"));
	        	System.out.println("아이템 카테고리3 : " + tempObj.get("category3"));
	        	*/
	        	//stmt.executeUpdate("insert into GOODS_CATEGORY values ('"+rs.getString(1)+"','"+tempObj.get("category1")+"','"+tempObj.get("category2")+"','"+tempObj.get("category3")+"')");
	        	
	        	ptmt.executeUpdate();
	        	Thread.sleep(1000);
	        	
	        	
	        }catch(ParseException e) {
	        	e.printStackTrace();
	        }
	        
    	}
        

    }

    private static String get(String apiUrl, Map<String, String> requestHeaders){
        HttpURLConnection con = connect(apiUrl);
        try {
            con.setRequestMethod("GET");
            for(Map.Entry<String, String> header :requestHeaders.entrySet()) {
                con.setRequestProperty(header.getKey(), header.getValue());
            }

            int responseCode = con.getResponseCode();
            if (responseCode == HttpURLConnection.HTTP_OK) { // 정상 호출
                return readBody(con.getInputStream());
            } else { // 에러 발생
                return readBody(con.getErrorStream());
            }
        } catch (IOException e) {
            throw new RuntimeException("API 요청과 응답 실패", e);
        } finally {
            con.disconnect();
        }
    }

    private static HttpURLConnection connect(String apiUrl){
        try {
            URL url = new URL(apiUrl);
            return (HttpURLConnection)url.openConnection();
        } catch (MalformedURLException e) {
            throw new RuntimeException("API URL이 잘못되었습니다. : " + apiUrl, e);
        } catch (IOException e) {
            throw new RuntimeException("연결이 실패했습니다. : " + apiUrl, e);
        }
    }

    private static String readBody(InputStream body){
        InputStreamReader streamReader = new InputStreamReader(body);

        try (BufferedReader lineReader = new BufferedReader(streamReader)) {
            StringBuilder responseBody = new StringBuilder();

            String line;
            while ((line = lineReader.readLine()) != null) {
                responseBody.append(line);
            }

            return responseBody.toString();
        } catch (IOException e) {
            throw new RuntimeException("API 응답을 읽는데 실패했습니다.", e);
        }
    }
}