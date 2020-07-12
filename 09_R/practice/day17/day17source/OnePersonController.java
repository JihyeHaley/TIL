package edu.spring.redu;

import java.io.File;

import javax.servlet.http.HttpServletRequest;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import rtest.OnePersonService;

@Controller
public class OnePersonController {
	@Autowired
	OnePersonService sr;
	
	@RequestMapping("/map7")
	public ModelAndView getMyMap(HttpServletRequest req) {
		ModelAndView mav = new ModelAndView();
		// 실제 톰캣 path를 확인해 보자!! -> 실제 path와 다르고 톰캣이 알아서 관리하는 path를 따로 관리한다.
		String real_path = req.getSession().getServletContext().getRealPath("/");
		//System.out.println(real_path);
	    real_path = real_path.replace("\\", "/");
	    //System.out.println(real_path);		
	    // resources 브라우저에서 바로 요처어할 수 있는 path
		File f = new File(real_path+"/resources/leafletSeoulGu");
		if(!f.exists()) f.mkdir();
		String gu = req.getParameter("gu");
		if(gu == null)
			gu = "양천구";
		String result = sr.returnmap7(real_path+"/resources/leafletSeoulGu", gu);
		mav.addObject("leafletOne", "http://localhost:8000/redu/resources/leafletSeoulGu/"+result);
		mav.setViewName("oneView");
		return mav;
	}
}
