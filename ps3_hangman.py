# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program


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

#    import string
    availableCharacters = ''
    for i in string.ascii_lowercase:
        if i not in lettersGuessed:
            availableCharacters += i
    return availableCharacters
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''



    lettersGuessed = []
    mistakesMade = 0
    availableLetters = string.ascii_lowercase
    allGuessedLeter = []
    guessedWord = ''


    # Welcome ; Start the Game
    print('Welcome to the game, Hangman! \nI am thinking of a word that is '+ str(len(secretWord)) +  ' letters long.')


    while mistakesMade < 8:
        print('-------------')
        if isWordGuessed(secretWord, lettersGuessed):
            break
        else:
            print ('You have '+ str(8-mistakesMade)+ ' guesses left.')
            print ('Available letters: '+ str(availableLetters))
            guess = raw_input('Please guess a letter: ')
            if guess in allGuessedLeter:
                print("Oops! You've already guessed that letter: " + str(guessedWord))
            else:
                if len(guess) == 1 and guess in secretWord:
                    lettersGuessed.append(guess)
                    allGuessedLeter.append(guess)
                    guessedWord = getGuessedWord(secretWord, lettersGuessed)
                    print('Good guess: ' + str(guessedWord))
                    availableLetters = getAvailableLetters(lettersGuessed)


                elif len(guess) == 1 and guess not in secretWord:
                    lettersGuessed.append(guess)
                    guessedWord = getGuessedWord(secretWord, lettersGuessed)
                    print('Oops! That letter is not in my word: '+ str(guessedWord))
                    availableLetters = getAvailableLetters(lettersGuessed)
                    allGuessedLeter.append(guess)
                    mistakesMade += 1
                elif len(guess) != 1:
                    print('Not a single character! Try again')

    if mistakesMade  < 8:
        print('Congratulations, you won!')

    else:
        print('-------------')
        print('Sorry, you ran out of guesses. The word was '+ str(secretWord)+ '.')








# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

#wordlist = loadWords()
#secretWord = chooseWord(wordlist).lower()
secretWord = 'c'
hangman(secretWord)
