public interface Objet{
	private String Nom;
	private String Proprietaire;
	private int Prix;
	private String Description;
	private String Labels;

	public Objet(String Nom, String Proprietaire, int Prix, String Description, String Labels){
		this.Nom= Nom;	
		this.Proprietaire= Proprietaire;	
		this.Prix= Prix;	
		this.Description= Description;	
		this.Labels= Labels;	
	}	

	public void getPrix(){
		return this.Prix;
	}
	public void setPrix(int prix){
		this.Prix= prix;
	}

	public void getNom(){
		return this.Nom;
	}
	public void setNom(String nom){
		this.Nom= nom;
	}

	public void getProprietaire(){
		return this.Proprietaire;
	}
	public void setProprietaire(String proprietaire){
		this.Proprietaire= proprietaire;
	}

	public void getDescription(){
		return this.Description;
	}
	public void setDescription(String description){
		this.Description= description;
	}

	public void getLabels(){
		return this.Labels;

	}
	public void setLabels(String labels){
		this.Labels= labels;
	}
}
