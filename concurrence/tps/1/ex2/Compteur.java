public class Compteur{
	private static int x;
	public Compteur(int x){
		this.x= x;	
	}	
	public void incremente(){
		x++;
	}
	public int getValue(){
		return x;
	}
}
