"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achive this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""

# SLIDING WINDOW

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        max_length = 0
        freqmap = {}
        max_repeat = 0
        
        for end in range(len(s)):
            rightchar = s[end]
            if rightchar not in freqmap:
                freqmap[rightchar] = 1
            else:
                freqmap[rightchar] += 1
            max_repeat = max(max_repeat, freqmap[rightchar])
            
            # slide window criteria
            window_size = end - start + 1
            if window_size - max_repeat > k:
                leftchar = s[start]
                freqmap[leftchar] -= 1
                if freqmap[leftchar] == 0: 
                    del freqmap[leftchar]
                start += 1
            
            window_size = end - start + 1
            max_length = max(max_length, window_size)
        return max_length
