import java.sql.*;
public class database{
	private Connection con;
	public database(){
		 con = null;
		 //tentative d'ouverture de la base de donnée ETU
		 try{
		     Class.forName("oracle.jdbc.driver.OracleDriver");
		     String dbURL = "jdbc:oracle:thin:@(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=ETU)(PORT=1521))(CONNECT_DATA=(SERVER = DEDICATED)(SERVICE_NAME=orclgg)))";
		     System.out.println("jdbcurl=" + dbURL);
		     String strUserID = "system";
		     String strPassword = "Oracle123";
		     con=DriverManager.getConnection(dbURL,strUserID,strPassword);
		 }catch(Exception e){ System.out.println(e);}
		 finally {
		     con.close();
		 }
	}	

	protected void finalize throws Throwable(){ 
             con.close();
	}

	public void getObjects(query){
	     //Faire une requête
             Statement stmt=con.createStatement();
             ResultSet rs=stmt.executeQuery(query);
	     ArrayList<String> objets = new ArrayList<string>( );
             while(rs.next())
		 objets.add(rs.getString());
	     return objets;
	}
}
