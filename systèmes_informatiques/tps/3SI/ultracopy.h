#ifndef DEF_ULTRACOPY
#define DEF_ULTRACOPY

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <dirent.h>
#include <sys/stat.h>
#define MAX_FILE_CONTENT_SIZE 65536

void copyFileToFile(char* sourceName, char* destinationName);
void copyFileToDirectory(char* sourceName, char* destinationName, int mode);
void copyDirectoryToDirectory(char* sourceName, char* destinationName);
void copyRecursively(struct stat* infos, char *basePath, char* destinationPath);
void ultraCopy(int argc, char* argv[]);

#endif