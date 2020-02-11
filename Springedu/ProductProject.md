# Product Project

*Feb 10 2020 Practice at Multi Campus

### Controller, VO, html, jsp,  



##### ProductController.java

~~~java
package my.spring.springedu;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.SessionAttributes;
//import org.springframework.web.bind.support.SessionStatus;

import vo.ProductVO;

@Controller
@SessionAttributes("prosession") //session 객체에 보관하겠다는 뜻!!!
public class ProductController{
	@ModelAttribute("prosession")
	public ProductVO productMethod1() {
		System.out.println("prosessionMethod 호출 - prosession");
		return new ProductVO();
	}
	
	@RequestMapping(value="/product")
	public String hh(@ModelAttribute("prosession") ProductVO vo, String pid) {
	
		if(pid!=null){
			if(pid.equals("p001")) {vo.setAppleCnt(1);}
			if(pid.equals("p002")) {vo.setBananaCnt(1);}
			if(pid.equals("p003")) {vo.setHalabongCnt(1);}
		}
		return "product";
	}
}

~~~



##### ProductVO.java

~~~java
package vo;

public class ProductVO {
	private int halabongCnt;
	private int bananaCnt;
	private int appleCnt;
	
	public int getHalabongCnt() {
		return halabongCnt;
	}
	public void setHalabongCnt(int halabongCnt) {
		this.halabongCnt += halabongCnt;
	}
	public int getBananaCnt() {
		return bananaCnt;
	}
	public void setBananaCnt(int bananaCnt) {
		this.bananaCnt += bananaCnt;
	}
	public int getAppleCnt() {
		return appleCnt;
	}
	public void setAppleCnt(int appleCnt) {
		this.appleCnt += appleCnt;
	}
	
}
~~~



##### product.html

~~~html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>Choose your product</h1>
<hr>
	<form method="post" action="/springedu/product">
		<a href="/springedu/product?pid=p001"><img src="/edu/images/jihyes.png" width="200px;"/></a>
		<a href="/springedu/product?pid=p002"><img src="/edu/images/gas_park.jpg" width="200px;"/></a>
		<a href="/springedu/product?pid=p003"><img src="/edu/images/kerry_park.jpg" width="200px;"/></a>
	</form>
	
</body>
</html>
~~~



##### Product.jsp

~~~jsp
<%@page import="vo.ProductVO"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<%
	ProductVO vo=(ProductVO)request.getAttribute("prosession");
%>
	<h1>List of your shopping</h1>
	<hr>
	<ul>
		<li>Oliver: <%= vo.getAppleCnt() %> </li>
		<li>GasPark: <%= vo.getBananaCnt() %></li>
		<li>KerryPark: <%= vo.getHalabongCnt() %></li>
	</ul>

	<a href="<%= request.getHeader("referer") %>">Back to online shopping center</a>
</body>
</html>
~~~