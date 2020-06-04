package dao;

import org.apache.ibatis.session.SqlSession;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import spring.mvc.pmkim.MapController;
import vo.MemberVO;

@Repository
public class SignupDAOImpl implements SignupDAO {
	 //private static final Logger logger = LoggerFactory.getLogger(MapController.class);
	 @Autowired
	 private SqlSession sql;
	    
	 @Override
	 public void insertMember(MemberVO vo){
		 //logger.info("mybatis inserMember DAO");
//		 logger.info("id2: " + vo.getId());
//		 //logger.info("pw: " + vo.getPw());
//		 logger.info("name2: " + vo.getName());
//		 logger.info("email2: " + vo.getEmail());
//		 logger.info("email2: " + vo);
		 sql.insert("resource.MemberMapper.insertMember",vo);
	 }
	 
	 @Override
	 public int idCheck(String id) {
		 //System.out.println("여기는 dao");
		 return sql.selectOne("resource.MemberMapper.idCheck",id);
	 }

}
