package service;

import javax.servlet.http.HttpSession;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import dao.LoginDAO;
import spring.mvc.pmkim.MapController;
import vo.MemberVO;

@Service
public class LoginServiceImpl implements LoginService {
	//private static final Logger logger = LoggerFactory.getLogger(MapController.class);
	@Autowired
	LoginDAO dao;
	@Override
	public boolean loginCheck(MemberVO vo,HttpSession session) {
		//logger.info("vo-id : "+vo.getId());
		boolean result = dao.loginCheck(vo);
		//logger.info("loginCheck service!!");
		//logger.info("result = " + result);
		if(result) {
			MemberVO newVO = viewMember(vo);
			session.setAttribute("id", newVO.getId());
			//session.setAttribute("name", newVO.getName());
			//logger.info("session id: "+session.getAttribute("id").toString());
			//logger.info("session name: "+session.getAttribute("name").toString());
		}
		return result;
	}

	@Override
	public MemberVO viewMember(MemberVO vo) {
		return dao.viewMember(vo);
	}
	

	@Override
	public void logout(HttpSession session) {
		session.invalidate();
	}

}
