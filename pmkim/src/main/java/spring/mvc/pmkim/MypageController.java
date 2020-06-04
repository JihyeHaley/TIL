package spring.mvc.pmkim;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

import vo.MemberVO;


@Controller
public class MypageController {
//	@Autowired
//	MapDAO dao;
	
	@RequestMapping(value = "/mypage", method = RequestMethod.GET)
	public String mypage() {
		return "/mypage";
	}
	
	@RequestMapping(value = "/memberinfomodify", method = RequestMethod.GET)
	public ModelAndView memberinfomodify(MemberVO memberVO) {
		ModelAndView mav = new ModelAndView();
		
		mav.setViewName("/memberInfoModify");
		return mav;
	}
	
	@RequestMapping(value = "/memberinfoinquiry", method = RequestMethod.GET)
	public ModelAndView memberInfomoInquiry(MemberVO memberVO) {
		ModelAndView mav = new ModelAndView();
		
		mav.setViewName("/memberInfomoInquiry");
		return mav;
	}
	
	@RequestMapping(value = "/memberwithdraw", method = RequestMethod.GET)
	public ModelAndView memberWithdraw(MemberVO memberVO) {
		ModelAndView mav = new ModelAndView();
		
		mav.setViewName("/memberWithdraw");
		return mav;
	}
	
}
