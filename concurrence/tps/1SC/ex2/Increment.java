public class Increment extends Thread{
	private Compteur compteur;
	private String str;
	public Increment(String str, int x){
		this.str= str;
		this.compteur= new Compteur(x);
	}	
	public void run(){
		while(true){
			compteur.incremente();
			int val = compteur.getValue();
			try{
				sleep(1000);
			}
			catch(InterruptedException e){
				System.out.println("Erreur");
			}
			System.out.println("processus "+str+": "+Integer.toString(val));
		}
	}
}
