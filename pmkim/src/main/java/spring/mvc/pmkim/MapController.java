package spring.mvc.pmkim;

import java.io.IOException;
import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletResponse;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.servlet.ModelAndView;

import dao.MapDAO;
import service.MapService;
import vo.GoodsEventShopMemberVO;

@Controller
public class MapController {
	private static final Logger logger = LoggerFactory.getLogger(MapController.class);

	@Autowired
	MapDAO dao;
	@Autowired
	MapService mapService;

	@RequestMapping(value = "/map", method = RequestMethod.GET)
	public ModelAndView mapGet(String searchKeyword, String searchProduct,
			GoodsEventShopMemberVO goodsEvtShopMemberVO) {
		ModelAndView mav = new ModelAndView();
		
		//logger.info("controller searchProduct: " + searchProduct);
		if(goodsEvtShopMemberVO != null) {
			logger.info("controller shop_code: " + goodsEvtShopMemberVO.getShop_code());
			System.out.println("controller shop_code: " + goodsEvtShopMemberVO.getShop_code());
		}
		//logger.info("controller shop_code: " + goodsEvtShopMemberVO.getShop_code());
		mav.addObject("goodsEvtShopMemberVO", goodsEvtShopMemberVO);
		mav.addObject("searchKeyword", searchKeyword);
		mav.addObject("searchProduct", searchProduct);
		mav.setViewName("/map");
		return mav;
	}
	
	
	// ajax에서 받을 때 한글 깨짐 현상이 있어서 추가함 -> produces = "application/text; charset=utf8"
	//, produces = "application/text; charset=UTF-8"
	@RequestMapping(value = "/map", method = RequestMethod.POST)
	@ResponseBody
	public void mapPost(String searchKeyword, String searchProduct, boolean goodNameFlag,
			GoodsEventShopMemberVO goodsEvtShopMemberVO, HttpServletResponse response) throws ServletException, IOException{
		//logger.info("controller goodNameFlag: " + goodNameFlag);
		//logger.info("controller searchProduct: " + searchProduct);
		
		if(goodsEvtShopMemberVO != null) {		
			//System.out.println("Controller : "+ goodsEvtShopMemberVO.getShop_code());
			//System.out.println("Controller : " + goodsEvtShopMemberVO.getShop_name_detail());

			if(searchProduct != null) goodsEvtShopMemberVO.setGood_name(searchProduct);
			if(goodNameFlag == true) {
				//logger.info("goodNameFlag : true");
				mapService.searchEventName(goodsEvtShopMemberVO, response);
			}else {
				//logger.info("goodNameFlag : false");
				mapService.searchStore(goodsEvtShopMemberVO, response);
			}
		}
	}
	
	@RequestMapping(value = "/map/data", method = RequestMethod.POST)
	@ResponseBody
	public List<GoodsEventShopMemberVO> mapPostData(String searchProduct,
			GoodsEventShopMemberVO goodsEvtShopMemberVO, HttpServletResponse response) throws ServletException, IOException{

		if(goodsEvtShopMemberVO != null) {		
			if(searchProduct != null) goodsEvtShopMemberVO.setGood_name(searchProduct);
		}
		return mapService.searchEventName(goodsEvtShopMemberVO, response);
	}


}
