"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
"""

# stack : tc: O(n), sc: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        p_map = {}
        p_map['}'] = '{'
        p_map[']'] = '['
        p_map[')'] = '('

        stack = []
        for c in s:
            if c in p_map.values():
                stack.append(c)
            elif len(stack) > 0 and stack[-1] == p_map[c]:
                stack.pop()
            else:
                return False
        return len(stack) == 0

