```java
package jdbcsrc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class SelectEmpLab{
    public static void main(String[] args){
        try{
            Class.forName("oracle.jdbc.OracleDriver");
        }
        catch (ClassNotFoundException e){
            e.printStackTrace();
        }
        String sql = null;
        
        boolean flag =(int)(Math.random()*2)==1? true : false;
        
        if(flag)
            sql = "SELECT ENAME, TO_CHAR(SAL, '999,999')||'원' SAL FROM EMP";
        
        else
            sql = "SELECT ENAME, TO_CHAR(HIREDATE, 'YYYY\"년\" MM\"')"
    }
}
```

