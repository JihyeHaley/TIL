package vo;

public class ShopVO {

    // 판매점 아이디 
    private String shop_id;

    // 판매점 주소 
    private String shop_addr;

    // 전화 번호 
    private String tel_num;

    // 판매점 코드
    private String shop_code;


    // 판매점 명 상세 
    private String shop_name_detail;

	public String getShop_id() {
		return shop_id;
	}

	public void setShop_id(String shop_id) {
		this.shop_id = shop_id;
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


	public String getShop_code() {
		return shop_code;
	}

	public void setShop_code(String shop_code) {
		this.shop_code = shop_code;
	}

	public String getShop_name_detail() {
		return shop_name_detail;
	}

	public void setShop_name_detail(String shop_name_detail) {
		this.shop_name_detail = shop_name_detail;
	}

	@Override
	public String toString() {
		return "ShopVO [shop_id=" + shop_id + ", shop_addr=" + shop_addr + ", tel_num=" + tel_num + ", shop_code="
				+ shop_code + ", shop_name_detail=" + shop_name_detail + "]";

	}
    
}