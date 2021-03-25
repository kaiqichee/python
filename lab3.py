'''
Created on September 18, 2019
I pledge my honor that I have abided by the Stevens Honor System.
@author: Kai Qi Chee
username: kchee
'''

from cs115 import map, reduce, filter

def change(amount, coins):
    "returns the least amount of coins needed to create the amount"
    if amount == 0:
        return 0
    if coins == []:
        return float('inf')
    elif coins[0] > amount:
        return change(amount, coins[1:])
    else:
        useIt = 1 + change(amount - coins[0], coins)
        loseIt = change(amount, coins[1:])
    return min(useIt, loseIt)

      
