<%@ page contentType="application/json; charset=utf-8"%>
<%
   if (request.getParameter("id").equals("ajaxtest") && 
		request.getParameter("passwd").equals("12345")) {
%>
{ 
   "result" : "ok"
}
<%
} else {
%>
{ 
   "result" : "fail"
}
<%	
}
%>

