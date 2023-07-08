# check if given two input words are anagrams of each other.

# TC: O(n log n)
# SC : O(n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True
