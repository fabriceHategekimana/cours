Pseudo code
===========
```
//Pour linklayer
Objet linkLayer(){
	send(trame){
		trame= manageSend(trame)
		hardware.send(trame)
	}
	receive(trame){
		trame= manageRecieve(trame)
		reseaux.recieve(trame)	
	}
}
	
//Pour hardware
Objet hardware(){
	send(trame){
		trame= hardware.manageSend(trame)
		send(trame)
	}

	recieve(trame){ 
		trame hardware.manageRecieve(trame)
	}
}

//Pour réseaux
Objet reseaux(){
	send(trame){
		trame= hardware.manageSend(trame)
		send(trame)
	}
	recieve(trame){
		trame= reseaux.manageRecieve(trame)
	}
}
	
//temporisateur
Objet Temporisateur{
	start(time){ 
		Timeout= false	
		sleep(1000*time)	
		Timeout= true
	}
}
	
//Code principal
//Émetteur
Objet Emetteur{ 
	temporisateur
	hardware
	reseaux
	trame1
	trame2

	start(trame){ 
		reseaux.send(trame1)	
		temporisateur.start(time)
		while(!temporisateur.Timeout){ 
			if(trame2 != null){ 
				hardware.recieve(trame2)
				trame2= null
				break;
			}
		}
		if(temporisateur.Timeout){ 
			start(trame)
		}
	}
}

//Receveur
Objet Receveur{
	hardware
	reseaux
	trame1
	trame2
	
	start(){
		while(trame == null){ 
			
		}
		if (trame != null){ 
			hardware.recieve(trame2)	
			//s'il y a une erreur, elle est transmise à la trame 1 comme non acquittement
			if(hardware.Err){ 
				reseaux.send(trame1)
			}
		}
		start()
	}
}
```



