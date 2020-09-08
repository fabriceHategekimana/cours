public class Attempt1 implements Lock{
	private boolean openDoor= true;
	public void requestCS(int i){
		while(!openDoor); //attente active
		openDoor= false;
	}

	public void releaseCS(int i){
		openDoor= true; //libère l'accès à la SC
	}
	public Attempt1(){
	
}	
}
