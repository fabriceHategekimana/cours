#include "ultracopy.h"
#include "listing.h"

void copyFileToFile(char* sourceName, char* destinationName)
{
    char fileContent[MAX_FILE_CONTENT_SIZE] = {0};
    FILE* sourceFile = NULL;
    FILE* destinationFile = NULL;

    //On ouvre le fichier source s'il existe
    sourceFile = fopen(sourceName, "rb");
    if (sourceFile != NULL)
    {
        //On récupère le contenu du fichier
        fread(fileContent, sizeof(char), MAX_FILE_CONTENT_SIZE, sourceFile);
        fclose(sourceFile);

        //On copie le contenu vers la destination, qu'on crée si elle n'existe pas
        destinationFile = fopen(destinationName, "wb");
        if (destinationFile != NULL) 
        {
            fputs(fileContent, destinationFile);
            fclose(destinationFile);
        }
    }
    else
    {
        printf("Le fichier %s n'existe pas !!!\n", sourceName);
        exit(EXIT_FAILURE);
    }   
}

void copyFileToDirectory(char* sourceName, char* destinationName, int mode)
{
    char fileContent[MAX_FILE_CONTENT_SIZE] = {0};
    char finalDestination[STRING_LENGTH] = {0};
    FILE* sourceFile = NULL;
    FILE* destinationFile = NULL;
    
    if (mode == 1)
    {
        strcat(finalDestination, destinationName);
        strcat(finalDestination, sourceName);
    }

    //On ouvre le fichier source s'il existe
    sourceFile = fopen(sourceName, "rb");
    if (sourceFile != NULL)
    {
        //On récupère le contenu du fichier
        fread(fileContent, sizeof(char), MAX_FILE_CONTENT_SIZE, sourceFile);
        fclose(sourceFile);

        //On copie le contenu vers la destination
        if (mode == 1)
        {
            destinationFile = fopen(finalDestination, "wb");
        }
        else
        {
            destinationFile = fopen(destinationName, "wb");
        }
        
        if (destinationFile != NULL)
        {
            fputs(fileContent, destinationFile);
            fclose(destinationFile);
        }
    }
    else
    {
        printf("Le fichier %s n'existe pas !!!\n", sourceName);
        exit(EXIT_FAILURE);
    }   
}

void copyDirectoryToDirectory(char* sourceName, char* destinationName)
{
    struct stat infos;
    lstat(sourceName, &infos);
    openRecursively(&infos, sourceName, destinationName, 1);
}

void ultraCopy(int argc, char* argv[])
{
    struct stat infos;

    //On vérifie si la destination est un dossier, sinon il faut quitter le programme
    char* destination = argv[argc-1];
    DIR* d;
    d = opendir(destination);
    if (d == NULL)
    {
        printf("La destination n'est pas un dossier !!!\n");
        exit(EXIT_FAILURE);
    }
    closedir(d);

    //On récupère chaque fichier/dossier et on le copie vers la destination
    for (int i = 1; i < (argc-1); i++)
    {
        if (lstat(argv[i], &infos) < 0)
        {
            fprintf(stderr, "Cannot stat %s\n", argv[i]);
        }
        //L'inode existe
        else
        {
            if (S_ISREG(infos.st_mode)) 
            { 
                copyFileToDirectory(argv[i], destination, 1); 
            }
            else if (S_ISDIR(infos.st_mode)) 
            {
                copyDirectoryToDirectory(argv[i], destination); 
            }
            else 
            { 
                printf("Type de fichier non géré par ce programme !!!\n"); 
            }   
        }
    }

}