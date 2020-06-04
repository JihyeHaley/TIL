package spring.mvc.pmkim;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import dao.CartDAO;
import dao.EventDAO;
import service.PagingService;
import vo.GoodsEventShopMemberVO;


@Controller
public class HomeController {
	
	@Autowired
	CartDAO cdao;
	
	@Autowired
	EventDAO edao;
	
	@Autowired
	PagingService ps;
	
	@RequestMapping(value = "/home", method = RequestMethod.GET)
	public ModelAndView home(String action, String good_name, GoodsEventShopMemberVO gesmvo, String event_name,String shop_code, @RequestParam(defaultValue="1")int pgNum) {
		ModelAndView mav = new ModelAndView();
		
		//Event Jihye
		if(event_name==null && shop_code==null) {
			event_name = "1+1";
			shop_code = "CU";
		}
		List<GoodsEventShopMemberVO> onelist = edao.homeEventOne(event_name,shop_code);
		List<GoodsEventShopMemberVO> twolist = edao.homeEventTwo(event_name,shop_code);
		List<GoodsEventShopMemberVO> pblist = edao.homeEventPB(event_name,shop_code);
		
		if (action != null && good_name != null) {
			onelist = edao.homeEventOne(event_name,shop_code);	
			twolist = edao.homeEventTwo(event_name,shop_code);	
			pblist = edao.homeEventPB(event_name,shop_code);	
		}
		//Event Jihye 

		mav.addObject("onelist", onelist);
		mav.addObject("twolist", twolist);
		mav.addObject("pblist", pblist);
		mav.setViewName("home");
		return mav;
	}
	
}







