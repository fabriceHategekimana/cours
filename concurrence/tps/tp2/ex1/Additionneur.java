public class Additionneur extends Thread{

	public Additionneur(String name, int time, int x){
		this.name= name;
		this.time= time;
		this.x= x;
	}	

	public void run(){
			System.out.println("Thread "+name+" lit x= "+x);
		try{ 
			sleep(time);
		}
		catch(InterruptedException e){ 
			System.out.println(e);	
		}
			System.out.println("Thread "+name+" incrémentation de x");
		try{ 
			sleep(time);
		}
		catch(InterruptedException e){ 
			System.out.println(e);	
		}
			x=x+1;
			System.out.println("Thread "+name+" maintenant x vaut: "+x);
	}
	private String name;
	private int time;
	private static int x;
}
