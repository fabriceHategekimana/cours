public class ex2 {
	public static void main(String[] args){
		int x= 0;
		Increment i1= new Increment("i1", x);
		Increment i2= new Increment("i2", x);

		i1.start();
		i2.start();
	}	
}
