package vo;

public class GoodsCategory {

    // 상품 아이디 
    private String good_id;

    // 소분류 1 
    private String ctg_1;

    // 소분류 2 
    private String ctg_2;

    // 소분류 3 
    private String ctg_3;


    public String getGood_id() {
		return good_id;
	}


	public void setGood_id(String good_id) {
		this.good_id = good_id;
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


	// GoodsCategory 모델 복사
    public void CopyData(GoodsCategory param)
    {
        this.good_id = param.getGood_id();
        this.ctg_1 = param.getCtg_1();
        this.ctg_2 = param.getCtg_2();
        this.ctg_3 = param.getCtg_3();
    }
}
