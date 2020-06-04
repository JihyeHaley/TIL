package vo;

import java.util.Date;

public class MemberVO {

    // 아이디 
    private String id;

    // 비밀번호 
    private String pw;

    // 명 
    private String name;

    // 전화 번호 
    private String tel_num;

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

	public String getTel_num() {
		return tel_num;
	}

	public void setTel_num(String tel_num) {
		this.tel_num = tel_num;
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

	@Override
	public String toString() {
		return "MemberVO [id=" + id + ", pw=" + pw + ", name=" + name + ", tel_num=" + tel_num + ", email=" + email
				+ ", sign_date=" + sign_date + ", nick_name=" + nick_name + ", road_addr=" + road_addr + ", login_type="
				+ login_type + ", member_type=" + member_type + "]";
	}
    
    

}
