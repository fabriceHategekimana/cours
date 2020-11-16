public interface FilDActualite{
	String getType();
	String getDate();
	Object getFirst();
	ArreyList<Objet> getFirstElements();
	void update();
}
