"""
76. Minimum Window Substring

Given two strings s and t of lengths m and n respectively, 
return the minimum window substring of s such that every character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?
"""

# SLIDING WINDOW

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # load pattern t to a hashmap
        freqmap = {}
        for c in t:
            freqmap[c] = freqmap.get(c, 0) + 1
        
        # parse the bigger string
        start = 0
        charmatch = 0
        
        min_length = len(s) + 1
        sub_start = 0
        for end in range(len(s)):
            right_char = s[end]
            if right_char in freqmap:
                freqmap[right_char] -= 1
                if freqmap[right_char] >= 0: charmatch += 1
            
            # check if pattern matched
            while charmatch == len(t):
                if min_length > end - start + 1:
                    min_length = end - start + 1
                    sub_start = start
                
                # slide window
                left_char = s[start]
                if left_char in freqmap:
                    if freqmap[left_char] == 0: charmatch -= 1
                    freqmap[left_char] += 1
                start += 1
        print(min_length)      
        if min_length > len(s): return ""
        return s[sub_start : sub_start + min_length]
