package dao;

import vo.MemberVO;

public interface SignupDAO {
    public void insertMember(MemberVO vo);
    public int idCheck(String id);
}
