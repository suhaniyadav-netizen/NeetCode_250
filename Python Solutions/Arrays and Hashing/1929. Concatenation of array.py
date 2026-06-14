from git import List

# Approach 1 :
# Simple logic of iterating through the list, adding the elements to the ans list and then re-adding
# the original list to the ans list.

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            ans += [nums[i]]
        return ans+nums   
    
# Approach 2 :
# Simple built in logic 

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums+nums   #( or nums*2 )
    
# Approach 3 : 
# If bulit-in functions not allowed

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []

        for x in nums:
            ans.append(x)

        for x in nums:
            ans.append(x)

        return ans
    
    
    