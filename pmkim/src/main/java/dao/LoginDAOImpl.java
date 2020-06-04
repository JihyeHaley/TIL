package dao;

import javax.servlet.http.HttpSession;

import org.apache.ibatis.session.SqlSession;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import spring.mvc.pmkim.MapController;
import vo.MemberVO;

@Repository
public class LoginDAOImpl implements LoginDAO {
	//private static final Logger logger = LoggerFactory.getLogger(MapController.class);
	@Autowired
	SqlSession sql;
	
	@Override
	public boolean loginCheck(MemberVO vo) {
		boolean result = false;
		String statement = "resource.MemberMapper.loginCheck";
//		logger.info("logincheck dao!!");
//		logger.info("idLoginCheck:"+vo.getId());	
//		logger.info("NameLoginCheck:"+vo.getName());
		if(sql.selectOne(statement,vo) != null)
			result=true;				
		return result;
	}

	@Override
	public MemberVO viewMember(MemberVO vo) {
		String statement = "resource.MemberMapper.viewMember";
		return sql.selectOne(statement, vo);
	}

	@Override
	public void logout(HttpSession session) {

	}

}
