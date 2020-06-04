package vo;

import java.util.Date;

public class GoodsCategoryEventShopMemberVO {

    // 상품 아이디 
    private String good_id;

    // 소분류 1 
    private String ctg_1;

    // 소분류 2 
    private String ctg_2;

    // 소분류 3 
    private String ctg_3;

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

    // 판매점 명 
    private String shop_name;
    
    // 행사 명 
    private String event_name;

    
 // 행사 아이디 
    private int event_id;
    
    // 아이디 
    private String id;

    // 비밀번호 
    private String pw;

    // 명 
    private String name;

    // 이메일 
    private String email;

    // 가입 날짜 
    private Date sign_date;

    // 별칭 명 
    private String nick_name;

    // 도로 주소 
    private String road_addr;

    // 로그인 종류 
    private String login_type;

    // 멤버 종류 
    private String member_type;
    
    
    
    
    public String getGood_shop_id() {
		return good_shop_id;
	}


	public void setGood_shop_id(String good_shop_id) {
		this.good_shop_id = good_shop_id;
	}


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


	public String getShop_name_detail() {
		return shop_name_detail;
	}


	public void setShop_name_detail(String shop_name_detail) {
		this.shop_name_detail = shop_name_detail;
	}


	public String getShop_name() {
		return shop_name;
	}


	public void setShop_name(String shop_name) {
		this.shop_name = shop_name;
	}


	public int getEvent_id() {
		return event_id;
	}


	public void setEvent_id(int event_id) {
		this.event_id = event_id;
	}


	public String getId() {
		return id;
	}


	public void setId(String id) {
		this.id = id;
	}


	public String getPw() {
		return pw;
	}


	public void setPw(String pw) {
		this.pw = pw;
	}


	public String getName() {
		return name;
	}


	public void setName(String name) {
		this.name = name;
	}


	public String getEmail() {
		return email;
	}


	public void setEmail(String email) {
		this.email = email;
	}


	public Date getSign_date() {
		return sign_date;
	}


	public void setSign_date(Date sign_date) {
		this.sign_date = sign_date;
	}


	public String getNick_name() {
		return nick_name;
	}


	public void setNick_name(String nick_name) {
		this.nick_name = nick_name;
	}


	public String getRoad_addr() {
		return road_addr;
	}


	public void setRoad_addr(String road_addr) {
		this.road_addr = road_addr;
	}


	public String getLogin_type() {
		return login_type;
	}


	public void setLogin_type(String login_type) {
		this.login_type = login_type;
	}


	public String getMember_type() {
		return member_type;
	}


	public void setMember_type(String member_type) {
		this.member_type = member_type;
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


@Override
public String toString() {
	return "GoodsCategoryEventShopMemberVO [good_id=" + good_id + ", ctg_1=" + ctg_1 + ", ctg_2=" + ctg_2 + ", ctg_3="
			+ ctg_3 + ", good_name=" + good_name + ", search_date=" + search_date + ", good_price=" + good_price
			+ ", mfg_name=" + mfg_name + ", good_img=" + good_img + ", good_shop_id=" + good_shop_id + ", shop_id="
			+ shop_id + ", shop_addr=" + shop_addr + ", tel_num=" + tel_num + ", shop_code=" + shop_code
			+ ", shop_name_detail=" + shop_name_detail + ", shop_name=" + shop_name + ", event_name=" + event_name
			+ ", event_id=" + event_id + ", id=" + id + ", pw=" + pw + ", name=" + name + ", email=" + email
			+ ", sign_date=" + sign_date + ", nick_name=" + nick_name + ", road_addr=" + road_addr + ", login_type="
			+ login_type + ", member_type=" + member_type + "]";
}

}