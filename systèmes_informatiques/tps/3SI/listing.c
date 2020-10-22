#include "listing.h"
#include "ultracopy.h"

void openRecursively(struct stat* infos, char* basePath, char* destinationPath, int mode)
{
    char path[STRING_LENGTH] = {0};
    char directoryPath[STRING_LENGTH] = {0};
    char filePath[STRING_LENGTH] = {0};
    struct stat next;

    //Fichier
    if (S_ISREG(infos->st_mode))
    {
        //Lister les fichiers
        if (mode == 0)
        {
            printf("-");
            getFileInfo(infos, basePath);
        }

        //Copier les fichiers
        if (mode == 1)
        {
            //On copie le fichier vers la destination spécifiée
            strcat(filePath, destinationPath);
            strcat(filePath, basePath);
            copyFileToDirectory(basePath, filePath, 0);
        }
    }
    //Répertoire
    else if (S_ISDIR(infos->st_mode))
    {
        //Lister les fichiers
        if (mode == 0)
        {
            printf("d");
            getFileInfo(infos, basePath);
        }

        //Copier les fichiers
        if (mode == 1)
        {
            //On créé un le dossier dans la destination
            strcat(directoryPath, destinationPath);
            strcat(directoryPath, basePath);
            int status = mkdir(directoryPath, S_IRWXU | S_IRWXG | S_IROTH | S_IXOTH);
        }
        strcpy(path, basePath);
        struct dirent* d;
        DIR* dir = opendir(basePath);

        //On lit tous les fichiers du répertoire
        while ((d = readdir(dir)) != NULL)
        {

            if(strcmp(d->d_name, ".") && strcmp(d->d_name, ".."))
            {
                //On met à jour les chemins vers les fichiers
                strcpy(path, basePath);
                strcat(path, d->d_name);
                
                if (lstat(path, &next) < 0)
                {
                    fprintf(stderr, "Cannot stat %s\n", path);
                }
                //L'inode existe
                else
                {
                    if (S_ISDIR(next.st_mode)) { strcat(path, "/"); }
                    //Lister les fichiers
                    if (mode == 0)
                    {
                        openRecursively(&next, path, NULL, 0);
                    }

                    //Copier les fichiers
                    if (mode == 1)
                    {
                        openRecursively(&next, path, destinationPath, 1);
                    }
                }
            }
        }
        closedir(dir);
    }
    //Lien symbolique
    else if (S_ISLNK(infos->st_mode))
    {
        printf("l");
        getFileInfo(infos, basePath);
    }
    //Autre chose
    else
    {
        printf("Type de fichier non géré par ce programme\n");
    }
}

void getDateAndTimeInfo(struct stat* infos)
{
    char dateAndTimeInfo[TIME_INFO_SIZE];
    time_t t;
    struct tm *tmp;

    t = time(NULL);
    tmp = localtime(&(infos->st_ctime));
    if (tmp == NULL)
    {
        perror("localtime");
        exit(EXIT_FAILURE);
    }

    if (strftime(dateAndTimeInfo, TIME_INFO_SIZE, "%a  %b  %d  %X  %Y", tmp) == 0) 
    {
        fprintf(stderr, "strftime returned 0");
        exit(EXIT_FAILURE);
    }
    printf("%s", dateAndTimeInfo);
}

void getFileInfo(struct stat* infos, char* fileName)
{
    //Utilisateur
    if (infos->st_mode & S_IRUSR) { printf("r"); }
    else { printf("-"); }

    if (infos->st_mode & S_IWUSR) { printf("w"); }
    else { printf("-"); }

    if (infos->st_mode & S_IXUSR) { printf("x"); }
    else { printf("-"); }

    //Groupes
    if (infos->st_mode & S_IRGRP) { printf("r"); }
    else { printf("-"); }

    if (infos->st_mode & S_IWGRP) { printf("w"); }
    else { printf("-"); }

    if (infos->st_mode & S_IXGRP) { printf("x"); }
    else { printf("-"); }

    //Autres
    if (infos->st_mode & S_IROTH) { printf("r"); }
    else { printf("-"); }

    if (infos->st_mode & S_IWOTH) { printf("w"); }
    else { printf("-"); }

    if (infos->st_mode & S_IXOTH) { printf("x"); }
    else { printf("-"); }
    
    printf("%10ld", infos->st_size);
    printf("\t");
    getDateAndTimeInfo(infos);
    printf("\t");
    printf("%s\n", fileName);
}

void listFiles(char* argv)
{
    struct stat infos;

    if (lstat(argv, &infos) < 0)
    {
        fprintf(stderr, "Cannot stat %s\n", argv);
    }
    //L'inode existe
    else
    {
        openRecursively(&infos, argv, NULL, 0);
    }
}