def caesar_cipher(text, shift, mode='encrypt'):
    result = ""

    # Adjust the shift value based on the mode
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        # Encrypt/Decrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt/Decrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Non-alphabetic characters remain unchanged
            result += char

    return result


def main():
    while True:
        # User input for message and shift value
        message = input("Enter the message: ")
        shift = int(input("Enter the shift value (positive integer): "))

        # Choose mode for encryption or decryption
        mode = input("Type 'e' for encryption or 'd' for decryption: ").lower()

        if mode == 'e':
            encrypted_message = caesar_cipher(message, shift, mode='encrypt')
            print("Encrypted Message:", encrypted_message)
        elif mode == 'd':
            decrypted_message = caesar_cipher(message, shift, mode='decrypt')
            print("Decrypted Message:", decrypted_message)
        else:
            print("Invalid mode. Please enter 'e' for encryption or 'd' for decryption.")

        # Ask if the user wants to continue
        cont = input("Do you want to continue? (yes/no): ").lower()
        if cont != 'yes':
            break


if __name__ == "__main__":
    main()
