# Caesar Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(direction,text, shift):
    if direction == 'encode':
        encoded_word = ""
        for letter in text:
            if alphabet.index(letter) + shift > len(alphabet):
                encoded_word += alphabet[(alphabet.index(letter) + shift)-26]
            else:
                encoded_word += alphabet[alphabet.index(letter) + shift]
        print(encoded_word)
    elif direction == 'decode':
        decoded_word = ""
    for letter in text:
        
        decoded_word += alphabet[alphabet.index(letter) - shift]

    print(decoded_word)
caesar(direction, text, shift)
