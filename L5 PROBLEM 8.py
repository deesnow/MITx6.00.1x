__author__ = 'suni'

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    if aStr == '':
        return False

    elif len(aStr) == 1:
        if char == aStr:
            return True
        else:
            return False
    else:
        if char == aStr[len(aStr)/2]:
            return True
        elif char < aStr[len(aStr)/2]:
            return isIn(char, aStr[:len(aStr)/2])
        elif char > aStr[len(aStr)/2]:
            return isIn(char, aStr[len(aStr)/2+1:])





