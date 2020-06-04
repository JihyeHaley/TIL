package service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import dao.CartDAO;

@Service
public class PagingService {
	
	@Autowired
	CartDAO dao;
	
	public int lineCnt = 9; 	// 한 화면에 구성하는 글 개수
	public int pageCnt = 5;  	// 한 화면의 페이지 개수
	//public int postCnt; 	// 요구 사항을 만족하는 글의 전체 개수
	public int pgNum; 	        // 현재 페이지 넘버
	
	public int getPageCount(String event_name, String shop_code) {	// 글의 개수에 따른 페이지 개수 계산
		int postCnt = dao.listCount(event_name,shop_code);
		//System.out.println("postCnt : "+postCnt);
		return ((postCnt-1)/lineCnt)+1;		
	}
	public int getPageCount(String keyword) {	// 글의 개수에 따른 페이지 개수 계산
		int postCnt = dao.listCount2(keyword);
		//System.out.println("postCnt : "+postCnt);
		return ((postCnt-1)/lineCnt)+1;		
	}
	public int getPageStart(int pgNum) {	// 각 화면별 시작 페이지 번호
		this.pgNum = pgNum;
		return ((pgNum-1)/pageCnt)*pageCnt+1;
	}
	public int getPageEnd(int pgNum,String event_name, String shop_code) {	//각 화면별 종료 페이지 번호
		this.pgNum = pgNum;
		int result1 = getPageStart(pgNum)+pageCnt-1;
		int result2 = getPageCount(event_name,shop_code);
		if(result1>result2)
			return result2;
		else
			return result1;
	}
	public int getPageEnd(int pgNum,String keyword) {	//각 화면별 종료 페이지 번호
		this.pgNum = pgNum;
		int result1 = getPageStart(pgNum)+pageCnt-1;
		int result2 = getPageCount(keyword);
		if(result1>result2)
			return result2;
		else
			return result1;
	}
	public boolean isPreData(int pgNum) {	//이전 페이지들을 출력하는 left 이미지 출력 여부 결정
		this.pgNum = pgNum;
		boolean result = false;
		if(getPageStart(pgNum)!=1)
			result = true;
		return result;
	}
	public boolean isNextData(int pgNum,String event_name, String shop_code) {	//이전 페이지들을 출력하는 right 이미지 출력 여부 결정
		boolean result = false;
		this.pgNum = pgNum;
		if(getPageEnd(pgNum,event_name,shop_code) < getPageCount(event_name,shop_code))
			result = true;
		return result;
	}
	public boolean isNextData(int pgNum,String keyword) {	//이전 페이지들을 출력하는 right 이미지 출력 여부 결정
		boolean result = false;
		this.pgNum = pgNum;
		if(getPageEnd(pgNum,keyword) < getPageCount(keyword))
			result = true;
		return result;
	}
	public int getWritingStart(int pgNum) {	//현재 페이지 넘버에 따라 DB 서버에서 가져올 글의 시작 행 넘버
		this.pgNum = pgNum;
		return getWritingEnd(pgNum)-lineCnt+1;
	}
	public int getWritingEnd(int pgNum) {	//현재 페이지 넘버에 따라 DB 서버에서 가져올 글의 종료 행 넘버
		this.pgNum = pgNum;
		return pgNum*lineCnt;
	}
}