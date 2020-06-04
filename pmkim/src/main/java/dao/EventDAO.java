package dao;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import vo.GoodsCategoryEventShopMemberVO;
import vo.GoodsEventShopMemberVO;

@Repository
public class EventDAO {

	@Autowired
	SqlSession session = null;

	
	//상품검색
	   public List<GoodsEventShopMemberVO> searchGoods(String good_name){
	      List<GoodsEventShopMemberVO> list = new ArrayList<GoodsEventShopMemberVO>();
	      String statement = "resource.CartMapper.searchGoods";
	      list = session.selectList(statement,good_name);
	      return list;
	   }
	   
	 //상품검색
		public List<GoodsCategoryEventShopMemberVO> searchGoods2(String good_name){
			List<GoodsCategoryEventShopMemberVO> list = new ArrayList<>();
			String statement = "resource.EventMapper.searchGoods";
			list = session.selectList(statement,good_name);
			return list;
		}

	//paging(sort)
	public int listCount(String event_name, String shop_code) {
		int count = 0;
		String statement = "resource.EventMapper.listCount";
		if(session.selectOne(statement)!=null) {
			Map<String,String> map = new HashMap<String,String>();
			map.put("event_name", event_name);
			map.put("shop_code", shop_code);
			count = session.selectOne(statement,map);
		}else {
			System.out.println("null이에유");
		}
		return count;
	}
	
	//paging (search)
	   public int listCount2(String good_name) {
	      int count = 0;
	      String statement = "resource.EventMapper.listCount_search";
	      if(session.selectOne(statement)!=null) {
	         count = session.selectOne(statement,good_name);
	      }else {
	         System.out.println("null이에유");
	      }
	      return count;
	   }
	//상품 전체 리스트 출력
	public List<GoodsCategoryEventShopMemberVO> goodsAll(){
		List<GoodsCategoryEventShopMemberVO> list = new ArrayList<GoodsCategoryEventShopMemberVO>();
		String statement = "resource.EventMapper.goodsListAll";
		list = session.selectList(statement);
		return list;
	}
	//shopName으로 찾아오기
		public List<GoodsEventShopMemberVO> goodsSortShop(String shop_code) {
			List<GoodsEventShopMemberVO> list = new ArrayList<GoodsEventShopMemberVO>();
			String statement = "resource.EventMapper.goodsList_shopName";
			list = session.selectList(statement,shop_code);
			return list;
		}
		
		//eventName으로 찾아오기
		public List<GoodsCategoryEventShopMemberVO> goodsSortEvent(String event_name){
			List<GoodsCategoryEventShopMemberVO> list = new ArrayList<GoodsCategoryEventShopMemberVO>();
			String statement = "resource.EventMapper.goodsList_eventName";
			list = session.selectList(statement,event_name);
			return list;
		}
		
		//shopName&eventName 모두로 찾아오기
		public List<GoodsCategoryEventShopMemberVO> goodsShopEvent(String event_name, String shop_code){
			List<GoodsCategoryEventShopMemberVO> list = new ArrayList<GoodsCategoryEventShopMemberVO>();
			String statement = "resource.EventMapper.goodsList_shopEvent";
			Map<String,String> map = new HashMap<String,String>();
			map.put("event_name", event_name);
			map.put("shop_code", shop_code);
			//System.out.println(map.keySet());
			list = session.selectList(statement,map);
			//System.out.println("list : "+ list);
			return list;
		}
		
		//shopName&eventName&Category 모두로 찾아오기
				public List<GoodsCategoryEventShopMemberVO> goodsShopEventCategory(String event_name, String shop_code, String ctg_1){
					List<GoodsCategoryEventShopMemberVO> list = new ArrayList<GoodsCategoryEventShopMemberVO>();
					String statement = "resource.EventMapper.goodsList_shopEventCategory";
					Map<String,String> map = new HashMap<String,String>();
					map.put("event_name", event_name);
					map.put("shop_code", shop_code);
					map.put("ctg_1", ctg_1);
					//System.out.println(map.keySet());
					list = session.selectList(statement,map);
					//System.out.println("list : "+ list);
					return list;
				}
		
		
		//shopName&eventName 모두로 찾아오기 + paging
			public List<GoodsCategoryEventShopMemberVO> goodsShopEvent(String event_name, String shop_code, int startNum, int endNum){
				List<GoodsCategoryEventShopMemberVO> list = new ArrayList<GoodsCategoryEventShopMemberVO>();
				String statement = "resource.EventMapper.goodsList_shopEvent_paging";
				Map<String,Object> map = new HashMap<String,Object>();
				map.put("startNum",startNum);
				map.put("endNum", endNum);
				map.put("event_name", event_name);
				map.put("shop_code", shop_code);
				System.out.println("startNum" + startNum);
				System.out.println("endNum" + endNum);
				System.out.println("eventName" + event_name);
				System.out.println("shopCode" + shop_code);
				list = session.selectList(statement,map);
				//System.out.println("list : "+ list);
				return list;
			}
			
