<%@ page language="java" contentType="text/plain; charset=UTF-8"%>
<% String news[] = { "SW융합클러스터, 지방 SW교육 지원…SW교육격차 해소 첨병",
		"메모리에 강한 한국, SW정의 구현 최적지",
		"'게임대상' 배틀그라운드 '더게임어워드'까지 거머쥐다",
  	    "페이스북, 2019년부터 우리 정부에 세금낸다...애플, 구글, 아마존은?",
		"여성 쇼핑몰만 모아서 보여주는 쇼핑앱 '쇼즐' iOS 버전 출시",
		"드론 뜨자 '조종 교관' 새 일자리로 뜬다",
		"KAIST·서울대, 메탄올 생산하는 로듐 단일 원자 촉매 개발"}; %>
<% response.setHeader("Cache-Control", "no-cache"); %>
<% int num = (int)(Math.random() * 7);%>
{ 
	"news" : "<%= news[num] %>"
}