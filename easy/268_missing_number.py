"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
"""
class Solution(object):
    def missingNumber(self, nums):
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        """
        :type nums: List[int]
        :rtype: int
        """
        return (len(nums) * (len(nums) + 1)) // 2 - sum(nums)