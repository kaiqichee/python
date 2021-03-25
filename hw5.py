'''
Created on October 13, 2019
@author: Kai Qi Chee and Bonnie Nguyen
Pledge: I pledge my honor that I have abided by the Stevens Honor System.
CS115 - Hw 5
'''
from cs115 import map, reduce, filter
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5
# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1
# Do not change the variables above.
# Write your functions here. You may use those variables in your code.


def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    if n%2==0:
        return False
    else:
        return True
    
def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned'''
    if n==0: 
      return '' 
    elif isOdd(n): 
      return numToBinary(n//2) +str(n%2)
    else: 
      return numToBinary(n//2) +str(n%2)

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
        
    
def compress(s):
    '''Takes a binary string s and returns a run length encoded binary string'''
    def compresshelper(s,c):
        '''Returns seperated segments of 0's and 1's in string s'''
        if len(s)==1:
            return [c]
        else:
            if s[0]==s[1]:
                return compresshelper(s[1:],c+1)
            else:
                return [c]+compresshelper(s[1:],1)   
    def compresshelper2(y):
        '''Returns the length of each divded segment in list y'''
        return map(lambda x: numToBinary(x),y)
    z=compresshelper2(compresshelper(s,1))
    def filler(z):
        '''Pads z with 0's or 1's so it has length of 5'''
        if len(z)>COMPRESSED_BLOCK_SIZE:
            w=binaryToNum(z)-31
            return '11111'+'00000'+filler(numToBinary(w))
        else:
            q=5-len(z)
            return q*'0'+z
    z=map(filler,z)
    t=reduce(lambda x,y: x+y, z)
    if s[0]=='1':
        return '00000'+t
    else:
        return t


def uncompress(s):
    '''Takes a run length encoded binary string s and returns
    the uncompressed binary string'''
    def uncompresshelper(s):
        '''Seperates s into segments of 5 bits'''
        if len(s)==COMPRESSED_BLOCK_SIZE:
            return [s]
        else:
             return [s[:COMPRESSED_BLOCK_SIZE]] + uncompresshelper(s[COMPRESSED_BLOCK_SIZE:])
    def uncompresshelper2(y):
        '''Takes each segment of y and converts it from a binary value to a number'''
        return map(lambda x: binaryToNum(x),y)
    z=uncompresshelper2(uncompresshelper(s))
    def uncompresshelper3(x,b):
        '''Alternates multiplication of '0' and '1' with the values in x'''
        if x==[]:
            return ''
        elif b==0:
            b=1
            return x[0]*'0' + uncompresshelper3(x[1:],b)
        else:
            b=0
            return x[0]*'1' + uncompresshelper3(x[1:],b)
    return uncompresshelper3(z,0)

def compression(x):
    '''Returns the ratio between the compressed length of x, and the length of x'''
    return len(compress(x))/len(x)
    
