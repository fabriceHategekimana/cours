#Variables personnelles
nom="nom"
prenom="prenom"
mail="mail"

if [ -z "$1" ]; then
	echo il manque le nom du fichier
else
	#Création du Makefile
	touch Makefile
	echo "all:pdf
	
pdf: FORCE
	pandoc imagerie_numerique.md $1.md  imagerie_numerique.yaml -o $1.pdf
	
FORCE:
	" >> Makefile
	
	#Création du template première page
	touch imagerie_numerique.md
	echo "
Back newcommandBack TPid{1}
Back newcommandBack TPname{$1}
Back newcommandBack Firstname{$prenom}
Back newcommandBack Familyname{$nom}
Back newcommandBack Email{$mail}

Back begin{titlepage}
Back newcommand{Back HRule}{Back rule{Back linewidth}{0.5mm}} 
Back center 
Back textsc{Back LARGE Université de Genève}Back Back [1cm]
Back textsc{Back Large Imagerie Numérique}Back Back [0.2cm]
Back textsc{Back large 13X004}Back Back [1cm] 								Back HRule Back Back [0.8cm]
{ Back huge Back bfseries TP Back TPid : Back TPname}Back Back [0.7cm]
Back HRule Back Back [2cm]
Back large
Back emph{Author:} Back Firstname Back ; Back FamilynameBack Back [0.5cm]		
Back emph{E-mail:} {Back color{blue}Back Email}Back Back [7cm]		
{Back large Back today}Back Back [2cm]
Back vfill 
Back end{titlepage}
" > imagerie_numerique.md

	#création du fichier yaml
	touch imagerie_numerique.yaml
	echo "
---
header-includes: 
  Back usepackage[english]{babel}
  Back usepackage[T1]{fontenc}
  Back usepackage[a4paper,top=3cm,bottom=2cm,left=2cm,right=2cm,marginparwidth=1.75cm]{geometry}
  Back usepackage{amsmath}
  Back usepackage{graphicx}
  Back usepackage[colorinlistoftodos]{todonotes}
  Back usepackage[justification=centering]{caption}
  Back usepackage{subcaption}
  Back usepackage{sectsty}
  Back usepackage{float}
  Back usepackage{titling} 
  Back usepackage{blindtext}
  Back usepackage[square,sort,comma,numbers]{natbib}
  Back usepackage[colorinlistoftodos]{todonotes}
  Back usepackage{xcolor}
  Back usepackage{fancyhdr}
  Back usepackage{lipsum}
  Back definecolor{darkgreen}{rgb}{0.0, 0.4, 0.0}
  Back pagestyle{fancy}
  Back fancyhf{}
  Back lhead{Back Firstname Back ; Back Familyname}
  Back rfoot{Page Back thepage}
---
	" > imagerie_numerique.yaml
	
	#on arrange les backslash (qui sont vraiment mal pris en charge sur bash)
	back='\'
	sed -i -e "s/Back /$back$back/g" imagerie_numerique.md
	sed -i -e "s/Back /$back$back/g" imagerie_numerique.yaml

	#Création de la page principale
	touch $1.md
fi
