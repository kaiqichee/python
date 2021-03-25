'''
Created on October 3, 2019
@author:   Kai Qi Chee
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.
CS115 - Hw 4
'''
import turtle  # Needed for graphics
# Ignore 'Undefined variable from import' errors in Eclipse.

    
def snowflakeSide(level, length):
    if level==0:
        turtle.forward(length)
    else:
        snowflakeSide(level-1,length)
        turtle.left(60)
        snowflakeSide(level-1,length)
        turtle.right(120)
        snowflakeSide(level-1,length)
        turtle.left(60)
        snowflakeSide(level-1,length)


def snowflake(trunk_length, levels):
    snowflakeSide(levels,trunk_length)
    turtle.right(120)
    snowflakeSide(levels,trunk_length)
    turtle.right(120)
    snowflakeSide(levels,trunk_length)

    
def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    memo={}
    def fast_change_helper(amount, coins, memo):
        if (amount,coins) in memo:
            return memo[(amount,coins)]
        elif amount == 0:
            return 0
        elif coins == ():
            return float('inf')
        elif coins[0] > amount:
            return fast_change_helper(amount, coins[1:],memo)
        else:
            useIt = 1 + fast_change_helper(amount - coins[0], coins,memo)
            loseIt = fast_change_helper(amount, coins[1:],memo)
            result = min(useIt, loseIt)
            memo[(amount,coins)]=result
            return result
    # Call the helper. Note we converted the list to a tuple.
    return fast_change_helper(amount, tuple(coins), memo)


# If you did this correctly, the results should be nearly instantaneous.
print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))


# Should take a few seconds to draw a snow flake
snowflake(10, 3)



