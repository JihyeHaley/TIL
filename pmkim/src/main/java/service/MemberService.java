package service;

import javax.servlet.http.HttpServletResponse;

import vo.MemberVO;

public interface MemberService {
	public void check_id(String id, HttpServletResponse response) throws Exception;
	
	public void check_email(String email, HttpServletResponse response) throws Exception;
	
	public int join_member(MemberVO member, HttpServletResponse response) throws Exception;
}
