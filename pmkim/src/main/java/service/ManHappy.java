package service;

import java.io.IOException;

import javax.servlet.http.HttpServletResponse;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;
import org.springframework.stereotype.Service;

import dao.CartDAO;
import vo.GoodsEventShopMemberVO;

@Repository
@Service
public class ManHappy {
	
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
}
