words = input("Enter word: ")
seperator = ""
newWord = ""

word = list(seperator.join(list(words)))

key = int(input("\nSize: "))

for i in range(0, len(word) // key + 1):
    for m in range(0, key):
        itemIndex = i + (key * m)
        # print(f"i + (key * m): {itemIndex}")
        if itemIndex < len(word):
            newWord = newWord + " " + word[itemIndex]
    print(newWord)
    newWord = ""
