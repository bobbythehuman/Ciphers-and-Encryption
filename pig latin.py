word = input("Enter: ")
newword = []
w=[]
nw=[]
word=word.split(" ")
vowel = ["a","e","i","o","u"]
for x in word:
    if x[0] in vowel:
        newword.append(x+"way")
    else:
        
        for y in range(len(x)):
            w.append(x[y])
            nw.append(x[y])
        for i in range(len(w)):
            if w[0] not in vowel:
                nw.insert(len(w),str(w[0]))
                del w[0]
                del nw[0]
        newword.append(nw)
        w.clear
        nw.clear
print(*newword)
