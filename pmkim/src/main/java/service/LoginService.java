package service;

import javax.servlet.http.HttpSession;

import org.springframework.stereotype.Service;

import vo.MemberVO;

@Service
public interface LoginService {
	public boolean loginCheck(MemberVO vo,HttpSession session);
	public MemberVO viewMember(MemberVO vo);
	public void logout(HttpSession session);
}
