
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 14:42:38 2022

@author: yuhs19
"""

lst = []
f = open("C:/Users/yuhs19/Downloads/p067_triangle.txt", 'r')

for i in f:
    ls = i.split()
    
    lst00 = []
    for j in ls:
        lst00.append(int(j))
        
    lst.append(lst00)
f.close()
        

for i in range(len(lst)):
    for j in range(len(lst[len(lst)-i-1])-1):
        #print(j)
        if lst[len(lst)-i-1][j] > lst[len(lst)-i-1][j+1]:
            lst[len(lst)-i-2][j] += lst[len(lst)-i-1][j]
        else:
            lst[len(lst)-i-2][j] += lst[len(lst)-i-1][j+1]
            
            
print(lst[0][0])
