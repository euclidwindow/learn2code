# check if a given string is a valid palindrome
# after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters

# SOLUTION 1 : USING TWO POINTERS
# TC: O(n), SC: O(1)

class Solution:
    def isPalindrome(self, s: str) -> bool:   
        left = 0
        right = len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1

        return True

