public class Ecrit extends Thread{
	public Ecrit(String texts, int nb, int time){
		this.texte= texts;
		this.nb= nb;
		this.time= time;
	}	
	public void run(){
		for(int i= 0; i<nb; i++){ 
			System.out.println(texte);	
			try{
				sleep(time);
			}
			catch(InterruptedException e){ 
				System.out.println("Erreur");
			}
		}
	}
	private String texte;
	private int nb;
	private int time;
}
