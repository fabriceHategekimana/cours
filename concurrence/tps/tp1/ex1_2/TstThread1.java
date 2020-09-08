public class TstThread1 {
	public static void main(String[] args){
		Ecrit e1= new Ecrit("bonjour", 10, 1000);
		Ecrit e2= new Ecrit("bonsoir", 12, 2000);
		Ecrit e3= new Ecrit("\n", 5, 3000);

		e1.start();
		e2.start();
		e3.start();
	}	
}
