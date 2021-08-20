# Caesar Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(direction,text, shift):
    encoded_word = ""
    if direction == 'encode':
        for letter in text:
            
            if letter not in alphabet:
                encoded_word += letter
            
            elif alphabet.index(letter) + shift > len(alphabet):
                encoded_word += alphabet[(alphabet.index(letter) + shift)-26]
            
            else:
                encoded_word += alphabet[alphabet.index(letter) + shift]
        print(encoded_word)
    elif direction == 'decode':
        encoded_word = ""
        for letter in text:
            if letter not in alphabet:
                encoded_word += letter
            else:
                encoded_word += alphabet[alphabet.index(letter) - shift]

    print(encoded_word)
caesar(direction, text, shift)
