package service;

import java.io.IOException;

import javax.servlet.http.HttpServletResponse;

import vo.MemberVO;

public interface SignupService {
    public void insertMember(MemberVO vo);
    public void idCheck(String id, HttpServletResponse response) throws IOException;
}
