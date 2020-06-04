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
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.HashMap;
import java.util.Locale;
import java.util.Map;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;
import org.springframework.stereotype.Service;

//@Service
public class NaverApiSearchNews {
	
	//@Scheduled(cron="* * 12 * * *")
    public void naverNews() throws Exception{
        String clientId = "FZqBsDALM8L8w7aa_vY5"; //애플리케이션 클라이언트 아이디값"
        String clientSecret = "RDK08h85bB"; //애플리케이션 클라이언트 시크릿값"

        String text = null;
        Map<String, String> requestHeaders = new HashMap<>();
        String responseBody = null;
        
        Class.forName("oracle.jdbc.driver.OracleDriver");
    	Connection conn = DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:XE","pmkim","pmkimbear");
    	Statement stmt = conn.createStatement(ResultSet.TYPE_SCROLL_INSENSITIVE,ResultSet.CONCUR_READ_ONLY);
    	PreparedStatement ptmt = conn.prepareStatement("insert into BOARD values (board_seq.nextval,?,?,?,?)");
    	ResultSet rs = stmt.executeQuery("select shop_name_kor from shop_code");
		DateFormat formatter = new SimpleDateFormat("EEE, dd MMM yyyy HH:mm:ss", Locale.ENGLISH);
		DateFormat formatter2 = new SimpleDateFormat("yy/MM/dd");
		Date date = new Date();
    	//rs.last();
    	//System.out.println(rs.getRow());
    	while(rs.next()) {
    		System.out.println(rs.getString(1));
	    	try {
	            text = URLEncoder.encode(rs.getString(1), "UTF-8");
	        } catch (UnsupportedEncodingException e) {
	        	System.out.println("kkkkkkkkkkk");
	            throw new RuntimeException("검색어 인코딩 실패",e);
	        }
	    	
	        String apiURL = "https://openapi.naver.com/v1/search/news?query=" + text +"&display=100";    // json 결과
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
	        	System.out.println("empty : "+itemsArray.isEmpty());
	        	if(itemsArray.isEmpty()) {
		        	ptmt.setString(1, "기타");
		        	ptmt.setString(2, "기타");
		        	ptmt.setString(3, "기타");
		        	ptmt.setString(4, "기타");
		        	
		        	ptmt.executeUpdate();
	        	}else {
	        		
	        		System.out.println(itemsArray.getClass());
	        		if(itemsArray.isEmpty()) {
	        			System.out.println("Fail");
	        		}
	        		
	        		for (int i=0; i<100; i++) {
	        			tempObj = (JSONObject) itemsArray.get(i);
	        			String dateS[] = tempObj.get("pubDate").toString().split(" \\+");
		        		
		        		date = formatter.parse(dateS[0]);
		        		
			        	ptmt.setString(1, formatter2.format(date));
			        	ptmt.setString(2, tempObj.get("title").toString());
			        	ptmt.setString(3, tempObj.get("originallink").toString());
			        	ptmt.setString(4, rs.getString(1));
			        	
			        	ptmt.executeUpdate();

	        		}
	        		
	        		
	        	}
	        	
	        	
	        	//ptmt.executeUpdate();
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