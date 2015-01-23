__author__ = 'suni'

def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here

    if a > b:
        if b ==0:
            return a
        else:
            return gcdRecur(b, a % b)
    else:
        if a == 0:
            return b
        else:
            return gcdRecur(a, b % a)