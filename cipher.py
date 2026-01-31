word = str(input("Enter a word: "))
key = int(input("Enter a key: "))
newWord=[]
item=0
for x in word.upper():
    if ord(x)<65 or ord(x)>90:
        newWord.append(x)
    else:
        item=ord(x)+key
        if item>90:
            item=item-26
        elif item<65:
            item=item+26
        newWord.append(chr(item))
print(*newWord)
