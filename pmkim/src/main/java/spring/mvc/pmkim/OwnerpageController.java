package spring.mvc.pmkim;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

import vo.MemberVO;

@Controller
public class OwnerpageController {
//	@Autowired
//	MapDAO dao;
	
	@RequestMapping(value = "/ownerpage", method = RequestMethod.GET)
	public ModelAndView owner(String searchKeyword, MemberVO memberVO) {
		ModelAndView mav = new ModelAndView();
		
		mav.setViewName("/ownerpage");
		return mav;
	}
	
	@RequestMapping(value = "/ask", method = RequestMethod.GET)
	public String owner() {
		return "/ask";
	}
	
	@RequestMapping(value = "/memberownerinquiry", method = RequestMethod.GET)
	public ModelAndView memberOwnerInquiry(MemberVO memberVO) {
		ModelAndView mav = new ModelAndView();
		
		mav.setViewName("/memberOwnerInquiry");
		return mav;
	}

}
