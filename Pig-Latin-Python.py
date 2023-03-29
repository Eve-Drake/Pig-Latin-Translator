def translate():
    sentence = input('Input your sentence... ')
    wordsList = sentence.split()
    vowelList = ['a', 'e' , 'i', 'o', 'u']
    i = 0
    pigLatinSentence = []
    while i < len(wordsList):
        currentWord = wordsList[i].lower()
        if currentWord[0] in vowelList:
            currentWord = currentWord + 'ay'

        else:
            letter = currentWord[0]
            currentWord = currentWord[1:]
            currentWord = currentWord + '-' + letter + 'ay'
        pigLatinSentence.append(currentWord)
        i = 1 + i
    print(' '.join(pigLatinSentence))
translate()