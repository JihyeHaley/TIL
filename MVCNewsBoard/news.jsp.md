~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ page import="model.vo.NewsVO, java.util.List"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Pooh World</title>
<style>
	
   @font-face {
   		src: url("/mvc/jspexam/SSShinb7.ttf");
   		font-family: "sb";
        
   }
   *{
      	font-family: "sb";
     	margin: 5;
      	padding: 2;
   }
	body{
		background-image:url("/mvc/jspexam/2222.jpg");
		font-family: "sb";
     	margin: 5;
      	padding: 2;
	}
	h1{
		text-align:center;
	}
	h2{
		font-size: 1.3em;
	}
	table {
		border-collapse: collapse;
		border-radius:5px;
		width: 100%;
		background-color: white;
	}
	th, td {
		text-align:center;
		padding: 8px;
		text-align: left;
		border-bottom: 1px dashed #ddd;
		table-layout: fixed;
	}
	th, td {
		text-align:center;
	}
	th {
		background-color:#ffcccc;
		text-size: 1.3em;
	}
	tr:hover {
		background-color: pink;
	}
	
	div{
		margin: auto;
		background-color:white;
		width: 300px;
		height: 430px;
		border-radius: 10px;
		text-align:center;
	}
	input[type="text"], textarea{
		font-size: 1.2em;
		border: 1px solid black;
		border-radius: 10px;
		margin: atuo;
		padding: 3px;
	}
	button, input[type="submit"], input[type="reset"]{
		background-color: #cc99ff;
		border : none;
		border-radius:5px;
		color: white;
		text-align:center;
		text-decoration:none;
		font-size:1.2em;
	}
</style>
</head>
<body>
	<h1>Hello! Pooh NEWS</h1>
	<hr>
	<table>
		<tr>
			<th width=50 style="color:tomato;">Number</th>
			<th width=150 style="color:orange;">Title</th>
			<th width=50 style="color:lime;">Writer</th>
			<th width=50 style="color:blue;">WriteDate</th>
			<th width=50 style="color:red;">Cnt</th>
		</tr>
	</table>

	<c:if test="${!empty listAll}">
		<c:forEach var="vo" items="${listAll}" varStatus="status">
			<table>
				<tr>
					<td width=50><c:out value="${vo.id}" />.</td>
					<td width=150><a href="/mvc/news?action=read&newsid=${vo.id}">
							<c:out value="${vo.title}" />
					</a></td>
					<td width=50><c:out value="${vo.writer}" /></td>
					<td width=50><c:out value="${vo.writedate}" /></td>
					<td width=50><c:out value="${vo.cnt}" /></td>
				<tr>
			</table>
		</c:forEach>
	</c:if>
	<hr>
	<br>
	
	<input id="hidden2" name="action" value="search">
	<input id="news_id2" type="text" name="newsid" style="display: none" value="${listOne.id }">
	<button type="button" onClick="location.href='/mvc/news?action=search&newsid=${listOne.id}'">Search News</button>
	
	
	<input id="hidden2" type="hidden" name="action" value="update">
	<br><button style="text-align:right;" id="writenews" type="button" onclick="displayWriteForm()">Write News</button>
	<c:if test="${!empty listOne}">
		<div id="news_update" style="display: black">
			<br>
			<h2 id="news_header2" style="font-size:1.3em;" >News Contents</h2>
			<form method="post" action="/mvc/news">
				Writer : <br><input id="news_writer2" type="text" name="writer" value="${listOne.writer}"><br>
				<br>Title : <br><input id="news_title2" type="text" name="title" value="${listOne.title}"><br>
				<br>Content :
				<br><textarea id="news_content2" rows="5" cols="27" name="content">${listOne.content}</textarea>
				<br><br>
					<button type="button" onclick="location.href='/mvc/news' ">Confirm</button>
					<input type="submit" value="Edit">
					<button type="button"
						onclick="location.href='/mvc/news?action=delete&newsid=${listOne.id}'">Delete</button>
				<br>
			
			</form>
	</c:if>
	</div>

	<c:if test="${!empty msg}">
		<h4>${msg}</h4>
	</c:if>
	
	<script>
		function displayWriteForm() {
			document.getElementById("news_form").style.display = "block";
			document.getElementById("news_update").style.display = "none";
		}
	</script>
	<div id="news_form" style="display: none">
	<br>
		<h2 id="news_header" style="font-size:1.3em;" >News Contents</h2>
		<form method="post" action="/mvc/news">
			<input id="hidden1" type="hidden" name="action" value="insert">
			Writer : <br><input id="news_writer" type="text" name="writer" value="Writer"><br>
			<br> Title : <br><input id="news_title" type="text" name="title" value="Title">
			<br><br>Content : 
			<br><textarea id="news_content" rows="5" cols="27" name="content"></textarea>
			<br><br>
				<input id="news_id" type="text" name="newsid"
					style="display: none"> <input type="submit" value="Confirm">
				<input type="reset" value="Rewrite">
				<button type="button" onclick="location.href='/mvc/news'">Cancel</button>
				<br><br>
				<a href="/mvc/news">Back to News Home</a>
			<br>
		</form>
	</div>
	<br><br>
</body>
</html>
~~~

