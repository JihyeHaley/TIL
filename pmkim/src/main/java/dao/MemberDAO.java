package dao;

import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;
import org.springframework.transaction.annotation.Transactional;

import vo.MemberVO;

@Repository
public class MemberDAO {

	@Autowired
	SqlSession session = null;
	
	//아이디 중복 검사
	public int check_id(String id) throws Exception{
		return session.selectOne("resource.MemberMapper.checkId",id);
	}
	
	//이메일 중복 검사
	public int check_email(String email) throws Exception{
		return session.selectOne("resource.MemberMapper.checkEmail",email);
	}
	
	//회원 가입
	@Transactional
	public int join_member(MemberVO member) throws Exception{
		System.out.println("DDDD"+member.toString());
		return session.insert("resource.MemberMapper.joinMember",member);
	}
	
	//로그인
	public MemberDAO login(String id) throws Exception{
		return session.selectOne("resource.MemberMapper.loginCheck",id);
	}

	
}
