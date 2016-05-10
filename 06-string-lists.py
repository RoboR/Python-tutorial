# -*- coding: utf-8 -*-
"""
Created on Tue May 10 16:06:40 2016

@author: ylim

Ask the user for a string and print out whether this string is a palindrome or not.
    (A palindrome is a string that reads the same forwards and backwards.)
"""

str_in = list(raw_input("Enter a string: "))
#str_list.append([a for a in str_in])

str_rev = list(str_in);
str_rev.reverse();

if (cmp(str_in, str_rev) == 0):
    print("The string entered is a palindrome")
else:
    print("The string entered is not a palindrome")