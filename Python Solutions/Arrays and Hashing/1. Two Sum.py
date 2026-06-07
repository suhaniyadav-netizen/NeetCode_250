# Given an array of integers nums and an integer target, return the indices i and j such that
# nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.

# Example 1:
# Input: 
# nums = [3,4,5,6], target = 7
# Output: [0,1]

# Example 2:
# Input: nums = [4,5,6], target = 10
# Output: [0,2]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in dict :
                return [dict[compliment],i]
            dict[nums[i]] = i 
             

# Time Complexity: O(n)
# Space Complexity: O(n)             

