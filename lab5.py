'''
Created on October 1, 2019
@author:   Kai Qi Chee
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Lab 5
'''
import time
from cs115 import map
words = []
HITS = 10

def fastED(first, second):
    '''Returns the edit distance between the strings first and second. Uses
    memoization to speed up the process.'''
    D={}
    def fastED_helper(first,second,dictionary):
        if (first,second) in dictionary:
            return dictionary[(first,second)]
        elif first == '':
            return len(second)
        elif second == '':
            return len(first)
        elif first[0] == second[0]:
            return fastED_helper(first[1:], second[1:],dictionary)
        else:
            substitution = 1 + fastED_helper(first[1:], second[1:],dictionary)
            deletion = 1 + fastED_helper(first[1:], second,dictionary)
            insertion = 1 + fastED_helper(first, second[1:],dictionary)
            result = min(substitution, deletion, insertion)
            dictionary[(first,second)]=result
            return result
    return fastED_helper(first,second, D)

def getSuggestions(user_input):
    '''For each word in the global words list, determine the edit distance of
    the user_input and the word. Return a list of tuples containing the
    (edit distance, word).
    Hint: Use map and lambda, and it's only one line of code!'''
    return map(lambda x: [fastED(user_input, x),x], words)

def spam():
    '''Main loop for the program that prompts the user for words to check.
    If the spelling is correct, it tells the user so. Otherwise, it provides up
    to HITS suggestions.

    To exit the loop, just hit Enter at the prompt.'''
    while True:
        user_input = input('spell check> ').strip()
        if user_input == '':
            break
        if user_input in words:
            print('Correct')
        else:
            start_time = time.time()
            suggestions = getSuggestions(user_input)
            suggestions.sort()
            endTime = time.time()
            print('Suggested alternatives:')
            for suggestion in suggestions[:HITS]:
                print(' %s' % suggestion[1])
            print('Computation time:', endTime - start_time, 'seconds')
    print('Bye')

if __name__ == '__main__':
    f = open('3esl.txt')
    for word in f:
        words.append(word.strip())
    f.close()
    spam()

