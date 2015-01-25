__author__ = 'suni'
'''
We want to write some simple procedures that work on dictionaries to return information.

First, write a procedure, called howMany, which returns the sum of the number of values associated with a dictionary. For example:

>>> print howMany(animals)
6

'''


animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')



def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many individual values are in the dictionary.
    '''
    result = 0
    for value in aDict.values():
        # Since all the values of aDict are lists, aDict.values() will
        #  be a list of lists
        result += len(value)
    return result

def howMany2(aDict):
    '''
    Another way to solve the problem.

    aDict: A dictionary, where all the values are lists.

    returns: int, how many individual values are in the dictionary.
    '''
    result = 0
    for key in aDict.keys():
        result += len(aDict[key])
    return result

def howMany3(aDict):
    '''
    flatened the value of dictionary, and count the element number
    '''
    return len(sum(aDict.values(),[]))

