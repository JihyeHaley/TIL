package vo;

public class CartVO {

    // 장바구니 아이디 
    private int cart_id;

    // 아이디 
    private String id;

    // 상품 아이디 
    private String good_id;

    // 주문 갯수
    private int cnt;

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

	public String getGood_id() {
		return good_id;
	}

	public void setGood_id(String good_id) {
		this.good_id = good_id;
	}

	public int getCnt() {
		return cnt;
	}

	public void setCnt(int cnt) {
		this.cnt = cnt;
	}

	@Override
	public String toString() {
		return "CartVO [cart_id=" + cart_id + ", id=" + id + ", good_id=" + good_id + ", cnt=" + cnt + "]";
	}

}
