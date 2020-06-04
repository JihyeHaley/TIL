package vo;

import java.util.Date;

public class GoodsInformVO {

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
    
    // 상품 판매점 아이디 
    private String good_shop_id;

    // 판매점 코드
    private String shop_code;
    
    // 행사 명 
    private String event_name;

    // 행사 아이디 
    private int event_id;
 
    // 판매점 명 
    private String shop_name;
    
    // 소분류 1 
    private String ctg_1;

    // 소분류 2 
    private String ctg_2;

    // 소분류 3 
    private String ctg_3;
 
    // 장바구니 아이디 
    private int cart_id;

    // 아이디 
    private String id;

    // 주문 갯수
    private int cnt;
    
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

	public String getGood_shop_id() {
		return good_shop_id;
	}

	public void setGood_shop_id(String good_shop_id) {
		this.good_shop_id = good_shop_id;
	}

	public String getShop_code() {
		return shop_code;
	}

	public void setShop_code(String shop_code) {
		this.shop_code = shop_code;
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

	public String getShop_name() {
		return shop_name;
	}

	public void setShop_name(String shop_name) {
		this.shop_name = shop_name;
	}

	public String getCtg_1() {
		return ctg_1;
	}

	public void setCtg_1(String ctg_1) {
		this.ctg_1 = ctg_1;
	}

	public String getCtg_2() {
		return ctg_2;
	}

	public void setCtg_2(String ctg_2) {
		this.ctg_2 = ctg_2;
	}

	public String getCtg_3() {
		return ctg_3;
	}

	public void setCtg_3(String ctg_3) {
		this.ctg_3 = ctg_3;
	}

	public int getCart_id() {
		return cart_id;
	}

	public void setCart_id(int cart_id) {
		this.cart_id = cart_id;
	}

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public int getCnt() {
		return cnt;
	}

	public void setCnt(int cnt) {
		this.cnt = cnt;
	}

	@Override
	public String toString() {
		return "GoodsInformVO [good_id=" + good_id + ", good_name=" + good_name + ", search_date=" + search_date
				+ ", good_price=" + good_price + ", mfg_name=" + mfg_name + ", good_img=" + good_img + ", good_shop_id="
				+ good_shop_id + ", shop_code=" + shop_code + ", event_name=" + event_name + ", event_id=" + event_id
				+ ", shop_name=" + shop_name + ", ctg_1=" + ctg_1 + ", ctg_2=" + ctg_2 + ", ctg_3=" + ctg_3
				+ ", cart_id=" + cart_id + ", id=" + id + ", cnt=" + cnt + "]";
	}
	
}
