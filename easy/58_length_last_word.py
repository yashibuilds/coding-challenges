"""
Given a string s consisting of words and spaces, return the length of the last word in the string.
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        words_lst = s.split()
        return len(words_lst[-1])