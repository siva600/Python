#!/usr/bin/python
# encoding=utf8
"""
The Fisher–Yates shuffle is an algorithm for generating a random permutation of a finite sequence.
For more details visit
wikipedia/Fischer-Yates-Shuffle.
"""
import secrets

def FYshuffle(LIST):
    for i in range(len(LIST)):
        a = secrets.SystemRandom().randint(0, len(LIST)-1)
        b = secrets.SystemRandom().randint(0, len(LIST)-1)
        LIST[a], LIST[b] = LIST[b], LIST[a]
    return LIST

if __name__ == '__main__':
    integers = [0,1,2,3,4,5,6,7]
    strings = ['python', 'says', 'hello', '!']
    print ('Fisher-Yates Shuffle:')
    print ('List',integers, strings)
    print ('FY Shuffle',FYshuffle(integers), FYshuffle(strings))
