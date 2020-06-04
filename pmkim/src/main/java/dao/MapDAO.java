package dao;

import java.util.List;

import org.apache.ibatis.session.SqlSession;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import vo.GoodsEventShopMemberVO;
import vo.MemberVO;

@Repository
public class MapDAO {
	private static final Logger logger = LoggerFactory.getLogger(MapDAO.class);
    @Autowired
    SqlSession sqlSession; // mybatis 실행 객체

	public List<MemberVO> memberListAll() {
		logger.info("Mybatis memberListAll");
		List<MemberVO> list = null;
		String statement = "resource.MapMapper.selectMemberList";
		list = sqlSession.selectList(statement);
		return list;
	}
	
	public GoodsEventShopMemberVO mapAlgorithmDB(GoodsEventShopMemberVO vo) {
		//logger.info("Mybatis mapAlgorithmDBList");
		String statement = "resource.MapMapper.mapAlgorithmDBList";
		//logger.info("mapAlgorithmDB dao: "+vo.getGood_name());
		vo = sqlSession.selectOne(statement, vo);
		// null 수정후 확인할것 !!
		//logger.info("mapAlgorithmDB dao: "+vo.getGood_name());
		return vo;
	}
	//selShopCodeNameDetail
	
	public GoodsEventShopMemberVO shopCodeName(GoodsEventShopMemberVO vo) {
		//logger.info("Mybatis shopCodeName");
		String statement = "resource.MapMapper.selShopCodeNameDetail";
		vo = sqlSession.selectOne(statement, vo);
		return vo;
	}
	
//	public GoodsEventShopMemberVO eventName(GoodsEventShopMemberVO vo) {
//	//logger.info("Mybatis eventName");
//	String statement = "resource.MapMapper.selEventName";
//	try{
//		vo = sqlSession.selectOne(statement, vo);
//	}catch(Exception e) {
//		logger.info("eventName exception : " + e);
//	}
//	return vo;
//}

	public List<GoodsEventShopMemberVO> eventName(GoodsEventShopMemberVO vo) {
		//logger.info("Mybatis eventName");
		String statement = "resource.MapMapper.selEventName";
		List<GoodsEventShopMemberVO> list = null;
		try{
			list = sqlSession.selectList(statement, vo);
		}catch(Exception e) {
			logger.info("eventName exception : " + e);
		}
		return list;
	}
	
	public List<GoodsEventShopMemberVO> shopCodeTableList() {
		//logger.info("Mybatis shopCodeTableList");
		List<GoodsEventShopMemberVO> list = null;
		String statement = "resource.MapMapper.shopCodeTableList";
		list = sqlSession.selectList(statement);
		return list;
	}
	
}

