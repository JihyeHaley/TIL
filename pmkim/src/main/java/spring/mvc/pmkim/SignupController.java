package spring.mvc.pmkim;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import service.SignupService;
import vo.MemberVO;

@Controller
public class SignupController extends HttpServlet{
	private static final Logger logger = LoggerFactory.getLogger(MapController.class);
	private static final long serialVersionUID = 1L;
	@Autowired
    private SignupService sService;
    
    @RequestMapping(value="/signup", method=RequestMethod.GET)
    public String signupGET(){
        return "/member/signup";
    }
    
    @RequestMapping(value="/signup", method=RequestMethod.POST)
    public String signupPOST(MemberVO vo){
    	logger.info("id: " + vo.getId());
    	//logger.info("pw: " + vo.getPw());
    	logger.info("name: " + vo.getName());
    	logger.info("email: " + vo.getEmail());
    	logger.info("email: " + vo.getLogin_type());
    	
        sService.insertMember(vo);
        
        return "/home";
		//response.sendRedirect("/pmkim/home");
    }
    
    @RequestMapping(value="/idcheck", method=RequestMethod.POST)
    @ResponseBody
    public void idCheck(HttpServletResponse response, @RequestParam("id")String id) throws IOException {
    	//System.out.println("여기는 controller");
    	sService.idCheck(id, response);
    }
}