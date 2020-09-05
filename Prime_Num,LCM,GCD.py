# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 14:55:58 2020

@author: Admin
"""

#Finding GCD and LCM -- cause why not :P
import math
def gcd(x,y):
    i = 1
    gcd = 1
    while(x%i==0 and y%i==0):
        gcd = i
        i = i+1
        
    return gcd

def lcm(x,y):
    return int((x*y)/gcd(x,y))    

#Find prime factors of a number
"""
1. Every composite number has at least one prime factor less than or equal to square root of itself.
This property can be proved using counter statement. Let a and b be two factors of n such that a*b = n. 
If both are greater than √n, then a.b > √n, * √n, which contradicts the expression “a * b = n”.
Src: https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/
"""
def prime_factors(x):
    factors = []
    while(x%2==0):
        factors.append(2)
        
    for i in range(3, int(math.sqrt(x)), 2): #1
        if (x%i == 0):
            factors.append(i)
        x = x/i #Remove occurences of i from n
            
    return factors
    
if __name__ == '__main__':
    print(prime_factors(315))
    print(lcm(5,7))