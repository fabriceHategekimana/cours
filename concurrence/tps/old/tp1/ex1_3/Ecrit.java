public class Ecrit extends Thread{

	public Ecrit(String texts, int nb, int time){
		this.texte= texts;
		this.nb= nb;
		this.time= time;
	}	

	public void run(){
		for(int i= 0; i<nb; i++){ 
			print(texte);	
			try{
				sleep(time);
			}
			catch(InterruptedException e){ 
				System.out.println("Erreur");
			}
		}
	}

	public void print(String txt){
		String[] parts= txt.split("");
		int l= parts.length;
		int i= 0;
		while(i<l){
			System.out.print(parts[i]);
			i++;
		}
	}
	private String texte;
	private int nb;
	private int time;
}

