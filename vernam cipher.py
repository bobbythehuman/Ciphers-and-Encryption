import random
import string


def XORTwoChars(char1, char2):
    temp = ""
    for x in range(len(char1)):
        if char1[x] != " ":
            if char1[x] == char2[x]:
                temp = temp + "0"
            else:
                temp = temp + "1"
        else:
            temp = temp + " "
    return temp


def generateOTP(ptext):
    text = ""
    for x in range(len(ptext)):
        text = text + str(random.choice(string.ascii_uppercase))
    return text


def performEncoding(message, key=""):
    EncText = ""
    EncKey = ""
    for x in message:
        EncText = EncText + str(baudotCodes[x]) + " "
    for i in key:
        EncKey = EncKey + str(baudotCodes[i]) + " "
    return (EncText, EncKey)


def performDecoding(message, key=" "):
    EncText = ""
    EncKey = ""
    for x in message.split(" "):
        if x != "":
            EncText = EncText + str(baudotReverse[x])
    for i in key.split(" "):
        if i != "":
            EncKey = EncKey + str(baudotReverse[i])
    return (EncText, EncKey)


key = ""
CodMessage = ""
baudotCodes = {
    ".": "00000",
    "E": "00001",
    "\n": "00010",
    "A": "00011",
    " ": "00100",
    "S": "00101",
    "I": "00110",
    "U": "00111",
    "~": "01000",
    "D": "01001",
    "R": "01010",
    "J": "01011",
    "N": "01100",
    "F": "01101",
    "C": "01110",
    "K": "01111",
    "T": "10000",
    "Z": "10001",
    "L": "10010",
    "W": "10011",
    "H": "10100",
    "Y": "10101",
    "P": "10110",
    "Q": "10111",
    "O": "11000",
    "B": "11001",
    "G": "11010",
    ",": "11011",
    "M": "11100",
    "X": "11101",
    "V": "11110",
    "!": "11111",
}

baudotReverse = {
    "00000": ".",
    "00001": "E",
    "00010": "\n",
    "00011": "A",
    "00100": " ",
    "00101": "S",
    "00110": "I",
    "00111": "U",
    "01000": "~",
    "01001": "D",
    "01010": "R",
    "01011": "J",
    "01100": "N",
    "01101": "F",
    "01110": "C",
    "01111": "K",
    "10000": "T",
    "10001": "Z",
    "10010": "L",
    "10011": "W",
    "10100": "H",
    "10101": "Y",
    "10110": "P",
    "10111": "Q",
    "11000": "O",
    "11001": "B",
    "11010": "G",
    "11011": ",",
    "11100": "M",
    "11101": "X",
    "11110": "V",
    "11111": "!",
}

plaintext = "THE SECRET TO EVERYTHING IS FORTY TWO"
print(f"Plaintext: {plaintext}")

key = generateOTP(plaintext)
print(f"Generated key: {key}")

ciphertext, key = performEncoding(plaintext, key)
print(f"Ciphertext: {ciphertext}")
print(f"Key: {key}")

CodMessage = XORTwoChars(ciphertext, key)
print(f"Encoded Message: {CodMessage}")

ciphertext, keyUsed = performEncoding(plaintext)
print(f"Ciphertext: {ciphertext}")

recoveredText, key = performDecoding(ciphertext, keyUsed)
print("*" * len(plaintext))
print(f"Original Encoded Message: {CodMessage}")
print(f"Recovered Text: {recoveredText}")
