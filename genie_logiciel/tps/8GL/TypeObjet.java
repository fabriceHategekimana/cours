import java.util.Date;

public class TypeObjet implements FilDActualite{
	String type= "TypeObjet";
	Date date;
	ArrayList<Objet> listeDObjet;	

	public TypeObjet(){
		date= new Date();
	}	
	
	public String getType(){ 
		return this.type;	
	}
	public String getDate(){ 
		return this.date.toString();
	}
	public Object getFirst(){ 
		if(this.listeDObjet.size() > 0){
			return listeDObjet.get(0);
		}		
	}
	public ArreyList<Objet> getFirstElements(int nb){
		if(this.listeDObjet.size() > nb){
			return this.listeDObjet.subList(0, nb);
		}	
	}
	public void update(String typeDObjet){ 
			
	}
}
