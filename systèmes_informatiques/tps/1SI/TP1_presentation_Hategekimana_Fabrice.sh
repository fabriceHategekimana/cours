#!/bin/bash
changeFormat(){
	#le but de cette fonction est de changer le formatage des noms
	for ancien in *.jpg *.svg *.png
	do
		nouveau=$(echo "$ancien" | sed "s/ /_/g" | sed "s/'/_/g" | sed 's/"//g')
		if [ "$ancien" != "$nouveau" ]; then
			mv "$ancien" "$nouveau"
		fi
	done
}

resize(){
	#le but est de changer la résolution de l'image et le transformer en png
	for image in *
	do
		#on elève l'extention pour y mettre png après
		convert $image -resize $1 $image
	done
}

toPGN(){
	
	#le but est de changer la résolution de l'image et le transformer en png
	for image in *
	do
		#on elève l'extention pour y mettre png après
		nom=$(echo $image | cut -f 1 -d '.')
		convert $image $nom.png
		rm $image
	done
}


#----
#CODE
#----

#si le répertoir de départ et/ou le répertoire d'arrivé ne sont pas passés dans les arguments, alors il y a une erreur
if [ -z "$1" ]; then
	echo "error: the source directory and the destination directory don't exist"
elif [ -z "$2" ];  then
	echo "error: the destination directory doesn't exist"
fi

#si le répertoir d'arrivé n'existe pas, on le crée
if [ ! -d "$2" ]; then
	mkdir $2	
fi

#déplacement des images dans le répertoir d'arrivé
for image in $1*.jpg $1*.svg $1*.png
do
	cp "$image" $2
done

##on formate le tout
cd $2
changeFormat 

##on converti en pdf
toPGN

#On change la résolution des image si le troisième paramètre est passé
if [ ! -z "$3" ]; then
	resize $3	
fi

cd -
