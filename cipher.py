def caesar_cipher_encrypt(text, shift=5):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha(): 
            shift_base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text

def main():
    plain_text = input("Please enter a sentence: ")
    encrypted_text = caesar_cipher_encrypt(plain_text)
    print("The encrypted sentence is:", encrypted_text)
if __name__ == "__main__":
    main()
