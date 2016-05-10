# -*- coding: utf-8 -*-
"""
Created on Tue May 10 17:18:16 2016

@author: ylim

Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock
"""


"""
No input error checking
"""

game_dict = {'rock': 1, 'paper': 2, 'scissors': 3}

while(1):
    player_1 = raw_input("Player 1: ")
    player_2 = raw_input("Player 2: ")

    in_p1 = game_dict.get(player_1);
    in_p2 = game_dict.get(player_2);
    
    diff = in_p1 - in_p2
    
    if (diff in [-2, 1]):
        print("Player 1 wins")
    elif (diff in [-1, 2]):
        print("player 2 wins")
    else:
        print("Is a draw")