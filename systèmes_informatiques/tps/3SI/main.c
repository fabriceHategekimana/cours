#include "listing.h"
#include "ultracopy.h"

int main(int argc, char* argv[])
{
    struct stat sourceInfo;
    struct stat destinationInfo;
    //S'il y a moins de 2 arguments il faut quitter le programme
    if(argc < 2)
    {
        printf("Aucun argument n'a été spécifié\n");
        exit(EXIT_FAILURE);
    }

    //Un seul argument
    if (argc == 2)
    {
        char* argument = argv[1];
        listFiles(argument);
    }

    //Deux fichiers en arguments
    if(argc == 3)
    {
        char* sourceFile = argv[1];
        char* destinationFile = argv[2];
        FILE* file;
        DIR* dir;

        if (lstat(sourceFile, &sourceInfo) < 0)
        {
            fprintf(stderr, "Cannot stat %s\n", sourceFile);
        }
        else
        {
            dir = opendir(destinationFile);
            //Cas 1: Fichier vers fichier
            if (S_ISREG(sourceInfo.st_mode) && dir == NULL)
            {
                //On crée le fichier s'il n'existe pas
                file = fopen(destinationFile, "rb");
                if (file == NULL)
                {
                    file = fopen(destinationFile, "wb");
                    fclose(file);
                }
                copyFileToFile(sourceFile, destinationFile);
            }

            //Cas 2 : Fichier vers répertoire
            else if (S_ISREG(sourceInfo.st_mode) && dir != NULL)
            {
                strcat(destinationFile, sourceFile);
                openRecursively(&sourceInfo, sourceFile, destinationFile, 1);
            }
            //Cas 3 : Répertoire vers répertoire
            else if (S_ISDIR(sourceInfo.st_mode) && dir != NULL)
            {
                copyDirectoryToDirectory(sourceFile, destinationFile);
            }
            //Autre
            else
            {
                closedir(dir);
                printf("Erreur !!!\n");
                exit(EXIT_FAILURE);
            }
            closedir(dir);
        }
    }

    //Au moins 3 arguments
    if (argc > 3)
    {
        ultraCopy(argc, argv);
    }
    return 0;
}
