__author__ = 'suni'

'''
We want to write some simple procedures that work on dictionaries to return information.

This time, write a procedure, called biggest, which returns the key corresponding to the entry with
the largest number of values associated with it. If there is more than one such entry, return any
one of the matching keys.

'''


animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


def biggest(aDict):
    if len(aDict.keys()) == 0:
        return None
    else:
        maxkey = ''
        lenght = 0
        for i in aDict.keys():
            if len(aDict[i])>= lenght:
                lenght = len(aDict[i])
                maxkey = i
        return maxkey




