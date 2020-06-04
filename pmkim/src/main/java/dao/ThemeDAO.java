package dao;

import java.util.ArrayList;
import java.util.List;

import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import vo.GoodsInfoThemeVO;

@Repository
public class ThemeDAO {

	@Autowired
	SqlSession session = null;

	public List<GoodsInfoThemeVO>  allGoods(GoodsInfoThemeVO vo) {
		List<GoodsInfoThemeVO> li = new ArrayList<GoodsInfoThemeVO>();
		String statement = "resource.ThemeMapper.allGoodsTheme";
		li = session.selectList(statement,vo);
		//list 값 잘 넘어오는지 확인
		//System.out.println(li.get(0).toString());
		return li;
	}

}
