# -*- coding: utf-8 -*-
"""
Created on Tue May 10 15:51:38 2016

@author: ylim

Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:

    (1) Randomly generate two lists to test this
    (2) Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

"""
import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
  
print([i for i in a if i in b])

c = []
d = []

#(1)
i = random.randrange(10, 20, 1)
j = random.randrange(10, 20, 1)

while (i > 0):
    i -= 1;
    c.append(random.randrange(1, 200))

while (j > 0):
    j -= 1;
    d.append(random.randrange(1, 200))
    

print c, d

#(2)
print([i for i in c if i in d])