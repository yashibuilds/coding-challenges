"""
Given an input string s, reverse the order of the words.
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        words_lst = s.split()  
        reverse_words_lst = words_lst[::-1]
        return " ".join(reverse_words_lst)