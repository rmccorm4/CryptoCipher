### Auther:  Ryan McCormick
### Project: CryptoCypher

#Spellchecking library to decrypt ciphers without knowing shift
import enchant
#On Arch Linux, need to download english dictionary
#pacman -S aspell-en

######CAESAR CYPHER#####
#Shifts plaintext uniformly by n letters

#E(n) = (x+n) mod 26
def caesarEncrypt(plaintext, shift):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	ciphertext = []
	plaintext = plaintext.lower()
	for char in plaintext:
		if char in alphabet:
			#mod 26 to loop around if value exceeds 25
			shiftedChar = alphabet[(alphabet.index(char) + shift) % 26]
			ciphertext.append(shiftedChar)
		elif char == " ":
			ciphertext.append(" ")
		else:
			print("You didn't enter letters of the alphabet!")
			break
	
	return ''.join(ciphertext)

def caesarDecrypt(ciphertext, shift=None):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	#Decrypting without shift
	if shift == None:
		for i in range(0, 26):
			plaintext = []
			for char in ciphertext:
				if char in alphabet:
					shiftedChar = alphabet[(alphabet.index(char) - i) % 26]
					plaintext.append(shiftedChar)
				elif char == " ":
					plaintext.append(" ")
			if(checkWords(''.join(plaintext))):
				return ''.join(plaintext)
	return None

def checkWords(text):
	wordList = text.split()
	englishDict = enchant.Dict("en_US")
	for word in wordList:
		if englishDict.check(word):
			return True
	return False

def main():
	plaintext = input("Enter message to be encrypted: ")
	shift = int(input("Enter shift amount: "))
	encryption = caesarEncrypt(plaintext, shift)
	print("Encrypted Message:", encryption)
	print("Decrypted Message:", caesarDecrypt(encryption))

main()
