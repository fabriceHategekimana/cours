import java.lang.Math;

public class Ecrit extends Thread{
	public Ecrit(String texts, int nb){
		this.texte= texts;
		this.nb= nb;
	}	
	public void run(){
		for(int i= 0; i<nb; i++){
			System.out.println(texte);
			int r= (int) Math.round(Math.random()*5);
			try{
				sleep(1000*r);
			}
			catch(InterruptedException e){
				System.out.println("Erreur");
			}
		}
	}
	public String getTexte(){
		return texte;
	}
	public int getNb(){
		return this.nb;
	}
	private String texte;
	private int nb;
}
