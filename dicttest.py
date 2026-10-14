word = "HelloWorldThisIsThailand"
wordlist = []
wordcount = {}
for i in word.lower:
    wordlist.append(i.lower())

for a in wordlist:
    if a not in wordcount.values():
        wordcount[a] = 1
    else:
        wordcount[a] += 1

print(wordcount)