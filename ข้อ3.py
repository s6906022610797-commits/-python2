def word_frequency(text: str) -> dict:
    word_list = text.split()
    wordcount = {}

    

    for a in word_list:
        if a not in wordcount.keys():
            wordcount[a] = 1
        else:
            wordcount[a] += 1

    return wordcount

print(word_frequency("Hello world Hello everyone."))

#print(word_frequency("This is a test. This test is easy."))

#print(word_frequency("Python is fun. Fun fun fun"))