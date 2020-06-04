package spring.mvc.pmkim;

import javax.servlet.http.HttpServletResponse;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import service.MemberServiceImpl;
import vo.MemberVO;

@Controller
@RequestMapping(value = "/member/*")
public class MemberController {
	
	@Autowired
	private MemberServiceImpl service;
	
	//아이디 중복검사(ajax)
	@RequestMapping(value = "/check_id", method = RequestMethod.POST)
	public void check_id(@RequestParam("id") String id , HttpServletResponse response) throws Exception {
		service.check_id(id,response);
	}
	
	//이메일 중복검사(ajax)
	@RequestMapping(value = "/check_email", method = RequestMethod.POST)
	public void check_email(@RequestParam("email") String email , HttpServletResponse response) throws Exception {
		service.check_email(email, response);
	}
	
	//회원가입
	@RequestMapping(value = "/join_member", method = RequestMethod.POST)
	public String memberInsert(@ModelAttribute MemberVO member, 
			RedirectAttributes rttr, HttpServletResponse response) throws Exception {
		rttr.addFlashAttribute("result", service.join_member(member, response));
		//System.out.println("CCCC"+member.toString());
		return "redirect:./memberJoinForm";
	}
	
	//회원 가입 폼 이동
	@RequestMapping(value = "/memberJoinForm")
	public String memberJoinForm() throws Exception {
		return "/member/memberJoinForm";
	}
}
