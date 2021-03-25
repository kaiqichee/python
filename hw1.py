'''
Created on September 12, 2019
I pledge my honor that I have abided by the Stevens Honor System.
@author: Kai Qi Chee
username: kchee
'''

from cs115 import map, reduce

def mult(x,y):
    """returns the product of x and y"""
    return x*y

def add(x,y):
    """returns the sum of x and y"""
    return x+y

def factorial(n):
    """returns the factorial of n"""
    result=reduce(mult, list(range(1,n+1)))
    return result

def mean(L):
    """finds the mean of list L"""
    a=reduce(add, list(L))
    result=a/(len(L))
    return result

def div(k):
    """indicates if there is a remainder with 42/k"""   
    return 42 % k == 0

def divides(n):
    """indicates if there is a remainder with n/k"""   
    def div(k):
        return n % k == 0
    return div

def prime(n):
    """determines if n is a prime number"""
    L=list(range(2,n))
    P=map(divides(n),L)
    return (max(P) == False)
   

    
