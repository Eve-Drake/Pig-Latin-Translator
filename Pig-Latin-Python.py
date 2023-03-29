def translate():
    sentence = input('Input your sentence... ')
    wordsList = sentence.split()
    vowelList = ['a', 'e' , 'i', 'o', 'u']
    i = 0
    print(wordsList)
    while i < len(wordsList):
        currentWord = wordsList[i].lower()
        if currentWord[0] in vowelList:
            currentWord = currentWord + 'ay'
        else:
            

        print(currentWord)
        i = 1 + i

translate()