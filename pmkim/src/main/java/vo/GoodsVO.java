package vo;

import java.util.Date;

public class GoodsVO {

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

	@Override
	public String toString() {
		return "GoodsVO [good_id=" + good_id + ", good_name=" + good_name + ", search_date=" + search_date
				+ ", good_price=" + good_price + ", mfg_name=" + mfg_name + ", good_img=" + good_img + "]";
	}

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

}
