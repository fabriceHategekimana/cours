public class Additionneur implements Runnable{
	private String name;
	private int time;
	private static int x;

	public Additionneur(String name, int time, int x){
		this.name= name;
		this.time= time;
		this.x= x;
	}	

	@Override
	public void run(){
		try{ 
			System.out.println("Thread "+name+" lit x= "+x);
			Thread.sleep(time);
			System.out.println("Thread "+name+" incrémentation de x");
			x=x+1;
			Thread.sleep(time);
			System.out.println("Thread "+name+" x vaut maintenant: "+x);
		}
		catch(InterruptedException e){ 
			System.out.println(e);	
		}
	}
}
