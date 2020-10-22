#ifndef DEF_LISTING

#define DEF_LISTING

#include <unistd.h>
#include <stdlib.h>
#include <time.h>
#include <stdio.h>
#include <string.h>
#include <sys/stat.h>
#include <dirent.h>

#define TIME_INFO_SIZE 256
#define STRING_LENGTH 1024

void listFiles(char* argv);
void getFileInfo(struct stat* infos, char* fileName);
void getDateAndTimeInfo(struct stat* infos);
void openRecursively(struct stat* infos, char *basePath, char* destinationPath, int mode);

#endif