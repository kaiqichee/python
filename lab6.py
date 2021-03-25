'''
Created on October 8, 2019
@author:   Kai Qi Chee
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.
CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    if n%2==0:
        return False
    else:
        return True
    
def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned
    '''
    if n==0: 
      return '' 
    elif isOdd(n): 
      return numToBinary(n//2) +'1'
    else: 
      return numToBinary(n//2) +'0'

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s=='': 
      return 0 
    elif isOdd(int(s[-1])): 
      return 1 + 2*binaryToNum(s[:-1])  #odd
    else: 
      return 0 + 2*binaryToNum(s[:-1])  #even

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    x=numToBinary(binaryToNum(s)+1)
    if len(x)>8:
        x=x[-8:]
    return (8-len(x))*'0'+x

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n==0:
        print(s)
    else:
        print(s)
        count(increment(s),n-1)


def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n==0: 
      return '' 
    return numToTernary(n//3) + str(n % 3)

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s=='': 
        return 0 
    return int(s[-1])+3*(ternaryToNum(s[:-1]))





