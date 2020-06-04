package vo;

public class ThemeVO {

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

	@Override
	public String toString() {
		return "ThemeVO [themeCode=" + themeCode + ", themeName=" + themeName + ", searchName1=" + searchName1
				+ ", searchName2=" + searchName2 + ", searchName3=" + searchName3 + "]";
	}
    
    
}