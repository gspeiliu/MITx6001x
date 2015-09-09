def isWordGuessed(secretWord, lettersGuessed):
    for letter in secretWord:
        if not (letter in lettersGuessed):
            return False
    return True
    

def getGuessedWord(secretWord, lettersGuessed):
    res = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            res = res + letter
        else:
            res = res + '_ '
            
    return res

def getAvailableLetters(lettersGuessed):
    import string
    res = ''
    for letter in string.ascii_lowercase:
        if not (letter in lettersGuessed):
            res = res + letter
    return res

#secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print getAvailableLetters('')