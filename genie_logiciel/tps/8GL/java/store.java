
public class Store { 

	volatile private static store store;

	private username= "username";
	private password= "password";
	private role= "role";

	private Store(){ 
					
	}

	public void PostObjet(){

	}

	public void FileDactualite(){

	}

	public Objet message(){

	}

	public static Store getInstance(){ 
		if( Store == null){
			synchronized (Store.class){ 
				if(store == null){
					store = new Store();
				}	
			}
		}	
		return store;
	}

}
