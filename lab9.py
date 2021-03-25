'''
Edited on October 30, 2019
fibonacci by Kai Qi Chee
Pledge: I pledge my honor that I have abided by the Stevens Honor System.

cs 115-lab9
'''

# Demo of hmmm, the Harvey Mudd miniature machine
# D.N. Oct 2018

# When this file is loaded, it runs the program assigned
# to variable RunThis. Debug mode is controlled by 
# variable Mode. Read all the comments before trying it out.

import sys
import importlib
# Also requires hmmmAssembler.py and hmmmSimulator.py to
# be available in the same directory as this file.


# Example1 is an example program that
#   1) asks the user for two inputs
#   2) computes the product of the inputs
#   3) prints out the result (with write)
#   4) stops

Example1 = """
00 read r1          # get # from user to r1
01 read r2          # ditto, for r2
02 mul r3 r1 r2     # r3 = r1 * r2
03 write r3         # print what's in r3
04 halt             # stop.
"""


# Example2 is an example program that
#   1) asks the user for an input
#   2) counts up from that input
#   3) keeps going and going...

Example2 = """
00 read r1          # get # from user to r1
01 write r1         # print the value of r1
02 addn r1 1        # add 1 to r1
03 jumpn 01         # jump to line 01
04 halt             # never halts! [use ctrl-c]
"""

# StoreLoad is an example program that
#   1) asks the user for an input
#   2) stores the value in a memory location
#   3) increments it and stores in another location
#   4) loads from that location and writes that value
# Try changing 11 to the address of an instruction!

StoreLoad = """
00 read r1         
01 storen r1 11   # put the value into mem[11]
02 addn r1 1       
03 setn r2 13 
04 storer r1 r2   # put incremented value into mem[13]
05 loadn r1 13
06 write r1       # write what was loaded
07 halt
"""

# Triangle1 calculates the area of triangle with base and height
Triangle1 = """
00 read  r1          # get base
01 read  r2          # get height
02 mul   r1 r1 r2    # b times h into r1
03 setn  r2 2
04 div   r1 r1 r2    # divide by 2
05 write r1
06 halt
"""

# This factorial version computes factorial without calliong a function
Factorial = """
# Input: n
# Assume: n >= 0
# Output: n!
#

# register usage: r1 for the input, r13 for the output

0       read    r1         # Get n
1       setn    r13  1     # set r13 to 1
2       jeqzn   r1 6       # done if r1 is 0
3       mul     r13 r13 r1 # change r13 = r13 * r1
4       addn    r1 -1      # change r1 = r1 - 1
5       jumpn   2          # repeat
6       write   r13
7       halt
""" 

# This factorial version calls factorial function from main but still uses
# loop to calculate factorial
FactorialCall = """
# Input: n 
# Assume: n >= 0
# Output: n!
#

# register usage: r1 for the input, r13 for the output

0       read    r1         # Get n
1       calln   r14 4      # jump to factorial function
2       write   r13        # print r13
3       halt
4       setn    r13 1      # initialize r13 (start of factorial function)
5       jeqzn   r1 9       # done if r1 is 0
6       mul     r13 r13 r1 # change r13 = r13 * r1
7       addn    r1 -1      # change r1 = r1 - 1
8       jumpn   5          # repeat
9       jumpr   r14        # return (end of factoral function)
"""

FunctionParamExample = """
0     setn r15 26      # initialize stack pointer
1     read r1          # Get r1 value from input
2     storer r1 r15    # next 2 statements push r1 onto stack
3     addn r15 1
4     calln r14 10     # call emma function with param r1
5     addn r15 -1      # next 2 statements pop r1 from stack
6     loadr r1 r15
7     add r13 r13 r1   # add r1 to r13
8     write r13        # print r13
9     halt
10    addn r1 1        # add 1 to r1 (start of emma function)
11    storer r1 r15    # next 2 statements push r1 onto stack
12    addn r15 1
13    storer r14 r15   # next 2 statements push return addr onto stack
14    addn r15 1
15    call r14 22      # call sarah function with param r1
16    addn r15 -1      # next 2 statemnents pop return address from stack onto r14
17    loadr r14 r15
18    addn r15 -1      # next 2 statements pop r1 value from stack
19    loadr r1 r15
20    add r13 r13 r1  # add r1 to r13 
21    jumpr r14       # return from emma function (end of emma function)
22    addn r1 42       # add 42 to r1 (start of sarah function)
23    setn r2 1        # next 2 statements set r3 to r1 + 1
24    add  r13 r1 r2
25    jumpr r14        # return from sarah function (end of sarah function)
"""

fibonacci = """
00 read r1        #get input from user to r1
01 jeqzn r1 12    #if r1 is 0, jump to line 12
02 setn r5 1      # set r5 to 1
03 setn r2 0      #set r2 to 0
04 setn r3 1      # set r3 to 1
05 copy r4 r3     # set r4 to r3
06 write r2       #print the contents of r2
07 sub r1 r1 r5   #set r1 to r1-r5
08 add r4 r2 r3   #set r4 to r2+r3
09 copy r2 r3     #set r2 to r3
10 copy r3 r4     #set r3 to r4
11 jnezn r1 6     #if r1 is 0, jump to line 6
12 halt           #stop the program
"""

# Set this variable to whichever program you want to execute
# when this file is loaded.
RunThis = fibonacci

# Choose whether to use debug mode; uncomment one of the following lines.
#Mode = ['-n'] # not debug mode
Mode = ['-d'] # debug mode
#Mode = []     # prompt for whether to enter debug mode


# When you press F5 in IDLE, the following code will
# load the assembler and simulator, then run them.
# You can interrupt with Ctrl-C; then re-start Python.

if __name__ == "__main__" : 
    import hmmmAssembler ; importlib.reload(hmmmAssembler)
    import hmmmSimulator ; importlib.reload(hmmmSimulator)
    hmmmAssembler.main(RunThis) # assemble input into machine code file out.b
    hmmmSimulator.main(Mode)    # run the machine code in out.b


