#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 19:12:54 2020

@author: yangsong
"""

# Given a string s, find the length of the longest substring without repeating characters.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        
        if s=='':
            return 0
        
        else:
            s_list=[x for x in s]
        
            num_list=[]

            for i in range(len(s_list)):
                temp_list=[]
                for x in s_list[i:]:
                
                    
                    if x not in temp_list:
                        temp_list.append(x)
                        
                        if len(temp_list)==len(s_list[i:]):
                            num=len(temp_list)
                            num_list.append(num)
        
                    else:
                        num=len(temp_list)
                        num_list.append(num)
                        break
            
            return max(num_list)