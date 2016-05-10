# -*- coding: utf-8 -*-
"""
Created on Tue May 10 14:49:18 2016

@author: ylim
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
b = [];

for num in a:
    if ( num  < 5):
        b.append(num);

for num in b:
    print num;

print([ i for i in [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] if i < 5]) 

usr_in = input("Enter a num: ");
print( [i for i in a if i < usr_in]);