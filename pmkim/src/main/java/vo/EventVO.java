package vo;

public class EventVO {

    // 상품 아이디 
    private String good_id;

    // 행사 명 
    private String event_name;

    // 행사 아이디 
    private int event_id;

	public String getGood_id() {
		return good_id;
	}

	public void setGood_id(String good_id) {
		this.good_id = good_id;
	}

	public String getEvent_name() {
		return event_name;
	}

	public void setEvent_name(String event_name) {
		this.event_name = event_name;
	}

	public int getEvent_id() {
		return event_id;
	}

	public void setEvent_id(int event_id) {
		this.event_id = event_id;
	}

	@Override
	public String toString() {
		return "EventVO [good_id=" + good_id + ", event_name=" + event_name + ", event_id=" + event_id + "]";
	}
    
    

}