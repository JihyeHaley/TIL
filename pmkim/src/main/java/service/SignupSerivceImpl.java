package service;

import java.io.IOException;

import javax.servlet.http.HttpServletResponse;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import dao.SignupDAO;
import spring.mvc.pmkim.MapController;
import vo.MemberVO;

@Service
public class SignupSerivceImpl implements SignupService {
	private static final Logger logger = LoggerFactory.getLogger(MapController.class);
	@Autowired
	private SignupDAO dao;	    	
	
	@Override
	public void insertMember(MemberVO vo) {
		//logger.info("mybatis service inserMember");
		dao.insertMember(vo);
	}
	
	@Override
    public void idCheck(String id, HttpServletResponse response) throws IOException{
		//System.out.println("여기는 service");
		int num = dao.idCheck(id);
		
		if(num==0) {
			response.getWriter().print("1");
		}else {
			response.getWriter().print("0");
		}
	}
}
