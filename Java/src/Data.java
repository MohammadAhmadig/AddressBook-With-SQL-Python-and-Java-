import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;




public class Data
{
	public static Connection connection;
	static Statement statement;
    public static void main (String[] args) throws InstantiationException, IllegalAccessException, ClassNotFoundException, SQLException
    {
		GetConnection();
		CreateTable();
    	new Gui().setVisible(true);
    }
public static void GetConnection() throws InstantiationException, IllegalAccessException, ClassNotFoundException, SQLException{
	 
		
		String url = "jdbc:mysql://localhost:3306/pauldb";
    	String userName = "paul";
    	String password = "mypass";
    	Class.forName ("com.mysql.jdbc.Driver").newInstance ();
        connection = DriverManager.getConnection (url, userName, password);
        System.out.println ("Database connection established");
        statement = connection.createStatement();
	}
	public static void CreateTable() throws SQLException{//sex ra string kon
		try
		{
			statement.executeUpdate ("create table AddressBook1(name VARCHAR(20), address VARCHAR(50),phone VARCHAR(30))");
		}
		catch (Exception e) {
			// TODO: handle exception
			System.out.println("twice call create");
		}
	}
	
	public static void Add(Person person) throws SQLException{
		String sql="Insert into AddressBook1(name,address,phone) values(?,?,?)";
		PreparedStatement ps=connection.prepareStatement(sql);
		ps.setString(1 , person.getName());
		ps.setString(2 , person.getAddress());
		ps.setString(3 , person.getPhone());
		ps.executeUpdate();
		
	}
	public static ArrayList<Person> Search(String name) throws SQLException{
		ArrayList<Person> persons = new ArrayList<Person>();
		Person person = new Person();
		String sql="Select * from Addressbook1 where name like '%"+name+"%'";
		Statement statement=connection.createStatement();
		ResultSet rs=statement.executeQuery(sql);
		for(;rs.next();){
			person.setName(rs.getString("name"));
			person.setAddress((rs.getString("address")));
			person.setPhone(rs.getString("phone"));
			persons.add(person);
		}
		return persons;
	}
	public static boolean Delete(String name) throws SQLException{
		int temp=0;
		String sql="Select * from AddressBook1";
		ResultSet rs=statement.executeQuery(sql);
		for(;rs.next();){
			if(rs.getString("name").equals(name))
				temp=1;
		}
		try {
			String sql1="Delete from AddressBook1 where name like '%"+name+"%'";
			statement=connection.createStatement();
			statement.executeUpdate(sql1);
			
		} catch (Exception e) {
			// TODO: handle exception
			
		}
		
		if(temp==1)
			return true;
		return false;
	}
	
	public static boolean Edit(Person person) throws SQLException{
		int temp=0;
		String sql="Select * from AddressBook1";
		ResultSet rs=statement.executeQuery(sql);
		for(;rs.next();){
			if(rs.getString("name").equals(person.getName()))
				temp=1;
		}
		try {
			String sql1="Update AddressBook1 set address=? ,phone=? where name=? ";
			PreparedStatement ps=connection.prepareStatement(sql1);
			ps.setString(1 , person.getAddress());
			ps.setString(2 , person.getPhone());
			ps.setString(3 , person.getName());
			ps.executeUpdate();
		} catch (Exception e) {
			// TODO: handle exception
		}
		if(temp==1)
			return true;
		return false;
	}
}
