from pwdlib import PasswordHash

pasword_hash = PasswordHash.recommended()

def hash_password(password : str) -> str:
    return pasword_hash.hash(password)

def verify_password(plain_password : str, hashed_password: str) -> bool:
    return pasword_hash.verify(plain_password, hashed_password)