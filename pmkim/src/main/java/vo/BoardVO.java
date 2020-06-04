package vo;

import java.util.Date;

public class BoardVO {

    // 게시 아이디 
    private Integer write_id;

    // 아이디 
    private String id;

    // 날짜 
    private Date date;

    // 제목 
    private String title;

    // 수 
    private Integer cnt;

    // 내용 
    private String content;

	public Integer getWrite_id() {
		return write_id;
	}

	public void setWrite_id(Integer write_id) {
		this.write_id = write_id;
	}

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public Date getDate() {
		return date;
	}

	public void setDate(Date date) {
		this.date = date;
	}

	public String getTitle() {
		return title;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	public Integer getCnt() {
		return cnt;
	}

	public void setCnt(Integer cnt) {
		this.cnt = cnt;
	}

	public String getContent() {
		return content;
	}

	public void setContent(String content) {
		this.content = content;
	}

	@Override
	public String toString() {
		return "BoardVO [write_id=" + write_id + ", id=" + id + ", date=" + date + ", title=" + title + ", cnt=" + cnt
				+ ", content=" + content + "]";
	}
	
}
