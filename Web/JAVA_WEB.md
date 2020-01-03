# HTML



~~~html


<!DOCTYPE html>
<html> <!-- <안에 있는 걸 태그라고 표현한다.-->
<head>
<meta charset="EUC-KR">
//시작태그
<title>ㅋㅋㅋ</title>
</head>
<body>
<h1> go for 2020 </h1>
//시작태크    // 이 내용이 컨텐트 //종료태그
<hr>
// 분리선
<br>
// 행바꿈
</body>
</html>

~~~





```html
<ul>
	<li> Java Programming </li>
	<li> SQL </li>
	<li> HTML5 </li>
	<li> CSS3 </li>
	<li> JavaScript </li>
	<li> Ajax </li>
	<li> Servlet </li>
	<li> JSP</li>
	<li> JDBC </li>

</ul>

<ol> <!-- Ordered List  숫자를 앞에 붙여준다. 로마자나 다른 글잘를 붙여주거나는 css3를 통해서 할 수 있다.-->
	<li> Java Programming </li>
	<li> SQL </li>
	<li> HTML5 </li>
	<li> CSS3 </li>
	<li> JavaScript </li>
	<li> Ajax </li>
	<li> Servlet </li>
	<li> JSP</li>
	<li> JDBC </li>
</ol>
```







~~~html
<h2>태이블 테그</h2>
<table border = "1">
	<tr><th>언어이름</th><th>설명</th></tr> <!-- 제목행 -->
	<tr><td>Java</td><td>범용으로 활용되는 OOP 언어</td></tr> <!-- 컨텐츠행 -->
	<tr><td>JavaScript</td><td>동적인 웹 페이지 개발에 사용하는 opp 언어</td></tr>
	<tr><td>css</td><td>HTML의 스타일을 조정하는 언어</td></tr>
	<tr><td>R</td><td>통계 분석과 데이터 마이닝에 사용되는 언어</td></tr>
</table>
~~~



```html
<h2> 입력 폼 태그 </h2>
<form action = "..."method ="">
	<input type="text" placeholder ="이름을 입력하세요..." required name = "gname">
	<input type="submit" value ="전송">
</form>
```



Query String : Web Client  가 Web Server 에게 정보(페이지)를 요청할 대 함께 전달 가능한 name과 value 구성되는 문자열

 W3C가 정해놓기를 

1. name = value로 구성되어야 한다.
2. 여러개의 name=value  를 전달하는 경우에는 & 기호로 분리한다.
3. 영문과 숫자 그리고 일부 특수 문자를 제외하고는 %기호와 코드 값으로 전달된다.
4. 공백은 + 기호로 전달된다.

```

```



| - unico 영어 전송<br/><br/>  http://localhost:8000/edu/htmlexam/...?gname=unico<br/><br/>- 유니코 한글을 전송<br/><br/>  [http://localhost:8000/edu/htmlexam/...?gname=%EC%9C%A0%EB%8B%88%EC%BD%94](http://localhost:8000/edu/htmlexam/...?gname=유니코)<br/><br/>- 한글 + 숫자<br/><br/>  [http://localhost:8000/edu/htmlexam/...?gname=%EA%B0%80&gage=123](http://localhost:8000/edu/htmlexam/...?gname=가&gage=123)<br/><br/>- 한글 + 영어 + 숫자<br/><br/>  [http://localhost:8000/edu/htmlexam/...?gname=%EA%B0%80+ABC&gage=123]( |
| ------------------------------------------------------------ |
| **[placeholder에 썼을때!!]**<br/><br/>- unico 영어 전송<br/><br/>  http://localhost:8000/edu/htmlexam/...?gname=unico<br/><br/>- 유니코 한글을 전송<br/><br/>  [http://localhost:8000/edu/htmlexam/...?gname=%EC%9C%A0%EB%8B%88%EC%BD%94](http://localhost:8000/edu/htmlexam/...?gname=유니코)<br/><br/>- 한글 + 숫자<br/><br/>  [http://localhost:8000/edu/htmlexam/...?gname=%EA%B0%80&gage=123](http://localhost:8000/edu/htmlexam/...?gname=가&gage=123)<br/><br/>- 한글 + 영어 + 숫자 (공백은 + 기호로 표시된다.)<br/><br/>  [http://localhost:8000/edu/htmlexam/...?gname=%EA%B0%80+ABC&gage=123](http://localhost:8000/edu/htmlexam/...?gname=가+ABC&gage=123)<br/><br/>- Query String: Web Client가 Web Server에게 정보(페이지)를 요청할 때 함께 전달 가능한 name과 value 구성되는 문자열<br/><br/>  W3C가 정해놓기를<br/><br/>  1. name-value로 구성되어야 한다.<br/>  2. 여러개의 name=value를 전달하는 경우에는 & 기호로 분리한다.<br/>  3. 영문과 숫자 그리고 일부 특수문자를 제외하고는 %기호와 코드 값으로 전달된다.<br/>  4. 공백 + 기호로 전달된다. |



[http://localhost:8000/edu/htmlexam/...?gname=%EA%B0%80&gage=24&gdate=2020-01-03&gender=female&food=on](http://localhost:8000/edu/htmlexam/...?gname=가&gage=24&gdate=2020-01-03&gender=female&food=on)



http://localhost:8000/edu/Urgent.html --> 문자열

​									/    URI                    /



html을 읽어들이는 것을 '파싱'한다고 한다.

html은 반드시 WebContent  안에 있어야 하지만

서브 폴더에 다 넣는다.





http://localhost:8000/edu/htmlexam/exam1.html





http://html5test.com

~~~html
<!-- 교육에서 사용 할 수 있는 tag-->

<h1>This is heading 1가나다</h1>
<h2>This is heading 2</h2>
<h3>This is heading 3</h3>
<h4>This is heading 4</h4>
<h5>This is heading 5</h5>
<h6>This is heading 6</h6>

<p>Do not <mark>forget to buy 밀크우유</mark> today.</p>

<p>This is a paragraph.</p>
<p>This is a paragraph.</p>
<p>This is a paragraph.</p>

<hr>

This is a paragraph.<br>
This is a paragraph.<br>
This is a paragraph.<br>

<picture>
  <source media="(min-width: 650px)" srcset="img_pink_flowers.jpg">
  <source media="(min-width: 465px)" srcset="img_white_flower.jpg">
  <img src="img_orange_flowers.jpg" alt="Flowers" style="width:auto;">
</picture>

<figure>
  <img src="../html/pic_trulli.jpg" alt="Trulli" style="width:100%">
  <figcaption>Fig.1 - Trulli, Puglia, Italy.</figcaption>
</figure>

<textarea rows="4" cols="50">
At w3schools.com you will learn how to make a website. We offer free tutorials in all web development technologies.
</textarea>
~~~

