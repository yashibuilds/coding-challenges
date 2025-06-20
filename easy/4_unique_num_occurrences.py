"""
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
"""

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        occurrences = {}
        for i in range(len(arr)):
            if arr[i] in occurrences:
                occurrences[arr[i]] += 1
            else:
                occurrences[arr[i]] = 1
        return len(set(occurrences.values())) == len(occurrences)