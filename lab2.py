'''
Created on September 11, 2019
I pledge my honor that I have abided by the Stevens Honor System.
@author: Kai Qi Chee
username: kchee
'''

from cs115 import map, reduce

def even(X):
    "returns if X is an even or odd number"
    if X % 2 == 0 :
        return True 
    else:
        return False
    
def reverse(L):
    "returns list L in reverse"
    if myLength(L)==0:
        return L
    else: 
        return L[-1:]+reverse(L[:-1])
    
    
def myLength(L):
    "returns length of L"
    if L==[]:
        return 0
    else:
        return(1+myLength(L[1:]))


def isList(x):
    "returns if x is a list"
    if isinstance(x, list):
        return True
    else:
        return False


def dot(L,K):
    "returns the dot product of vectors L and K"
    if L==[] or K==[]:
        return 0
    else:
        result = (L[0]*K[0])+dot(L[1:],K[1:])
    return result


def explode(S):
    "returns S as a string into a list of individual strings"
    if S=='':
        return []
    else:
        return list(S[0])+list(explode(S[1:]))


def ind(e,L):
    "returns the index of position e in L"
    if L==[] or L=='':
        return 0
    elif L[0]==e:
        return 0
    else:
        return 1+ind(e,L[1:])

def removeAll(e,L):
    "returns list L without e"
    if L==[]:
        return []
    elif L[0]==e:
        return removeAll(e,L[1:])
    else:
        return [L[0]]+removeAll(e,L[1:])

def myFilter(e,L):
    "returns indexes of L applicable to e"
    if L==[]:
        return []
    elif e(L[0])==True:
        return [L[0]]+myFilter(e,L[1:])
    else:
        return myFilter(e,L[1:])


def deepReverse(L):
    "returns the reverse of list L, including the reverse of internal lists"
    if myLength(L)==0:
        return L
    elif isList(L[-1]):
         return [deepReverse(L[-1])]+deepReverse(L[:-1])
    else: 
        return L[-1:]+deepReverse(L[:-1])
    




