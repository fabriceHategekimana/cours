
public class Singleton { 

	volatile private static singleton singleton;

	private Singleton(){ 
	
	}

	public static Singleton getInstance(){ 
		if( Singleton == null){
			synchronized (Singleton.class){ 
				if(singleton == null){
					singleton = new Singleton();
				}	
			}
		}	
		return singleton;
	}

}
