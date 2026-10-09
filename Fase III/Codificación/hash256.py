import hashlib
def encrypt_string(hash_string):
    print("1 ",type(hashlib.sha256(hash_string.encode())))
    print("2 ",hashlib.sha256(hash_string.encode()))
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

hash_string = 'confidential data'
sha_signature = encrypt_string(hash_string)
print("3",sha_signature)
