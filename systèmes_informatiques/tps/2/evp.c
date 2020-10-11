#include <openssl/evp.h>

void EVP_MD_CTX_init(EVP_MD_CTX *ctx);
EVP_MD_CTX *EVP_MD_CTX_create(void);

int EVP_DigestInit_ex(EVP_MD_CTX *ctx, const EVP_MD *type, ENGINE *impl);
int EVP_DigestUpdate(EVP_MD_CTX *ctx, const void *d, size_t cnt);
int EVP_DigestFinal_ex(EVP_MD_CTX *ctx, unsigned char *md,
       unsigned int *s);

int EVP_MD_CTX_cleanup(EVP_MD_CTX *ctx);
void EVP_MD_CTX_destroy(EVP_MD_CTX *ctx);

int EVP_MD_CTX_copy_ex(EVP_MD_CTX *out,const EVP_MD_CTX *in);

int EVP_DigestInit(EVP_MD_CTX *ctx, const EVP_MD *type);
int EVP_DigestFinal(EVP_MD_CTX *ctx, unsigned char *md,
       unsigned int *s);

int EVP_MD_CTX_copy(EVP_MD_CTX *out,EVP_MD_CTX *in);

#define EVP_MAX_MD_SIZE (16+20) /* The SSLv3 md5+sha1 type */

#define EVP_MD_type(e)                 ((e)->type)
#define EVP_MD_pkey_type(e)            ((e)->pkey_type)
#define EVP_MD_size(e)                 ((e)->md_size)
#define EVP_MD_block_size(e)           ((e)->block_size)

#define EVP_MD_CTX_md(e)               (e)->digest)
#define EVP_MD_CTX_size(e)             EVP_MD_size((e)->digest)
#define EVP_MD_CTX_block_size(e)       EVP_MD_block_size((e)->digest)
#define EVP_MD_CTX_type(e)             EVP_MD_type((e)->digest)

const EVP_MD *EVP_md_null(void);
const EVP_MD *EVP_md2(void);
const EVP_MD *EVP_md5(void);
const EVP_MD *EVP_sha(void);
const EVP_MD *EVP_sha1(void);
const EVP_MD *EVP_sha224(void);
const EVP_MD *EVP_sha256(void);
const EVP_MD *EVP_sha384(void);
const EVP_MD *EVP_sha512(void);
const EVP_MD *EVP_dss(void);
const EVP_MD *EVP_dss1(void);
const EVP_MD *EVP_mdc2(void);
const EVP_MD *EVP_ripemd160(void);

const EVP_MD *EVP_get_digestbyname(const char *name);
#define EVP_get_digestbynid(a) EVP_get_digestbyname(OBJ_nid2sn(a))
#define EVP_get_digestbyobj(a) EVP_get_digestbynid(OBJ_obj2nid(a))
