def encrypt_caesar(input_file, output_file, shift, decrypt=False):
    with open(input_file, 'r') as file:
        plain_text = file.read()

    encrypted_text = ""

    direction = 1 if not decrypt else -1

    for char in plain_text:
        if char.isalpha():
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
    output_file = "ceaser_text"
    new_file = "ceaser_new_file"
    shift = int(input("Enter offset: "))

    encrypt_caesar(input_file, output_file, shift, decrypt=False)
    encrypt_caesar(output_file, new_file, shift, decrypt=True)
    print("Decryption is complete. The decrypted text is written to a file", output_file)
