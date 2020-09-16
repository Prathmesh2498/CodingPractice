# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 16:56:24 2020

@author: Admin
"""

Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

 

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i=0
        j=len(s) - 1
        while(i<=j):
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1


#################################################################
            
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


class Solution:
    def reverse(self, x: int) -> int:
        s = -1 if(x<0) else 1       # Controls the sign
        num = int(str(abs(x))[::-1])
        
        if (num > -2147483648 and num < 2147483647):
            return num*s
        else:
            return 0
        
###########################################################
            
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
 

Note: You may assume the string contains only lowercase English letters.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        index = -1
        curr = 0
        limit = len(s)
        s = list(s)
        for i in range(limit):
            t = s.pop(0)
            if(t not in s):
                if(index<0):
                    index = curr
                    break
            s.append(t)
            curr += 1
        return index
    
####################################################
        
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        if(sorted(s) == sorted(t)):
            return True
        
######################################################
            
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
 

Constraints:

s consists only of printable ASCII characters.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        j = len(s) - 1
        s  = list(s)
        while(i<=j):
            intS = ord(s[i])
            intJ = ord(s[j])
            if((intS>=48 and intS<=57) or (intS>=97 and intS<=122)):
                pass
            else:
                i+=1
                continue
            if((intJ>=48 and intJ<=57) or (intJ>=97 and intJ<=122)):
                pass
            else:
                j-=1
                continue
            if(s[i]!=s[j]):
                return False
            i+=1
            j-=1
        return True 
    
#######################################################
        
    
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
             
class Solution:
    def myAtoi(self, s: str) -> int:
        if (len(s)<=0):
            return 0
        flag = False
        num = ""
        sign = 1
        signctr = 0
        l = list(s)
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
#####################################################################
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

 

Constraints:

haystack and needle consist only of lowercase English characters.


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return(haystack.index(needle))
        return(-1)
        
##############################################################
        
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. You can do so recursively, in other words from the previous member read off the digits, counting the number of digits in groups of the same digit.

Note: Each term of the sequence of integers will be represented as a string.

 

Example 1:

Input: 1
Output: "1"
Explanation: This is the base case.
Example 2:

Input: 4
Output: "1211"
Explanation: For n = 3 the term was "21" in which we have two groups "2" and "1", "2" can be read as "12" which means frequency = 1

class Solution:
    def countAndSay(self, n: int) -> str:
        if(n==1):
            return "1"
        if (n==2):
            return "11"
        if (n==3):
            return "21"
        
        l = ["1", "11", "21"]
        answer = ""
        prev = "21"
        for i in range(3,n):
            lprev = list(prev)
            frequency = 1
            currindex = 0
            answer = ""
            while(currindex<len(lprev)):
                if(currindex+1<len(lprev)):
                    if(lprev[currindex] == lprev[currindex+1]):
                        frequency+=1
                        currindex+=1
                        continue
                
                answer = answer + str(frequency) + lprev[currindex]
                frequency = 1
                currindex+=1
            prev = answer
        return answer

###############################################################
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(len(strs) == 0):
            return ""
        if(len(strs) == 1):
            return strs[0]
        lens = [len(i) for i in strs]
        minlen = min(lens)
        
        max = 0
        flag = 0
        for i in range(1, minlen+1):
            count=0
            for j in range(1,len(strs)):
                if(strs[j-1][:i] != strs[j][:i]):
                    break
                if(strs[j-1][:i] == strs[j][:i]):
                    if(count==0):
                        a = strs[j-1][:i]
                        count+=1
                    elif(a!=strs[j][:i]):
                        break
                    if(j+1 == len(strs)):
                        tmax = i
                        flag = 1
            
            if(flag == 1):
                max=tmax
        
        
        return strs[0][:max]