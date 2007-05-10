"""
convert a number to a string representation in a given base
"""
def tobase(base,number):
    def tb(b,n,result=''):
        if n == 0: return result
        else: return tb(b,n/b,str(n%b)+result)
    if type(base) != type(1):
        raise TypeError, 'invalid base for tobase()'
    if base <= 0:
        raise ValueError, 'invalid base for tobase(): %s' % base
    if type(number) != type(1) and type(number) != type(1L):
        raise TypeError, 'tobase() of non-integer'
    if number == 0:
        return '0000'
    if number > 0:
        return tb(base, number)
    if number < 0:
        return '-' + tb(base, -1*number)
