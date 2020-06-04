package vo;

public class MemberOwnerVO {

    // 아이디 
    private String id;

    // 판매점 아이디 
    private String shop_id;

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getShop_id() {
		return shop_id;
	}

	public void setShop_id(String shop_id) {
		this.shop_id = shop_id;
	}

	@Override
	public String toString() {
		return "MemberOwnerVO [id=" + id + ", shop_id=" + shop_id + "]";
	}
	
	
}