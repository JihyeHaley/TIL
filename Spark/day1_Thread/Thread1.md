```java
package threadexam;

import java.text.SimpleDateFormat;
import java.util.Date;


class ThreadLab1 {
	public static void main(String[] args) throws Exception 	{
		ThreadLab1_1 t1 = new ThreadLab1_1();
		ThreadLab1_2 t2 = new ThreadLab1_2();
		t1.start();
		t2.start();
		for(int i=1; i<=10; i++) {
			System.out.println("number of milliseconds since January 1, 1970, 00:00:00 GMT");
			try {
				Thread.sleep(3000);
			} catch(Exception e ) { }
		}
		
	}
}

class ThreadLab1_1 extends Thread{
	public void run() {
		Date today = new Date();
		SimpleDateFormat month = new SimpleDateFormat("MM");
		SimpleDateFormat date = new SimpleDateFormat("dd");
		//SimpleDateFormat date = new SimpleDateFormat("yyyy/MM/dd");
		//SimpleDateFormat time = new SimpleDateFormat("hh:mm:ss a");
		//System.out.println("Time: "+time.format(today));
		for(int i=1; i<=3; i++) {
		    System.out.println("오늘은 "+month.format(today)+"월 "+ date.format(today)+"일 입니다.");
			try {
				Thread.sleep(10000);
			} catch(Exception e ) { }
		}	
	}
}



class ThreadLab1_2 extends Thread{
	public void run() {
		Date today = new Date();
		
		
		SimpleDateFormat hr = new SimpleDateFormat("hh");
		SimpleDateFormat min = new SimpleDateFormat("mm");
		SimpleDateFormat sec = new SimpleDateFormat("ss");
		//System.out.println("Time: "+time.format(today));
		for(int i=1; i<=5; i++) {
		    System.out.println(hr.format(today)+"시 "+ min.format(today)+"분 "+sec.format(today)+"초");
			try {
				Thread.sleep(5000);
			} catch(Exception e ) { }
		}		
	}
}

```

