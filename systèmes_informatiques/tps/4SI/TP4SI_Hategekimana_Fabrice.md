
## 5 Questions
• Que se passera-t-il si nous déverrouillons un fichier (ou une partie du fichier) qui n’est pas verrouillé?  
- De ce que j'ai observé, il ne se passe rien.  

• Que se passera-t-il si nous mettons un nouveau verrou sur une section déjà verrouillée?  
- L'opération va échouer.  
 
Le type de verrou changera-t-il le résultat? Expliquer dans la situation avec le même processus et avec 2 processus différents  
- Si on a le même processus, le type de verrou ne changera rien.  
- Dans le cas de processus différent, le second processus ne pourra pas lire dans le premier.  

