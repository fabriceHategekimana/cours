public class tp2 {
	public static void main(String[] args){
		System.out.println("Start");
		int x = 0;
		int y = 0;
		Additionneur a1= new Additionneur("1", 2000, x);
		Additionneur a2= new Additionneur("2", 1000, x);

		a1.start();
		a2.start();
	}	
}
