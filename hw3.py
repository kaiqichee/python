'''
Created on September 23, 2019
I pledge my honor that I have abided by the Stevens Honor System.
@author: Kai Qi Chee
username: kchee

CS115 - Hw 3
'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
from cs115 import map, reduce, filter

             
def giveChange(amount, coins):
    "returns the least amount of coins needed, and coins used, to create the amount"
    if amount ==0:
        return [0,[]]
    if coins == []:
        return [float('inf'),[]]
    elif coins[0] > amount:
        return giveChange(amount, coins[1:])
    else:
        useIt = giveChange(amount - coins[0], coins)
        loseIt = giveChange(amount, coins[1:])
        useIt2= [ useIt[0]+1 , [coins[0]]+useIt[1]]
    return min(useIt2, loseIt)


