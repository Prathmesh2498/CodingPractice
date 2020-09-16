# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 16:45:09 2020

@author: Admin
"""

  Group Anagrams

Solution
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        dict_all={}
        
        for s in strs:
                
            if ''.join(sorted(s)) not in dict_all:
                dict_all[''.join(sorted(s))]=[]
                
            dict_all[''.join(sorted(s))].append(s)

        return list(dict_all.values())

        """
        if (len(strs)==0):
            return [[""]]
        elif(strs[0] == "" and len(strs)==1):
            return [[""]]
        elif(strs[0] == "" and strs[1]=="" and len(strs)==2):
            return [["",""]]
        elif(len(strs) == 1):
            return [[strs[0]]]
        
        res = [[strs[0]]]
        flag = False
        sorteda = ["".join(sorted(strs[0]))]
        print(sorteda)
        for i in range(1, len(strs)):
            if(i == ""):
                s = strs[i]
            else: 
                s = "".join(sorted(strs[i]))
            flag = False
            for j in range(len(res)):
                t = sorteda[j]
                if s == t:
                    flag = True
                    res[j].append(strs[i])
                        
            if flag==False:
                res.append([strs[i]])
                sorteda.append("".join(sorted(strs[i])))
        return res
        """
