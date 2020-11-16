public class FactoryProvider implements AbstractFactory{
	public FilDActualite getFilDActualite(){ 
		return new TypeObjet();
	}
}
