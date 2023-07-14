"""
Given a string s, find the length of the longest substring without repeating characters. 

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

# SLIDING WINDOW: TC: O(n), SC: O(1)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        start = 0
        charmap = {}
        for end in range(len(s)):
            c = s[end]
            # slide the sliding window
            if c in charmap:
                start = max(start, charmap[c] + 1)
            max_len = max(max_len, end - start + 1)
            charmap[c] = end
        return max_len
