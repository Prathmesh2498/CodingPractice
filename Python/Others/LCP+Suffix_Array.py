# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 10:46:44 2020

@author: Admin
"""
#Suffix Array and LCP Array

class suffix:
    @staticmethod
    def build_suffix_array(s=" "):
        arr = [] 
        if(s==" "):
            return "Sring is Empty!"
        for i in range(1, len(s)):
            for j in range(i + 1, len(s) + 1):
                temp = s[i: j]
                if (temp not in arr):
                    arr.append(temp)
                 
                        
        arr.sort()
        return arr
        
    @staticmethod    
    def build_LCP_array(arr = []):
        lcp = [0]
        maxValue = 0
        for i in range(len(arr)-1):
            maxValue = 0
            temp = 0
            one = 1
            j = 2
            s1 = arr[i]
            s2 = arr[i+1]
            while (s1[one:j] == s2[one:j]):
                temp+=1
                if(maxValue<temp):
                    maxValue = temp
                j+=1
                
            lcp.append(maxValue)
        
        return lcp

        
#Main for suffix array and lcp
s = "ABABBAB"

arr_suffix = suffix.build_suffix_array(s)
print(arr_suffix)

arr_lcp = suffix.build_LCP_array(arr_suffix)
print(arr_lcp)