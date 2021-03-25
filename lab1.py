'''
Created on September 4, 2019
I pledge my honor that I have abided by the Stevens Honor System.
@author: Kai Qi Chee
username: kchee
'''

from cs115 import map, reduce
import math

def inverse(n):
    "moves n from the numerator to denominator"
    result=1/n
    return result

def add(x,y):
    "add x and y"
    return x+y

def multiply(x,y):
    "multiply x and y"
    return x*y

def fact(x):
    "take the factorial of x"
    result=reduce(multiply,list(range(1,x+1)))
    return result

def e(x):
    "taylor expansion with x values"
    y=list(range(1,x+1))
    q=map(fact,y)
    z=map(inverse,q)
    result=1+reduce(add,z)
    return result

def error(x):
    "shows error between e(x) and actual e"
    result=abs(math.e-e(x))
    return result

