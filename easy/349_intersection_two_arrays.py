"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
"""
class Solution(object):
    def intersection(self, nums1, nums2):
        # len(nums1) = m, len(nums2) = n
        # Time Complexity: O(n+m)
        # Space Complexity: O(n+m)
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))  