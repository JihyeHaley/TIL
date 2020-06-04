package dao;
import javax.servlet.http.HttpSession;

import vo.MemberVO;

public interface LoginDAO {
	public boolean loginCheck(MemberVO vo);
	public MemberVO viewMember(MemberVO vo);
	public void logout(HttpSession session);
}
