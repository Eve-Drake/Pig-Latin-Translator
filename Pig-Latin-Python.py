def translate():
    sentence = input('Input your sentence... ')
    wordsArray = sentence.split()
    i = 0
    print(wordsArray)
    while i < len(wordsArray):
        currentWord = wordsArray[i]
        print(currentWord) 
        i = 1 + i

translate()