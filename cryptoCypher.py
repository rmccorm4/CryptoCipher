### Auther:  Ryan McCormick
### Project: CryptoCypher


######CAESAR CYPHER#####
#Shifts plaintext uniformly by n letters

#E(n) = (x+n) mod 26
def caesarEncrypt(plaintext, shift):
    ciphertext = [ch += shift for ch in plaintext]
    return ciphertext

#D(n) = (x-n) mod 26
def caesarDecrypt(ciphertext, shift):
    plaintext = [ch -= shift for ch in ciphertext]
    return plaintext

def main():
    plaintext = input("Enter message to be encrypted" )
    shift = input("Enter shift amount: ")
    print("Encrypted Message:", caesarEncrypt(plaintext, shift))

main()
