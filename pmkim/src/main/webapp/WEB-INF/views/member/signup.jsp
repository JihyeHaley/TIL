<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<script src="http://code.jquery.com/jquery-latest.js"></script>
<script>
$(function(){
	$("#joinForm").submit(function(){
		//비밀번호 입력
		//비밀번호 맞나 체크도
		if($("#pw").val() !== $("#pw2").val()){
			alert("비밀번호가 다릅니다!");
			//지우기
			$("#pw").val("").focus();
			$("#pw2").val("");
			return false;
		}else if ($("#pw").val().length <8) {
			alert("비밀번호는 8자 이상으로 설정해야 합니다!");
			$("#pw").val("").focus();
			return false;
		}else if ($.trim($("#pw").val()) !== $("#pw").val() || $.trim($("#email").val()) !== $("#email").val() ||
		$.trim($("#id").val()) !== $("#id").val()){
		alert("공백은 입력이 불가능합니다!") //공백 제거해주는 함수 trim()
		return false;
		}
	})
	
	//아이디 입력
	("#id").keyup(function() {
		$.ajax({
			url : "../member/check_id",
			type : "POST",
			data : {
				id : $("#id").val()
			},
			success : function(result) {
				if (result == 1) {
					$("#id_check").html("중복된 아이디가 있습니다.");
					$("#joinBtn").attr("disabled", "disabled");
				} else {
					$("#id_check").html("");
					$("#joinBtn").removeAttr("disabled");
				}
			},
		})
	});
	
	//이메일 입력
	$("#email").keyup(function(){
		$.ajax({
			url : "./check_email",
			type : "POST",
			data : {
				email : $("#email").val()
			},
			success : function(result) {
				if (result == 1) {
					$("#email_check").html("중복된 이메일이 있습니다.");
				} else {
					$("#email_check").html("");
				}
			},
		})
	});
})
	
	
	
</script>
<title>회원가입 폼</title>
</head>
<body>
	<br><br><br>
	<div class ="w3-center w3-large pmkim-logo">
		<img src="/pmkim/resources/images/Pmkim_Signup_Logo.jpg" class="logo" alt="">
	</div>
	<br><br>
	<div class="w3-content w3-container w3-margin-top">
		<div class="w3-container w3-card-4">
			<div class="w3-center w3-large w3-margin-top">
				<h3><b>회원가입</b></h3>
			</div>
			<div>
				<form id="joinForm" action="/pmkim/signup" method="post">
					<p>
						<label>아이디</label> 
						<input class="w3-input" type="text" id="id" name="id" required> 
						<span id="id_check" class="w3-text-red"></span>
					</p>
					<p>
						<label>패스워드</label> 
						<input class="w3-input" id="pw" name="pw" type="password" required>
					</p>
					<p>
						<label>패스워드 확인</label>
						<input class="w3-input" id="pw2" name="pw2" type="password" required>
					</p>
					<!-- id, pw, name, tel_num, email, sign_date, nick_name, road_addr, login_type, member_type -->
					<p>
						<label>이름</label>
						<input type="text" id="name" name="name" class="w3-input" required>
					</p>
					<p>
						<label>이메일</label>
						<input type="text" id="email" name="email" class="w3-input" required>
						<span id="email_check" class="w3-text-red"></span>
					</p>
					<p>
						<label>전화번호</label>
						<input type="text" id="tel_num" name="tel_num" class="w3-input" required>
					</p>
					<p>
						<label>닉네임</label>
						<input type="text" id="nick_name" name="nick_name" class="w3-input" required>
					</p>
					<p>
						<label>도로명 주소</label>
						<input type="text" id="road_addr" name="road_addr" class="w3-input" required>
					</p>
					<!-- <p>회원 가입 사이트 : 
					<input type = "radio" name = "login_type" value = "pmkim" >일반
        			<input type = "radio" name = "login_type" value = "naver">네이버
        			<input type = "radio" name = "login_type" value = "kakao">카카오
					<input type = "radio" name = "login_type" value = "google">구글
					</p> -->
					<p>회원 유형 : 
						<input type = "radio" name = "member_type" value = "owner">사장님
						&nbsp;
	        			<input type = "radio" name = "member_type" value = "customer">일반회원
					</p>
					<p class="w3-center">
							<button type="submit" id="joinBtn" class="w3-button w3-block w3-ripple w3-margin-top w3-round" style="background-color:#0F694D">Join</button>
							<button type="button" onclick="history.go(-1);" class="w3-button w3-block w3-ripple w3-margin-top w3-margin-bottom w3-round" style="background-color:#0F694D">Cancel</button>						
					</p>
				</form>
			</div>
		</div>
	</div>
</body>
</html>