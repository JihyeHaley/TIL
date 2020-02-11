# Lotto Proejct

*Feb 10 2020 Practice at Multi Campus

### Controller, VO, DAO, Service, html, jsp



##### LottoController1.java

~~~java
package my.spring.springedu;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import service.LottoService;
import vo.LottoVO;
@Controller // 가 service //가 dao를 사용하는 관계
public class LottoController1 {
	@Autowired
	private LottoService lottoService;	//lottoService에 의존적이다.
										//lottoDAO 찾아가게 해줌
	@RequestMapping("/lotto1")
	public String lottoProcess(LottoVO vo) {		
		if (lottoService.getLottoProcess(vo.getLottoNum())) {
			vo.setResult("추카추카!!");
		}else {
			vo.setResult("아쉽네요 .. 다음 기회를!!");
		}
		return "lottoView1";
	}
}
~~~



##### LottoVO.java

~~~java
package vo;
public class LottoVO {
	private int lottoNum;
	private String result;
	
	public LottoVO()  {
		System.out.println("LottoVO Create object");
	}
	public int getLottoNum() {
		return lottoNum;
	}
	
	public void setLottoNum(int lottoNum) {
		this.lottoNum = lottoNum;
	}
	
	public String getResult() {
		return result;
	}
	
	public void setResult(String result) {
		this.result = result;
	}	
}
~~~



##### LottoDAO.java

~~~java
package dao;
import java.util.Random;
import org.springframework.stereotype.Repository;
@Repository // COMPONENT라는 ANNOTATION을 지정하는거랑 똑같은 방식
public class LottoDAO {
	public LottoDAO()  {
		System.out.println("LottoDAO 객체생성");
	}
	public int getLottoNumber() {
		Random rand = new Random();
		return rand.nextInt(6)+1;
	}
}
~~~



##### LottoService.java

~~~java
package service;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import dao.LottoDAO;
@Service //spring객체에 의해서 관리되는 아이들 
public class LottoService {
	public LottoService()  {
		System.out.println("LottoService 객체생성");
	}
	@Autowired
	LottoDAO lottoDAO = null; //언제 객체 생성하는지 보라고!!!! //
	public boolean getLottoProcess(int lottoNum) {
		boolean result = false;		
		int randomNumber = lottoDAO.getLottoNumber(); //DAO에서 추출받아온 LottoNumber
		System.out.println("--- 난수: " + randomNumber);
		System.out.println("--- 입력한 수: " + lottoNum);
		if(randomNumber == lottoNum) 
			result = true;
		return result;
	}
} 

~~~



##### lottoForm1.html

~~~html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style>
	div{
		display: inline-block;
		width:120px;
		height: 120px;
	}
	img{
		width:100px;
		height: 100px;
	}
	.shadow img {
		transition: .5s ease;
	}
	
	.shadow img:hover{
		box-shadow:
		1px 1px #d9d9d9,
		2px 2px #d9d9d9,
		3px 3px #d9d9d9,
		4px 4px #d9d9d9,
		5px 5px #d9d9d9,
		6px 6px #d9d9d9;
		-webkit-transform: translateX(-3px);
		transform: translateX(-3px);
		transition: .5s ease;
	}
</style>
</head>
<body>
	<h1>Lotto Game</h1>
		<div><a href="/springedu/lotto1?lottoNum=1" class ="shadow"><img src="images/1.png" alt="1"></a></div>
		<div><a href="/springedu/lotto1?lottoNum=2" class ="shadow"><img src="images/2.png" alt="2"></a></div>
		<div><a href="/springedu/lotto1?lottoNum=3" class ="shadow"><img src="images/3.png" alt="3"></a></div>
		<div><a href="/springedu/lotto1?lottoNum=4" class ="shadow"><img src="images/4.png" alt="4"></a></div>
		<div><a href="/springedu/lotto1?lottoNum=5" class ="shadow"><img src="images/5.png" alt="5"></a></div>
		<div><a href="/springedu/lotto1?lottoNum=6" class ="shadow"><img src="images/6.png" alt="6"></a></div>
</body>
</html>
~~~



##### lottoView.jsp

~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<h1>로또 결과</h1>
	<hr>
	<h2>${ lottoVO.result }</h2>
	<%
		vo.LottoVO vo = (vo.LottoVO)request.getAttribute("lottoVO");
	%>
	<h2><%= vo.getResult() %></h2>
	<hr>
	<a href="/springedu/resources/lottoForm1.html">재시도.....</a>
</body>
</html>
~~~