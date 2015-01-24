__author__ = 'suni'
def lenRecur(aStr):
    '''
    aStr: a string

    returns: int, the length of aStr
    '''
    # Your code here
    count = 0
    if aStr == '':
        return 0
    return 1 + lenRecur(aStr[:-1])