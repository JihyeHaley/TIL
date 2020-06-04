package service;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import javax.servlet.http.HttpServletResponse;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;
import org.springframework.stereotype.Service;

import dao.CartDAO;
import vo.GoodsEventShopMemberVO;
import vo.GoodsInformVO;

@Repository
@Service
public class ManHappyService {
	
	@Autowired
	CartDAO cdao;
	
	//카테고리 체크해줌
	public void checkCtg(String good_id,HttpServletResponse response) throws IOException{
		if(cdao.checkCtg(good_id)!=null) {
			response.getWriter().print("1");
		}else {
			response.getWriter().print("0");
		}
	}
	
	public void insertCart(GoodsEventShopMemberVO vo, HttpServletResponse response) throws IOException{
		if(cdao.cartInsert2(vo)) {
			response.getWriter().print("1");
		}else {
			response.getWriter().print("0");
		}
	}

	public void deleteCart(HttpServletResponse response) throws IOException{
		if(cdao.cartDelete2()) {
			response.getWriter().print("1");
		}else {
			response.getWriter().print("0");
		}
	}
	
	public List<GoodsEventShopMemberVO> getNameImg(String good_id) {
		return cdao.getNameImg(good_id);
	}
	
	public void recomGoods(String ctg_3, int max, HttpServletResponse response) throws IOException{
		List<GoodsInformVO> list = cdao.recomGoodsList(ctg_3, max);
		if(list != null) {
			response.getWriter().print("1");
		}else {
			response.getWriter().print("0");
		}
	}
	
	public void selectCtg_3(String ctg_3,String shop_name, HttpServletResponse response) throws IOException{
		List<GoodsInformVO> list = cdao.selectCtg_3(ctg_3,shop_name);
		if(list != null) {
			response.getWriter().print("1");
		}else {
			response.getWriter().print("0");
		}
	}
	

	public List<GoodsInformVO> recomAlgo(String ctg_3,String shop_name){
				
		List<GoodsInformVO> list = new ArrayList<>();
		
		switch(ctg_3) {
		
			case "치즈":
				list.addAll(cdao.selectCtg_3("잼", shop_name));
				break;
				
			case "간편조리식":
			case "스프" :
			case "라면" : 
			case "도시락" :
				list.addAll(cdao.selectCtg_2("김치",shop_name));
				list.addAll(cdao.selectCtg_3("생수",shop_name));
				list.addAll(cdao.selectCtg_3("쌀",shop_name));
				list.addAll(cdao.selectCtg_2("반찬",shop_name));
				list.addAll(cdao.selectCtg_3("즉석밥",shop_name));
				break;
				
			case "즉석밥" :
			case "쌀" :
				list.addAll(cdao.selectCtg_2("김치",shop_name));
				list.addAll(cdao.selectCtg_3("생수",shop_name));
				list.addAll(cdao.selectCtg_3("생선",shop_name));
				list.addAll(cdao.selectCtg_2("반찬",shop_name));
				list.addAll(cdao.selectCtg_3("김/해초",shop_name));
				list.addAll(cdao.selectCtg_3("즉석국/즉석탕",shop_name));
				list.addAll(cdao.selectCtg_3("라면",shop_name));
				list.addAll(cdao.selectCtg_3("젓갈",shop_name));
				break;

			case "케이크" :
			case "빵":
				list.addAll(cdao.selectCtg_3("우유", shop_name));
				list.addAll(cdao.selectCtg_3("두유", shop_name));
				break;
				
			case "시리얼" :
				list.addAll(cdao.selectCtg_3("우유", shop_name));
				list.addAll(cdao.selectCtg_3("두유", shop_name));
				list.addAll(cdao.selectCtg_3("오트밀", shop_name));
				break;
				
			//ctg_2 = '축산'	
			case "알류" :
			case "쇠고기" :
			case "축산가공품" :
			case "닭고기" :
			case "돼지고기" : 
				list.addAll(cdao.selectCtg_2("김치",shop_name));
				list.addAll(cdao.selectCtg_3("탄산",shop_name));
				break;
			
			case "과일":
				list.addAll(cdao.selectCtg_2("다이어트식품", shop_name));
				list.addAll(cdao.selectCtg_3("채소", shop_name));
				list.addAll(cdao.selectCtg_3("샐러드", shop_name));	
				break;
				
			case "햄버거" :
			case "튀김류" :
			case "기타냉동/간편조리식품" :
			case "피자" :
			case "핫도그" :
				list.addAll(cdao.selectCtg_3("청량/탄산음료", shop_name));
				list.addAll(cdao.selectCtg_3("탄산수", shop_name));
				break;
				
			case "샐러드":
				list.addAll(cdao.selectCtg_3("과일", shop_name));
				list.addAll(cdao.selectCtg_3("채소", shop_name));
				list.addAll(cdao.selectCtg_2("다이어트식품", shop_name));
				break;
				
			case "아이스크림":
			case "커피":
			case "주스/과즙음료":
				list.addAll(cdao.selectCtg_3("빵", shop_name));
				list.addAll(cdao.selectCtg_3("쿠키", shop_name));
				list.addAll(cdao.selectCtg_3("스낵", shop_name));
				list.addAll(cdao.selectCtg_3("기타과자", shop_name));
				break;
				
			case "초콜릿":
			case "강냉이":
				list.addAll(cdao.selectCtg_3("초콜릿", shop_name));
				list.addAll(cdao.selectCtg_3("강냉이", shop_name));
				break;
				
			case "푸딩":
			case "젤리":
				list.addAll(cdao.selectCtg_3("푸딩", shop_name));
				list.addAll(cdao.selectCtg_3("젤리", shop_name));
				break;
				
			case "사탕":
			case "강정":
			case "엿":
				list.addAll(cdao.selectCtg_3("사탕", shop_name));
				list.addAll(cdao.selectCtg_3("강정", shop_name));
				list.addAll(cdao.selectCtg_3("엿", shop_name));
				break;
			
			
			default : 
				list.addAll(cdao.selectCtg_3("생수",shop_name));
		}
		
		return list;
		
	}
}