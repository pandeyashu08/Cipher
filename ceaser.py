alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"
            ,"q","r","s","t","u","v","w","x","y","z"]

def encrypt(plain_text,shift_key):
    cipher_text =  ""
    for char in plain_text:
        position = alphabet.index(char)
        new_position = (position + shift_key)%26
        cipher_text += alphabet[new_position]
    print(f"Encrypted Cipher text: {cipher_text}")

def decrypt(cipher_text,shift_key):
    plain_text =  ""
    for char in cipher_text:
        position = alphabet.index(char)
        new_position = (position - shift_key)%26
        plain_text += alphabet[new_position]
    print(f"Encrypted Cipher text: {plain_text}")

what_to_do = input("Type 'encrypt' for encryption, type 'decrypt' for decryption: \n")
text = input("Enter your message:\n")
shift=int(input("Enter shift key:\n"))
if what_to_do == "encrypt":
    encrypt(plain_text=text,shift_key=shift)
elif what_to_do == "decrypt":
    decrypt(cipher_text=text,shift_key=shift)
