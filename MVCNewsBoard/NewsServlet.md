~~~java
package controller;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import model.dao.NewsDAO;
import model.vo.NewsVO;

@WebServlet("/news")
public class NewsServlet extends HttpServlet {

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String action = request.getParameter("action");
		String newsid = request.getParameter("newsid");
		NewsDAO dao = new NewsDAO();
		
		if(action == null & newsid == null) {
			request.setAttribute("listAll", dao.listAll());
		}else if(action.equals("read") && newsid != null) {
			request.setAttribute("listOne", dao.listOne(Integer.parseInt(newsid)));
			request.setAttribute("listAll", dao.listAll());
		}else if(action.equals("delete") && newsid != null) {
			if(dao.delete(Integer.parseInt(newsid))){
				request.setAttribute("msg", "No." + newsid + " succeed to delete");
			}else {
				request.setAttribute("msg", "No." + newsid + " fail to delete");
			}
			request.setAttribute("listAll", dao.listAll());
			
		}
			request.getRequestDispatcher("/jspexam/news.jsp").forward(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		String action = request.getParameter("action");
		String newsid = request.getParameter("newsid");

		String writer = request.getParameter("writer");
		String title = request.getParameter("title");
		String content = request.getParameter("content");
		String cnt = request.getParameter("cnt");
		
		NewsDAO dao = new NewsDAO();
		NewsVO vo = new NewsVO();
		
		if(action!=null && action.equals("insert")) {
			vo.setWriter(writer);
			vo.setTitle(title);
			vo.setContent(content);
			vo.setCnt(0);
			if(dao.insert(vo)) {
				request.setAttribute("msg", "It has been succefully updated.");
			}else {
				request.setAttribute("msg", "It does not work for updating News");
			}
		} else if(newsid != null && action!=null && action.equals("update")) {
			vo.setId(Integer.parseInt(newsid));
			vo.setWriter(writer);
			vo.setTitle(title);	
			vo.setContent(content);
			vo.setCnt(vo.getCnt());
			if (dao.update(vo)) {
				request.setAttribute("msg", "It has been successfully updated.");
			} else {
				request.setAttribute("msg", "It has not been updated.");
			}
		} else {
			request.setAttribute("msg", "Query Error");
			
			System.out.println(action);
			System.out.println(newsid);
			System.out.println(writer);
			System.out.println(title);
			System.out.println(content);
			System.out.println(cnt);
			
		}
		request.setAttribute("listAll", dao.listAll());
		request.getRequestDispatcher("/jspexam/news.jsp").forward(request, response);
	}

}
~~~

