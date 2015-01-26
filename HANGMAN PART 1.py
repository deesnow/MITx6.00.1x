__author__ = 'suni'

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    catch = []
    for i in secretWord:
        if i in lettersGuessed:
            catch.append(i)
    if len(catch) == len(secretWord):
        return True
    else:
        return False

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    catchWord = ''
    for i in secretWord:
        if i in lettersGuessed:
            catchWord += i
        else:
            catchWord += '_ '
    return catchWord

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''

    import string
    availableCharacters = ''
    for i in string.ascii_lowercase:
        if i not in lettersGuessed:
            availableCharacters += i
    return availableCharacters







