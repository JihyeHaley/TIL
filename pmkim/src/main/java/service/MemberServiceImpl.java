package service;

import java.io.PrintWriter;

import javax.inject.Inject;
import javax.servlet.http.HttpServletResponse;

import org.springframework.stereotype.Repository;
import org.springframework.stereotype.Service;

import dao.MemberDAO;
import vo.MemberVO;



@Service
public class MemberServiceImpl implements MemberService{
	
	@Inject
	private MemberDAO manager;
	
	// 아이디 중복 검사(AJAX)
	@Override
	public void check_id(String id, HttpServletResponse response) throws Exception{
		PrintWriter out = response.getWriter();
		out.println(manager.check_id(id));
		out.close();
	}

	@Override
	public void check_email(String email, HttpServletResponse response) throws Exception {
		PrintWriter out = response.getWriter();
		out.println(manager.check_email(email));
		out.close();
	}

	@Override
	public int join_member(MemberVO member, HttpServletResponse response) throws Exception {
		response.setContentType("text/html; charset=UTF-8");
		PrintWriter out = response.getWriter();
		//System.out.println("SSSS"+member.toString());
		//체크해서 alert 창에 경고 후 되돌아가기
		if(manager.check_id(member.getId())==1) {
			out.println("<script>");
			out.println("alert('동일한 아이디가 있습니다!');");
			out.println("history.go(-1);");
			out.println("</script>");
			out.close();
			return 0;
		}else if (manager.check_email(member.getEmail())==1) {
			out.println("<script>");
			out.println("alert('동일한 이메일가 있습니다!');");
			out.println("history.go(-1);");
			out.println("</script>");
			out.close();
			return 0;
		}else {
			manager.join_member(member);
			return 1;
		}
	}
}
