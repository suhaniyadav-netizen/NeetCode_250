# An anagram is a string that contains the exact same characters as another string, but the order of 
# the characters can be different.

# Example 1:
# Input: s = "racecar", t = "carrace"
# Output: true

# Example 2:
# Input: s = "jar", t = "jam"
# Output: false

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for i in set(s):
            if s.count(i) != t.count(i):
                return False
        return True
    
# Time Complexity: O(n)
# Space Complexity: O(1)    