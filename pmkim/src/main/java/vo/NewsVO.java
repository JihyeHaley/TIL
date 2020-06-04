package vo;

import java.text.SimpleDateFormat;
import java.util.Date;

public class NewsVO {
	
	// 게시 아이디 
    private int write_id;

    // 날짜 
    private Date write_date;

    // 제목 
    private String title;

    // 내용 
    private String content;
    
    // 판매점 코드 
    private String shop_code;

    // 판매점 명 
    private String shop_name;
    
    // 판매점 명 
    private String shop_name_kor;

	public int getWrite_id() {
		return write_id;
	}

	public void setWrite_id(int write_id) {
		this.write_id = write_id;
	}

	
	public String getWrite_date() {
		SimpleDateFormat format = new SimpleDateFormat("yyyy년 MM월 dd일");
		return format.format(write_date);
	}

	public void setWrite_date(Date write_date) {
		this.write_date = write_date;
	}

	public String getTitle() {
		return title;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	public String getContent() {
		return content;
	}

	public void setContent(String content) {
		this.content = content;
	}

	public String getShop_code() {
		return shop_code;
	}

	public void setShop_code(String shop_code) {
		this.shop_code = shop_code;
	}

	public String getShop_name() {
		return shop_name;
	}

	public void setShop_name(String shop_name) {
		this.shop_name = shop_name;
	}

	public String getShop_name_kor() {
		return shop_name_kor;
	}

	public void setShop_name_kor(String shop_name_kor) {
		this.shop_name_kor = shop_name_kor;
	}

	@Override
	public String toString() {
		return "NewsVO [write_id=" + write_id + ", write_date=" + write_date + ", title=" + title + ", content="
				+ content + ", shop_code=" + shop_code + ", shop_name=" + shop_name + ", shop_name_kor=" + shop_name_kor
				+ "]";
	}

	@Override
	public int hashCode() {
		return title.hashCode()+shop_name.hashCode();
	}

	@Override
	public boolean equals(Object obj) {
		boolean result = false;
		//obj = new NewsVO();
		if(((NewsVO) obj).getTitle().equals(title)&& ((NewsVO) obj).getShop_name().equals(shop_name)) {
			result = true;
		}else {
			System.out.println("vo에서 equal메소드 오류");
		}
		return result;
	}

	
}
