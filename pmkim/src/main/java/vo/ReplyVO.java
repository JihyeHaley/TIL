package vo;

import java.util.Date;

public class ReplyVO {

    // 댓글 아이디 
    private Integer reply_id;

    // 게시 아이디 
    private Integer write_id;

    // 내용 
    private String content;

    // 아이디 
    private String id;

    // 날짜 
    private Date write_date;

	public Integer getReply_id() {
		return reply_id;
	}

	public void setReply_id(Integer reply_id) {
		this.reply_id = reply_id;
	}

	public Integer getWrite_id() {
		return write_id;
	}

	public void setWrite_id(Integer write_id) {
		this.write_id = write_id;
	}

	public String getContent() {
		return content;
	}

	public void setContent(String content) {
		this.content = content;
	}

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public Date getWrite_date() {
		return write_date;
	}

	public void setWrite_date(Date write_date) {
		this.write_date = write_date;
	}

	@Override
	public String toString() {
		return "ReplyVO [reply_id=" + reply_id + ", write_id=" + write_id + ", content=" + content + ", id=" + id
				+ ", write_date=" + write_date + "]";
	}

    
}
