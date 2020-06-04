package spring.mvc.pmkim;


import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
//import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import dao.EventDAO;
import service.PagingService2;
import vo.GoodsCategoryEventShopMemberVO;
import vo.GoodsEventShopMemberVO;

@Controller
public class EventController {

	
	@Autowired
	EventDAO edao;
	GoodsCategoryEventShopMemberVO gcesmvo;
	
	@Autowired
	PagingService2 ps2;

	@RequestMapping(value = "/event", method = RequestMethod.GET)
	public ModelAndView cartGet(String action, String good_name, GoodsEventShopMemberVO gesmvo, String event_name,String shop_code, String ctg_1, @RequestParam(defaultValue="1")int pgNum) {
		ModelAndView mav = new ModelAndView();
		//paging용 시작페이지 num, 끝페이지 num
		int startNum = ps2.getWritingStart(pgNum);
		int endNum = ps2.getWritingEnd(pgNum);
		
		int end = ps2.getPageCount(good_name);
	    int pageEnd = ps2.getPageEnd(pgNum, good_name);
	    boolean nextdata = ps2.isNextData(pgNum, good_name);
	    //쿼리저장
	    String oldQ ="";
	    
		//default값 설정
		if(event_name==null && shop_code==null && ctg_1==null) {
			shop_code = "CU";
			event_name = "2+1";
			ctg_1 = "식품";

			//if(shop_code=="GS"){shop_code="GS";if(event_name=="1+1"){event_name="1+1";}else if(event_name=="2+1"){event_name="2+1";}else if(event_name=="PB"){event_name="PB";}}
			//else if(shop_code=="CU"){shop_code="CU";if(event_name=="1+1"){event_name="1+1";}else if(event_name=="2+1"){event_name="2+1";}else if(event_name=="PB"){event_name="PB";}}
			//else if(shop_code=="MS"){shop_code="MS";if(event_name=="1+1"){event_name="1+1";}else if(event_name=="2+1"){event_name="2+1";}else if(event_name=="PB"){event_name="PB";}}
			//else if(shop_code=="SE"){shop_code="SE";if(event_name=="1+1"){event_name="1+1";}else if(event_name=="2+1"){event_name="2+1";}else if(event_name=="PB"){event_name="PB";}}
			//else if(shop_code=="EM"){shop_code="EM";if(event_name=="1+1"){event_name="1+1";}else if(event_name=="2+1"){event_name="2+1";}else if(event_name=="PB"){event_name="PB";}}
			
		}
		
		//List <GoodsEventShopMemberVO> eventAllView = eventDAO.eventAllView();
		List<GoodsCategoryEventShopMemberVO> geslist = edao.goodsShopEvent(event_name,shop_code,startNum,endNum);
		
		if (action != null && good_name != null) {
			//geslist = edao.goodsAll();
			geslist = edao.searchGoods2(good_name);
			oldQ += "&action="+action+"&good_name="+good_name;
			
		} else if (action != null && good_name ==null){
			if (action.equals("sort")) {
				geslist = edao.goodsShopEvent(event_name,shop_code,startNum,endNum);
				geslist = edao.goodsShopEventCategory(event_name,shop_code,ctg_1,startNum,endNum);
				oldQ += "&action="+action+"&event_name="+event_name.replace("+", "%2B")+"&shop_code="+shop_code+"&ctg_1="+ctg_1;
		        end = ps2.getPageCount(event_name, shop_code);
		        pageEnd = ps2.getPageEnd(pgNum, event_name, shop_code);
		        nextdata = ps2.isNextData(pgNum, event_name, shop_code);
			}
		}
		
		
		mav.addObject("pgNum",pgNum);
		mav.addObject("oldQ",oldQ);
	    mav.addObject("end",end);
		//mav.addObject("end",ps2.getPageCount(event_name, shop_code));
		mav.addObject("pageStart",ps2.getPageStart(pgNum));
		//mav.addObject("pageEnd",ps2.getPageEnd(pgNum,event_name,shop_code));
		mav.addObject("pageEnd",pageEnd);
		mav.addObject("preData", ps2.isPreData(pgNum));
		//mav.addObject("nextData",ps2.isNextData(pgNum,event_name,shop_code));
		mav.addObject("nextData",nextdata);
		mav.addObject("gesList", geslist);
		mav.setViewName("event");
		return mav;
	}

	
}