			//shopName&eventName&Category 모두로 찾아오기 + paging
			public List<GoodsCategoryEventShopMemberVO> goodsShopEventCategory(String event_name, String shop_code, String ctg_1, int startNum, int endNum){
				List<GoodsCategoryEventShopMemberVO> list = new ArrayList<GoodsCategoryEventShopMemberVO>();
				String statement = "resource.EventMapper.goodsList_shopEventCategory_paging";
				Map<String,Object> map = new HashMap<String,Object>();
				map.put("startNum",startNum);
				map.put("endNum", endNum);
				map.put("event_name", event_name);
				map.put("shop_code", shop_code);
				map.put("ctg_1", ctg_1);
				System.out.println("startNum" + startNum);
				System.out.println("endNum" + endNum);
				System.out.println("eventName" + event_name);
				System.out.println("shopCode" + shop_code);
				System.out.println("ctg_1" + ctg_1);
				list = session.selectList(statement,map);
				//System.out.println("list : "+ list);
				return list;
			}
			//2020.05.29 추가
			   //상품검색_paging
			   public List<GoodsCategoryEventShopMemberVO> searchGoodsPaging(String good_name, int startNum, int endNum){
			      List<GoodsCategoryEventShopMemberVO> list = new ArrayList<GoodsCategoryEventShopMemberVO>();
			      Map<String,Object> map = new HashMap<String,Object>();
			      map.put("startNum",startNum);
			      map.put("endNum", endNum);
			      map.put("good_name", good_name);
			      String statement = "resource.EventMapper.goodsList_search_paging";
			      list = session.selectList(statement,map);
			      return list;
			   }
							
			
	//=======================Home===============================================//		
	//Home에서 쓸거
				//shopName&eventName 모두로 찾아오기
				public List<GoodsEventShopMemberVO> homeEventOne(String event_name, String shop_code){
					List<GoodsEventShopMemberVO> list = new ArrayList<GoodsEventShopMemberVO>();
					String statement = "resource.EventMapper.goodsList_One";
					Map<String,Object> map = new HashMap<String,Object>();
					map.put("event_name", event_name);
					map.put("shop_code", shop_code);
					//System.out.println(map.keySet());
					list = session.selectList(statement,map);
					//System.out.println("list : "+ list);
					return list;
				}
				//shopName&eventName 모두로 찾아오기
				public List<GoodsEventShopMemberVO> homeEventTwo(String event_name, String shop_code){
					List<GoodsEventShopMemberVO> list = new ArrayList<GoodsEventShopMemberVO>();
					String statement = "resource.EventMapper.goodsList_Two";
					Map<String,Object> map = new HashMap<String,Object>();
					map.put("event_name", event_name);
					map.put("shop_code", shop_code);
					//System.out.println(map.keySet());
					list = session.selectList(statement,map);
					//System.out.println("list : "+ list);
					return list;
				}
				//shopName&eventName 모두로 찾아오기
				public List<GoodsEventShopMemberVO> homeEventPB(String event_name, String shop_code){
					List<GoodsEventShopMemberVO> list = new ArrayList<GoodsEventShopMemberVO>();
					String statement = "resource.EventMapper.goodsList_PB";
					Map<String,Object> map = new HashMap<String,Object>();
					map.put("event_name", event_name);
					map.put("shop_code", shop_code);
					//System.out.println(map.keySet());
					list = session.selectList(statement,map);
					//System.out.println("list : "+ list);
					return list;
				}
}