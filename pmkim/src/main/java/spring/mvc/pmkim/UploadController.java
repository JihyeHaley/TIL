package spring.mvc.pmkim;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

@Controller
public class UploadController {

	@RequestMapping(value = "/upload", method = RequestMethod.GET)
	protected String upload() {
		return "/upload";
	}
	
}
