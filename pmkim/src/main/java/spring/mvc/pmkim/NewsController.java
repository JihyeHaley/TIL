package spring.mvc.pmkim;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import dao.NewsDAO;
import service.NewsPagingService;
import vo.NewsVO;

@Controller
public class NewsController {

	@Autowired
	NewsDAO ndao;
	
	@Autowired
	NewsPagingService nps;
	
	@RequestMapping(value="/news")
	public ModelAndView newsGet(NewsVO vo,String shop_name_kor, @RequestParam(defaultValue="1")int pgNum) {
		int startNum = nps.getWritingStart(pgNum);
		int endNum = nps.getWritingEnd(pgNum);
		int end = nps.getPageCount();
		int pageEnd = nps.getPageEnd(pgNum);
		boolean nextdata = nps.isNextData(pgNum);

		ModelAndView mav = new ModelAndView();
		List<NewsVO> list = ndao.listAll(vo,startNum, endNum);
		
		String oldQ ="";

		if(vo.getShop_name_kor() == null) {
			list = ndao.listAll(vo,startNum, endNum);
		}else {
			list = ndao.listSort(shop_name_kor, startNum, endNum);
			end = nps.getPageCount(shop_name_kor);
			pageEnd = nps.getPageEnd(pgNum,shop_name_kor);
			nextdata = nps.isNextData(pgNum,shop_name_kor);
			oldQ = "&shop_name_kor="+shop_name_kor;
		}
		
		mav.addObject("pgNum",pgNum);
		mav.addObject("end",end);
		mav.addObject("oldQ",oldQ);
		mav.addObject("pageStart",nps.getPageStart(pgNum));
		mav.addObject("pageEnd",pageEnd);
		mav.addObject("preData",nps.isPreData(pgNum));
		mav.addObject("nextData",nextdata);
		
		mav.addObject("newsList",list);
		mav.setViewName("news");
		return mav;
	}
}
