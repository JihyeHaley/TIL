package vo;

public class GoodsThemeVO {

	// 상품 테마 아이디 
    private Integer good_theme_id;

    // 테마 코드 
    private String theme_code;

    // 상품 아이디 
    private String good_id;

	public Integer getGood_theme_id() {
		return good_theme_id;
	}

	public void setGood_theme_id(Integer good_theme_id) {
		this.good_theme_id = good_theme_id;
	}

	public String getTheme_code() {
		return theme_code;
	}

	public void setTheme_code(String theme_code) {
		this.theme_code = theme_code;
	}

	public String getGood_id() {
		return good_id;
	}

	public void setGood_id(String good_id) {
		this.good_id = good_id;
	}

	@Override
	public String toString() {
		return "GoodsThemeVO [good_theme_id=" + good_theme_id + ", theme_code=" + theme_code + ", good_id=" + good_id
				+ "]";
	}

    

    
    
}