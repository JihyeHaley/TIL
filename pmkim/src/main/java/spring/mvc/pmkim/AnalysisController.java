package spring.mvc.pmkim;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletResponse;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.servlet.ModelAndView;

import dao.AnalysisDAO;
import vo.AnalysisVO;

@Controller
public class AnalysisController {

	@Autowired
	private AnalysisDAO AnalysisDAO;

	@RequestMapping(value="/analysis")
	public ModelAndView main(AnalysisVO avo) {
		ModelAndView mav = new ModelAndView();
		List<AnalysisVO> li = AnalysisDAO.allGoods2(avo);
		System.out.println(li.size());
		mav.addObject("analysis", li);
		mav.setViewName("analysis");
		return mav;
	}
	
	@RequestMapping(value="/analysis", method=RequestMethod.POST)
	@ResponseBody
	public List<AnalysisVO> ajax(AnalysisVO avo, HttpServletResponse response) throws ServletException, IOException{
		List<AnalysisVO> li = AnalysisDAO.allGoods(avo);
		return li;
	}
	
	@RequestMapping("/wordcloud")
	@ResponseBody
	public String analysis(String shop_code, HttpServletResponse response) throws ServletException, IOException {
		String result = "";
		try (BufferedReader br = new BufferedReader
				(new InputStreamReader
						(new FileInputStream("/pmkim/"+shop_code+".html"),"UTF8"));) {
			String data;
			while (true) {
				data = br.readLine();
				result += data+"\n";
				if (data == null)
					break;
			}
		} catch (FileNotFoundException fnfe) {
			System.out.println("파일이 존재하지 않습니다.");
		} catch (IOException ioe) {
			System.out.println("파일을 읽을 수 없습니다.");
		}
		System.out.println(result);
		return result;
	}
}
