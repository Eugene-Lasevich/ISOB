def encrypt_vigenere(input_file, output_file, key, decrypt=False):
    with open(input_file, 'r') as file:
        plain_text = file.read()

    encrypted_text = ""
    key_length = len(key)
    key_index = 0

    for char in plain_text:
        if char.isalpha():
            key_char = key[key_index % key_length].lower()
            shift = ord(key_char) - ord('a')
            key_index += 1

            # Determine the direction of the shift based on whether it's encryption or decryption
            direction = 1 if not decrypt else -1

            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + direction * shift) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + direction * shift) % 26 + ord('a'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    with open(output_file, 'w') as file:
        file.write(encrypted_text)

if __name__ == "__main__":
    input_file = "text"
    output_file = "vigenere_text"
    new_input_file = "new_vigenere_text"
    key = input("Enter the encryption key: ")

    encrypt_vigenere(input_file, output_file, key, decrypt=False)
    encrypt_vigenere(output_file, new_input_file, key, decrypt=True)
    print("Decryption completed. The decrypted text is written to the file", output_file)
