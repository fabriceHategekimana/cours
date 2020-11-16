
public class ETU_store {
	public static void main(String[] args){
		Store client= new Store("Nom", "mot_de_passe");
		AbstractFactory filtre= FilDActualiteFactory.getFactory("Faculté", client);
		ArrayList<Objet> monFilDActualite= filtre.getFilDActualite();
	}	
}
