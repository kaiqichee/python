'''
Created on: October 18, 2019
Author: Kai Qi Chee
Pledge: I pledge my honor that I have abided by the Stevens Honor System

cs115-hw6
'''
from cs115 import map, reduce, filter

def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    if n%2==0:
        return False
    else:
        return True
        
def numToBaseB(N,B):
    '''Precondition: integer argument is non-negative.
    Returns the string with the base B representation of non-negative integer n.
    If n is 0, the empty string is returned
    '''
    def helper1(N,B):
        if int(N)==0: 
          return '0'
        elif N%B != 0:
            w=str(numToBaseB(int(N)//B, B)) + (str(N%B))
            return w
        else:
            z=str(numToBaseB(int(N)//B, B)) + (str(N%B))
            return z
    f=helper1(N,B)
    def helper2(x):
        if x=='':
            return 0
        elif x[0]!='0':
            return x
        else:
            return helper2(x[1:])
    return helper2(f)
            
    
    
def baseBToNum(S,B):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if S=="":
        return 0
    elif B==10:
        return int(S)
    else:

        def baseBToNum_helper(S,B):
            if S=='': 
              return '0' 
            elif (int(S[-1]))%int(B) != 0: 
                return '1' + B*baseBToNum_helper(S[:-1],B)  #odd
            else: 
                return '0' + B*baseBToNum_helper(S[:-1],B)  #even
        z=baseBToNum_helper(S,B)
        def helper2(s):
            if s=='':
                return 0
            else:
                return int(s[0])+helper2(s[1:])
        return helper2(z)

def baseToBase(B1,B2,SinB1):
    x=baseBToNum(SinB1,B1)
    return numToBaseB(x,B2)
    

def add(S,T):
    x=baseBToNum(S,2)
    y=baseBToNum(T,2)
    z=x+y
    return numToBaseB(z,2)
    

def addB(A,B):
    if len(A)<len(B):
        A=(len(B)-len(A))*'0'+A
    if len(B)<len(A):
        B=(len(A)-len(B))*'0'+B
        
    def helper1(A,B,ci):
        if A=='' or B=='':
            if ci=='0':
                return ''
            else:
                return ci
        elif A[-1]=='0' and B[-1]=='0' and ci=='0':
            ci='0'
            return helper1(A[:-1],B[:-1],ci)+'0'
        
        elif A[-1]=='0' and B[-1]=='0' and ci=='1':
            ci='0'
            return helper1(A[:-1],B[:-1],ci)+'1'
        
        elif A[-1]=='0' and B[-1]=='1' and ci=='0':
            ci='0'
            return helper1(A[:-1],B[:-1],ci)+'1'
        
        elif A[-1]=='0' and B[-1]=='1' and ci=='1':
            ci='1'
            return helper1(A[:-1],B[:-1],ci)+'0'
        
        elif A[-1]=='1' and B[-1]=='1' and ci=='1':
            ci='1'
            return helper1(A[:-1],B[:-1],ci)+'1'
        
        elif A[-1]=='1' and B[-1]=='0' and ci=='0':
            ci='0'
            return helper1(A[:-1],B[:-1],ci)+'1'
        
        elif A[-1]=='1' and B[-1]=='0' and ci=='1':
            ci='1'
            return helper1(A[:-1],B[:-1],ci)+'0'
        else:
            ci='1'
            return helper1(A[:-1],B[:-1],ci)+'0'
        
    q=helper1(A,B,'0')
    def helper2(x):
        if x=='':
            return 0
        elif x[0]!='0':
            return x
        else:
            return helper2(x[1:])

    return helper2(q)
