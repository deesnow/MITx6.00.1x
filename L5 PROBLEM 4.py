__author__ = 'suni'

def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a > b:
        z = b
    else:
        z = a
    while z > 1:
        if b % z == a % z == 0:
            result = z
            break
        else:
            z = z-1
    return z

'''
orginal code

    while a % testValue != 0 or b % testValue != 0:
        testValue -= 1

    return testValue

'''



