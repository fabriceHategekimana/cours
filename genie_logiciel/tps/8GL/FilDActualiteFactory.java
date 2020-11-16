//C'est lui le FactoryProvider
public class FilDActualiteFactory{
	public FilDActualiteFactory(){
		
	}	

	public static AbstractFactory getFactory(String choice, Store client){
		switch(choice){ 
			case "Faculté":
				return new FilDActualiteFaculte();
				break;
			case "TypeObjet":
				return new FilDActualiteTypeObjet();
				break;
			default:
				return new FilDActualiteFaculte();
				break;
		}
	}
}
