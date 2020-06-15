# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 15:47:06 2020

@author: Admin
"""
def checkBalance(exp):
    stack = []
    try:
        for c in exp:
            if (c =='{' or c == '[' or c == '('):
                stack.append(c)
            elif(c == '}' or c == ']' or c == ')'):
                if(len(stack)<1):
                    print("Not a valid string")
                    return
                t = stack.pop()
                if((t == '{' and c=='}') or (t == '[' and c==']') or (t == '(' and c==')')):
                    pass
                else:
                    print("Not a valid string")
                    return
        if(len(stack)!=0):
            print("Invalid string")
            return
        print("Valid String")
    except:
      print ("Error")
            
if __name__ == '__main__':
    s = input("Enter exp: ")
    exp = list(s)
    checkBalance(exp)    