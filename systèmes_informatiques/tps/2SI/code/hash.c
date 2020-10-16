#include<stdlib.h>
#include<stdio.h>
#include <stdio.h>
#include <string.h>
#include <openssl/evp.h>
#include "hash.h"

//utiliser -lssl et -lcrypto
int hashage(char *message, char *digestName){
    EVP_MD_CTX *mdctx;
    const EVP_MD *md;
    //char *message = "Test Message\n";
    //char *digestName= "md5";
    unsigned char md_value[EVP_MAX_MD_SIZE];
    unsigned int md_len, i;

    md = EVP_get_digestbyname(digestName);

    if (md == NULL) {
	printf("Unknown message digest %s\n", digestName);
	exit(1);
    }

    mdctx = EVP_MD_CTX_new();
    EVP_DigestInit_ex(mdctx, md, NULL);
    EVP_DigestUpdate(mdctx, message, strlen(message));
    EVP_DigestFinal_ex(mdctx, md_value, &md_len);
    EVP_MD_CTX_free(mdctx);

    for (i = 0; i < md_len; i++)
	printf("%02x", md_value[i]);
	
}

void hasher(char *nom, char *digestName){
	//on prend le contenu du fichier
	char * buffer = 0;
	buffer= 0;
	long length;
	FILE * f = fopen (nom, "rb");

	if (f)
	{
	  fseek (f, 0, SEEK_END);
	  length = ftell (f);
	  fseek (f, 0, SEEK_SET);
	  buffer = malloc (length);
	  if (buffer)
	  {
	    fread (buffer, 1, length, f);
	  }
	  fclose (f);
	}
	else{
		printf("File %s doesn't exist\n", nom);
		exit(0);
	}

	//on hash le contenu du fichier
	hashage(buffer, digestName);
	printf("           %s", nom);
	printf("\n");
}



