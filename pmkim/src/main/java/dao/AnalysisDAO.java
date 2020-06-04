package dao;

import java.util.ArrayList;
import java.util.List;

import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import vo.AnalysisVO;

@Repository
public class AnalysisDAO {

	@Autowired
	SqlSession session = null;

	public List<AnalysisVO>  allGoods(AnalysisVO vo) {
		List<AnalysisVO> li = new ArrayList<AnalysisVO>();
		String statement = "resource.AnalysisMapper.allGoodsAnalysis";
		li = session.selectList(statement,vo);
		return li;
	}

	public List<AnalysisVO>  allGoods2(AnalysisVO vo) {
		List<AnalysisVO> li = new ArrayList<AnalysisVO>();
		String statement = "resource.AnalysisMapper.allGoods";
		li = session.selectList(statement,vo);
		return li;
	}
}
