'''
Created on September 20, 2019
I pledge my honor that I have abided by the Stevens Honor System.
@author: Kai Qi Chee
username: kchee

CS115 - Hw 2
'''

import sys
from cs115 import map, reduce, filter
# Be sure to submit hw2.py.  Remove the '_template' from the file name.
# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']
   
def letterScore(letter, scorelist):
    "returns the value of a given letter as assigned in scorelist"
    if scorelist[0][0]==letter:
        return scorelist[0][1]
    else:
        return letterScore(letter,scorelist[1:])

    
def wordScore(S, scorelist):
    "returns the value of a word as assigned in scorelist"
    if S=='':
        return 0
    else:
        return letterScore(S[0],scorelist)+wordScore(S[1:],scorelist)


def remove(e,L):
    "returns list L without e"
    if L==[]:
        return []
    elif L[0]==e:
        return L[1:]
    else:
        return [L[0]]+remove(e,L[1:])

   
def listCheck(d,r):
    "returns if word d can be made from letters in r"
    if d=='':
        return True
    elif d[0] in r:
        r=remove(d[0],r)
        return listCheck(d[1:],r)
    else:
        return False


def checkWord(d,r):
    "returns list of words from d that can be made from letters in r"
    return filter(lambda x: listCheck(x,r),d)


def scoreList(Rack):
    "returns the list of words that can be made from letters in Rack along with their values"
    if checkWord(Dictionary,Rack)==[]:
        return (['',0],['',0])
    else:
        return map(lambda y: [y,wordScore(y, scrabbleScores)],checkWord(Dictionary,Rack))


def maxWord(x,y):
    "returns the highest component out of x and y"
    if x[1]>y[1]:
        return x
    else:
        return y

   
def bestWord(Rack):
    "returns the highest scoring word that can be made from letters in Rack"
    return reduce(maxWord,scoreList(Rack))
