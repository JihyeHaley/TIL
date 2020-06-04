package spring.mvc.pmkim;

import javax.servlet.http.HttpSession;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

import service.LoginService;
import vo.MemberVO;

@Controller
public class LoginController {
	private static final Logger logger = LoggerFactory.getLogger(LoginController.class);
	
	@Autowired
	LoginService ms;
	
//	@RequestMapping(value="/main", method = RequestMethod.GET)
//	public String main(@ModelAttribute MemberVO vo, HttpSession session) {
//		return "main";
//	}
	
	@RequestMapping(value="/login")
	public ModelAndView loginCheck(@ModelAttribute MemberVO vo, HttpSession session) {
		ModelAndView mav = new ModelAndView();
		if(ms.loginCheck(vo, session)) {
			session.setAttribute("User", vo);
			session.setAttribute("id", vo.getId());
			mav.addObject("msg","success");
		}else {
			//mav.setViewName("main2");
			mav.addObject("msg","fail");
		}
		mav.setViewName("home");
		return mav;
	}
	
//	@RequestMapping(value="/menu")
//	public String menu(HttpSession session) {
//		session.getAttribute("id");
//		//System.out.println(session.getAttribute("sm_id"));
//		return "main2";
//	}
	
	@RequestMapping(value="/logout")
	public ModelAndView logout(HttpSession session) {
		ms.logout(session);
		ModelAndView mav = new ModelAndView();
		mav.setViewName("home");
		mav.addObject("msg","logout");
		return mav;
	}
}
