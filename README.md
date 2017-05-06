# CryptoCipher
Messing around with various cipher types and cryptography in general because it interests me

Currently only implements a simple "Caesar Cipher" but plan to add more in the near future.

## Caesar Cipher
Shifts plaintext uniformly by some shift amount, I am currently making the assumption that only valid letters of the alphabet and spaces are allowed.

I thought that decrypting the message with a known shift would be no fun, so I decided to crack it without knowing the shift. To do this I made use of a spellchecking library called "PyEnchant" 

```
pip install pyenchant
```
Additionally, PyEnchant does not necessarily come with the English-US dictionary, so you may have to install it online. 

For Arch Linux:

```
pacman -S aspell-en
```
![Alt text](imgs/cryptocipher.png?raw=true "Progress Picture")
