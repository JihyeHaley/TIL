package dao;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import vo.NewsVO;

@Repository
public class NewsDAO {
	@Autowired
	SqlSession session = null;
	
	//string객체에 hashcode메소드 있음
	public List<NewsVO> listSort(String shop_name_kor,int startNum,int endNum){
		List<NewsVO> list = new ArrayList<>();
		Map<String,Object> map = new HashMap<String,Object>();
		map.put("startNum",startNum);
		map.put("endNum", endNum);
		map.put("shop_name_kor", shop_name_kor);
		String statement = "resource.NewsMapper.newsSort";
		list = session.selectList(statement,map);
		return list;
	}
	
	public int allCount() {
		int count = 0;
		String statement = "resource.NewsMapper.newsAllCount";
		if(session.selectOne(statement)!=null) {
			count = session.selectOne(statement);
		}else {
			System.out.println("null이에유");
		}
		return count;
	}
	
	public int sortCount(String shop_name_kor) {
		int count = 0;
		String statement = "resource.NewsMapper.newsSortCount";
		if(session.selectOne(statement)!=null) {
			count = session.selectOne(statement,shop_name_kor);
		}else {
			System.out.println("null이에유");
		}
		return count;
	}
	
	public List<NewsVO> listAll(NewsVO vo,int startNum,int endNum){
		List<NewsVO> list = new ArrayList<>();
		Set<NewsVO> set = new HashSet<>(); 
		String statement = "resource.NewsMapper.newsAll";
		
		Map<String,Integer> map = new HashMap<>();
		map.put("startNum",startNum);
		map.put("endNum", endNum);
		list = session.selectList(statement,map);
		//System.out.println(list.size());
		for (int i=0; i<list.size();i++) {
			set.add(list.get(i));
		}
		//System.out.println(set.size());
		
		list = new ArrayList<>(set);
		return list;
	}
}
