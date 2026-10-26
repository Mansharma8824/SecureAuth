from pwdlib import PasswordHash

pasword_hash = PasswordHash.recommended()

def hash_password(password : str) -> str:
    return pasword_hash.hash(password)

