'''
Created on September 25, 2019
I pledge my honor that I have abided by the Stevens Honor System.
@author: Kai Qi Chee
username: kchee
'''

from cs115 import map,reduce,filter

def coin_row(L):
    "Returns the largest number that can be made with the values in the list"
    if L==[]:
        return 0
    elif L[0]==0:
        return coin_row(L[1:])
    else:
        useIt =L[0] + coin_row(L[2:])
        loseIt = coin_row(L[1:])
        return max(useIt,loseIt)

def coin_row_with_values(L):
    "returns the largest number that can be made with the values in the list, with the values used"
    if L==[]:
        return [0,[]]
    elif L[0]==0:
        return coin_row_with_values(L[1:])
    else:
        useIt=coin_row_with_values(L[2:])
        loseIt=coin_row_with_values(L[1:])
        useIt2=[useIt[0]+L[0] , [L[0]]+useIt[1]]
        return max(useIt2,loseIt)



