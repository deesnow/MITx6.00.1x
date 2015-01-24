__author__ = 'suni'
def lenIter(aStr):
    '''
    aStr: a string

    returns: int, the length of aStr
    '''
    # Your code here

    counter = 0
    for char in aStr:
        counter += 1
    return counter

z = len('valami')
print (z)