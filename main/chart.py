import string

words = input("Enter word: ")
letters = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
    "E": 0,
    "F": 0,
    "G": 0,
    "H": 0,
    "I": 0,
    "J": 0,
    "K": 0,
    "L": 0,
    "M": 0,
    "N": 0,
    "O": 0,
    "P": 0,
    "Q": 0,
    "R": 0,
    "S": 0,
    "T": 0,
    "U": 0,
    "V": 0,
    "W": 0,
    "X": 0,
    "Y": 0,
    "Z": 0,
}
exclude = set(string.punctuation)
words = words.upper().split(" ")
# words = ''.join(ch for ch in words if ch not in exclude)
# print(words)

for x in words:
    # print(x)
    for l in list(x):
        # print(l)
        if l in letters.keys():
            letters[l] += 1

print(letters)
for i in letters:
    print(i, "|" * letters[i])
