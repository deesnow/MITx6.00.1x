__author__ = 'suni'

def semordnilapWrapper(str1, str2):
    '''
    str1: a string
    str2: a string

    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    # wrapper functions:
    if str1 == str2 or (len(str1) != len(str2)) or (str1 == '' or str2 == '') or (len(str1) and len(str2)== 1):
        return False
    else:
        return semordnilap(str1, str2)

def semordnilap (str1, str2):
    if (len(str1) and len(str2)== 1 ):
        if str1 == str2:
            return True
        else:
            return False
    else:
        return semordnilap(str1[1:], str2[:-1])


