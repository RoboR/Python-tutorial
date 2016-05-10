# -*- coding: utf-8 -*-
"""
Created on Tue May 10 17:37:04 2016

@author: ylim

Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

    Keep the game going until the user types “exit”
    Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""
import random


usr_input = str();
#usr_input = raw_input("Guess a number (1-9), \"exit\" to Quit: ")
   
while ( usr_input != "exit" ):
    num = random.randrange(1, 9, 1)    
    guess = 0;
    print num
    
    usr_input = input("Guess a number (1-9), \"exit\" to Quit: ")
    
    while ( usr_input  != "exit" and int(usr_input) != num):
        if ( int(usr_input) > num):
            print("Too High")
        else:
            print("Too Low")
              
        guess += 1
        usr_input = raw_input("Guess a number (1-9), \"exit\" to Quit: ")
    
    print("You got it right with ", guess, " guesses")