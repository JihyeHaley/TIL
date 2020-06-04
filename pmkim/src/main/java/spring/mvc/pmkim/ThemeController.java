package spring.mvc.pmkim;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import dao.ThemeDAO;
import vo.GoodsInfoThemeVO;


@Controller
public class ThemeController {
	
	@Autowired
	private ThemeDAO ThemeDAO;

	
	@RequestMapping(value="/theme")
	public ModelAndView theme(GoodsInfoThemeVO gitvo) {

		List<GoodsInfoThemeVO> li = ThemeDAO.allGoods(gitvo);
		ModelAndView mav = new ModelAndView();
		//값 확인
		//System.out.println("Con : " + li.get(0).toString());
		//goods table
		mav.addObject("theme", li);
		mav.setViewName("theme");
		return mav;
	}
	

}
