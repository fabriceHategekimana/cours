#include<stdlib.h>
#include<stdio.h>
#include <stdio.h>
#include <string.h>
#include <openssl/evp.h>
#include "hash.h"

int getContenu(char *fichier){
	FILE *fid= fopen(fichier, "r");
	char *texte;
	fseek(fid, 0, SEEK_END);
	long fsize = ftell(fid);
	fseek(fid, 0, SEEK_SET);  /* same as rewind(f); */
	char *string = malloc(fsize + 1);
	fread(texte, 1, fsize, fid);

	fclose(fid);
	string[fsize] = 0;
}

int hasher(char *fichier, char *fonction){

}

int main(int argc, char *argv[])
{
    EVP_MD_CTX *mdctx;
    const EVP_MD *md;
    char mess1[] = "Test Message\n";
    char mess2[] = "Hello World\n";
    unsigned char md_value[EVP_MAX_MD_SIZE];
    unsigned int md_len, i;

    if (argv[1] == NULL) {
	printf("Usage: mdtest digestname\n");
	exit(1);
    }

    md = EVP_get_digestbyname(argv[1]);
    if (md == NULL) {
	printf("Unknown message digest %s\n", argv[1]);
	exit(1);
    }

    mdctx = EVP_MD_CTX_new();
    EVP_DigestInit_ex(mdctx, md, NULL);
    EVP_DigestUpdate(mdctx, mess1, strlen(mess1));
    EVP_DigestUpdate(mdctx, mess2, strlen(mess2));
    EVP_DigestFinal_ex(mdctx, md_value, &md_len);
    EVP_MD_CTX_free(mdctx);

    printf("Digest is: ");
    for (i = 0; i < md_len; i++)
	printf("%02x", md_value[i]);
    printf("\n");

    exit(0);
}


