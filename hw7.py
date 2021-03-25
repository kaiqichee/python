'''
Created on October 25, 2019
Author: Kai Qi Chee
Pledge: I pledge my honor that I have abided by the Stevens Honor System.

cs115-hw7
'''
from cs115 import map, reduce, filter

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
    
def flip(t):
    '''Flips the 0's to 1's and 1's to 0's in a string t'''
    if t=='':
        return ''
    elif t[0]=='0':
        return '1'+flip(t[1:])
    else:
        return '0'+flip(t[1:])
            
def TcToNum(x):
    '''Takes Two's Complement value and returns the equivalent base 10 number'''
    q=flip(x)
    if x[0]=='1':
        f=(binaryToNum(q)+1)
        return f*-1
    else:
        return binaryToNum(x)

def NumToTc(x):
    '''Takes a base 10 number and returns its Two's Complement equivalent'''
    if x>127 or x<-128:
        return 'Error'
    else:
        def pad(t):
            '''Pads string t so its length is 8'''
            if len(t)<8:
                return ((8-len(t))*'0')+t
            elif len(t)>8:
                return 'Error'
            else:
                return t
        def help(x):
            '''Returns the Two's Complement equivalent of x'''
            if str(x)[0]!='-':
                return pad(numToBinary(x))
            else:
                u=numToBinary(abs(x))
                v=pad(u)
                print (v)
                z=flip(v)
                print (z)
                return pad(numToBinary(binaryToNum(z)+1))
            
        return help(x)

  


    
