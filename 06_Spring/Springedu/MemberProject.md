# Member Project

*Feb 10 2020 Practice at Multi Campus

#### Controller, VO, html, jsp 



##### MebmerController

~~~java
package my.spring.springedu;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import vo.MemberVO;

@Controller
public class MemberController{
	@RequestMapping("/members")
	public ModelAndView members(MemberVO vo){
		ModelAndView mav = new ModelAndView();
		String name = vo.getName();
		String phone = vo.getPhone().replaceAll("[^0-9]","");
		String id = vo.getId();
		String pw = vo.getPw();
		
		System.out.println(name+phone+id+pw);
		
		if(name.equals("")) {
			vo.setName("NULL");
			mav.addObject("member", "null");
		}else{
			vo.setName(name);
			mav.addObject("member", name);
		}
		
		if(phone.equals("")){
			vo.setPhone("NULL");
			mav.addObject("member", "null");
		}else{
			vo.setPhone(phone);
			mav.addObject("member", phone);
		}
		
		if(id.equals("")){
			vo.setId("NULL");
			mav.addObject("member", "null");
		}else{
			vo.setId(id);
			mav.addObject("member", id);
		}
		
		if(pw.equals("")){
			vo.setPw("NULL");
			mav.addObject("member", "null");
		}else{
			vo.setPw(pw);
			mav.addObject("member", pw);
		}
		mav.setViewName("memberView");
		return mav;
	}
}
~~~



##### MemberVO

~~~JAVA
package vo;

public class MemberVO {
	String name;
	String phone;
	String id;
	String pw;
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getPhone() {
		return phone;
	}
	public void setPhone(String phone) {
		this.phone = phone;
	}
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getPw() {
		return pw;
	}
	public void setPw(String pw) {
		this.pw = pw;
	}
}
~~~



##### MemberForm.html

~~~html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<style>
	form{
		margin-left : 10px;
	}
	p > input{
		text-radius : 10px;
		border-radius: 30px;
		width : 300px;
		height : 25px;
	}
</style>
<body>
	<form action="/springedu/members" method ="post">
	<h1>Input Member Information Here</h1>
	<hr>
		<p><input type="text" required name = "name" placeholder="Name"></p><br>
		<p><input type="number" required name = "phone" placeholder="Phone NO." pattern="[0-9]{3}-[0-9]{4}-[0-9]{4}"><br>
		<p><input type="text" required name = "id" placeholder="ID"></p><br>
		<p><input type="password" required name = "pw" placeholder="Password"></p><br>
		<input type="submit" style="border-radius: 10px; width : 60px; height : 30px; font-weight:bold" value="등록">
	<input type="reset" style="border-radius: 10px; width : 60px; height : 30px; font-weight:bold" value="재작성">
	</form>
	
</body>
</html>
~~~



##### MemberView.jsp

~~~jsp
<%@page import="vo.MemberVO"%>
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
	MemberVO vo=(MemberVO)request.getAttribute("member");
%>
	<h1> Member Information</h1>
	<hr>
	<ul>
		<li>Name: <%= vo.getName() %> </li><br>
		<li>ID: <%= vo.getId() %></li><br>
		<li>PW: <%= vo.getPw() %></li><br>
		<li>PHONE: <%= vo.getPhone() %></li><br>
	</ul>
</body>
</html>
~~~

