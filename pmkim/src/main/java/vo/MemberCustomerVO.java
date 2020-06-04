package vo;

public class MemberCustomerVO {

    // 아이디 
    private String id;

    // 선호 상품 1 
    private String prefer_good_1;

    // 선호 상품 2 
    private String prefer_good_2;

    // 선호 상품 3 
    private String prefer_good_3;

    // 선호 판매점 
    private String prefer_shop;

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getPrefer_good_1() {
		return prefer_good_1;
	}

	public void setPrefer_good_1(String prefer_good_1) {
		this.prefer_good_1 = prefer_good_1;
	}

	public String getPrefer_good_2() {
		return prefer_good_2;
	}

	public void setPrefer_good_2(String prefer_good_2) {
		this.prefer_good_2 = prefer_good_2;
	}

	public String getPrefer_good_3() {
		return prefer_good_3;
	}

	public void setPrefer_good_3(String prefer_good_3) {
		this.prefer_good_3 = prefer_good_3;
	}

	public String getPrefer_shop() {
		return prefer_shop;
	}

	public void setPrefer_shop(String prefer_shop) {
		this.prefer_shop = prefer_shop;
	}

	@Override
	public String toString() {
		return "MemberCustomerVO [id=" + id + ", prefer_good_1=" + prefer_good_1 + ", prefer_good_2=" + prefer_good_2
				+ ", prefer_good_3=" + prefer_good_3 + ", prefer_shop=" + prefer_shop + "]";
	}

	
    
}
