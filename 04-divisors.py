# -*- coding: utf-8 -*-
"""
Created on Tue May 10 15:08:16 2016

@author: ylim
"""


num_in = input("Enter a num: ");
num_in = int(num_in);

div = num_in;
list_div = [];


while (num_in > 0 and div > 0):
    if (num_in % div == 0):
        list_div.append(div);
    
    div -= 1;
        
print([i for i in list_div])