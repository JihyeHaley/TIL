package vo;

import java.util.Date;

public class AnalysisVO {

    // 상품 아이디 
    private String good_id;

    // 상품 명 
    private String good_name;

	// 조사 날짜 
    private Date search_date;

    // 상품 가격 
    private String good_price;

    // 제조사 명 
    private String mfg_name;

    // 상품 이미지 
    private String good_img;

	// 테마 코드 
    private String themeCode;

    // 테마 명 
    private String themeName;
    
    // 조사 명 1 
    private String searchName1;

    // 조사 명 2 
    private String searchName2;

    // 조사 명 3 
    private String searchName3;
    
    // 행사 명 
    private String event_name;

    // 행사 아이디 
    private int event_id;
    
    // 판매점 코드 
    private String shop_code;

    // 판매점 명 
    private String shop_name;
    
    // 판매점 주소 
    private String shop_addr;

    // 전화 번호 
    private String tel_num;

    // 판매점 명 상세 
    private String shop_name_detail;

	public String getGood_id() {
		return good_id;
	}

	public void setGood_id(String good_id) {
		this.good_id = good_id;
	}

	public String getGood_name() {
		return good_name;
	}

	public void setGood_name(String good_name) {
		this.good_name = good_name;
	}

	public Date getSearch_date() {
		return search_date;
	}

	public void setSearch_date(Date search_date) {
		this.search_date = search_date;
	}

	public String getGood_price() {
		return good_price;
	}

	public void setGood_price(String good_price) {
		this.good_price = good_price;
	}

	public String getMfg_name() {
		return mfg_name;
	}

	public void setMfg_name(String mfg_name) {
		this.mfg_name = mfg_name;
	}

	public String getGood_img() {
		return good_img;
	}

	public void setGood_img(String good_img) {
		this.good_img = good_img;
	}

	public String getThemeCode() {
		return themeCode;
	}

	public void setThemeCode(String themeCode) {
		this.themeCode = themeCode;
	}

	public String getThemeName() {
		return themeName;
	}

	public void setThemeName(String themeName) {
		this.themeName = themeName;
	}

	public String getSearchName1() {
		return searchName1;
	}

	public void setSearchName1(String searchName1) {
		this.searchName1 = searchName1;
	}

	public String getSearchName2() {
		return searchName2;
	}

	public void setSearchName2(String searchName2) {
		this.searchName2 = searchName2;
	}

	public String getSearchName3() {
		return searchName3;
	}

	public void setSearchName3(String searchName3) {
		this.searchName3 = searchName3;
	}

	public String getEvent_name() {
		return event_name;
	}

	public void setEvent_name(String event_name) {
		this.event_name = event_name;
	}

	public int getEvent_id() {
		return event_id;
	}

	public void setEvent_id(int event_id) {
		this.event_id = event_id;
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

	public String getShop_addr() {
		return shop_addr;
	}

	public void setShop_addr(String shop_addr) {
		this.shop_addr = shop_addr;
	}

	public String getTel_num() {
		return tel_num;
	}

	public void setTel_num(String tel_num) {
		this.tel_num = tel_num;
	}

	public String getShop_name_detail() {
		return shop_name_detail;
	}

	public void setShop_name_detail(String shop_name_detail) {
		this.shop_name_detail = shop_name_detail;
	}

	@Override
	public String toString() {
		return "GoodsInfoThemeVO [good_id=" + good_id + ", good_name=" + good_name + ", search_date=" + search_date
				+ ", good_price=" + good_price + ", mfg_name=" + mfg_name + ", good_img=" + good_img + ", themeCode="
				+ themeCode + ", themeName=" + themeName + ", searchName1=" + searchName1 + ", searchName2="
				+ searchName2 + ", searchName3=" + searchName3 + ", event_name=" + event_name + ", event_id=" + event_id
				+ ", shop_code=" + shop_code + ", shop_name=" + shop_name + ", shop_addr=" + shop_addr + ", tel_num="
				+ tel_num + ", shop_name_detail=" + shop_name_detail + "]";
	}
    
    
}
