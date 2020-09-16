# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 11:46:01 2020

@author: Admin
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        if (len(s)<=0):
            return 0
        flag = False
        num = ""
        sign = 1
        signctr = 0
        for i in list(s):
            #Check white spaces at start
            if(ord(i)==32 and flag == False):
                continue
            #Flag indicates all whitespaces at the beginning are checked
            flag = True
            
            #Check sign, also the signctr is for (+*-*) case -_-
            if(i == '-' and signctr == 0):
                if(num==""):
                    sign = -1
                    signctr += 1
                    continue

            if(i=='+' and signctr == 0):
                if(num == ""):
                    signctr += 1
                    continue

            
            #If first char after space is not a number, return only if it is the first char
            if( not(48<=ord(i) and ord(i)<=57) and (flag == True)):
                if (num==""):
                    return 0
                else:
                    break
            #Add the nos to the number string
            if(48<=ord(i) and ord(i)<=57):
                num = num+str(i)
                
            #Break if first occurence of numbers is processed
            elif( not(48<=ord(i) and ord(i)<=57) and (flag == True)):
                break
            
        if(num!=""):
            t = int(int(num) * int(sign))
            if(t<0 and abs(t)>((2**31)-1)):
                return -2**31
            elif(t>0 and t>((2**31)-1)):
                return 2**31 - 1
            else:
                return t
        else:
            return 0
