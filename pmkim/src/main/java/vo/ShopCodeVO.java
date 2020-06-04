package vo;

public class ShopCodeVO {
	public class ShopCode {

	    // 판매점 코드 
	    private String shop_code;

	    // 판매점 명 
	    private String shop_name;

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

		@Override
		public String toString() {
			return "ShopCode [shop_code=" + shop_code + ", shop_name=" + shop_name + "]";
		}
	    
	}
}
