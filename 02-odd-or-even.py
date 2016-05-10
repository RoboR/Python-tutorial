# -*- coding: utf-8 -*-
"""
Created on Tue May 10 14:05:57 2016

@author: ylim
"""

num_i = input("Enter a number: ")

if (num_i % 4 == 0):
    print ("Special case")
    
elif ( num_i % 2 == 0):
    print ("Even case")
    
else:
    print ("Odd")


num = input("Enter a num: ")
check = input("Enter check number: ")

if (num % check == 0):
    print(str(num) + " is able to divide by " + str(check))
else:
    print(num, " is not able to divide by ", check)