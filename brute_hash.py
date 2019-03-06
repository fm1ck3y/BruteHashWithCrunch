from hashlib import md5, sha256, sha512
import sys

# chmod 777 brute_hash.py
# brute_hash.py type_hash hash.txt dict_word.txt

try:
    type_hash , file_hash, dict = sys.argv[1],sys.argv[2],sys.argv[3]
except:
    try:
        type_hash, file_hash = sys.argv[1], sys.argv[2]
        dict = sys.stdin.read()
    except:
        print("Error in arguments")
        print("EXAMPLE : brute_hash.py type_hash hash.txt dict_word.txt\nEXAMPLE : crunch 5 10 abcd | python3.6 brutehash.py type_hash hash.txt")
        raise SystemExit


with open(file_hash) as file:
    hashFunc = file.read()
    hashFunc = hashFunc.replace('\n','')

def encrypt(hash):
    passw = hash.encode()
    if type_hash.lower() == "md5":
        return md5(passw).hexdigest()
    if type_hash.lower() == "sha256":
        return sha256(passw).hexdigest()
    if type_hash.lower() == "sha512":
        return sha512(passw).hexdigest()
    return passw

try:
    with open(dict, errors="ignore") as file:
        dictionary = file.read()
except:
    dictionary = dict

dictionary = dictionary.split('\n')
for word in dictionary:
    passw = word.replace('\n','')
    if encrypt(passw) == hashFunc.lower():
        print("DECODING : ", word)
        break
    else:
        print("[FALSE] : ", word)


