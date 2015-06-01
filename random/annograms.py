'''
Question:
----

Implement a function that uses a word list
to return the annograms of a given word.

Answer:
----
'''

def annograms(word):

    '''
    For every string in WORD.LST return a copy of the string with trailing characters removed
    and assign it to the var 'words'
    '''
    words = [ _.rstrip() for _ in open('WORD.LST')]

    '''
    Assign list of items in arg (word) to var sword.
    Ex: yard would now read: ['a', 'd', 'r', 'y']
    '''
    sword = sorted(word)

    '''
    For each arg (word) passed into the function assign it to var 'annogram'
    if sorted items from 'WORD.LST' match sorted arg word
    '''
    annogram = [ _ for _ in words if sorted(_) == sword ]
    if annogram:
        return annogram
    else:
        raise NotImplementedError


if __name__ == '__main__':

    print annograms('yard')
    print '--'
    print annograms('drive')
    print '--'
    print annograms('python')

