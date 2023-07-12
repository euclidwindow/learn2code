# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

"""
Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""

# SOLUTION 1 : USE SORT + SET
# TC: O(N logn) , SC: O(n)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
            
        nums = list(set(nums))
        nums.sort()
        max_len = 1
        curr_max_len = 1
        for i in range(0, len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                curr_max_len += 1
            else:
                curr_max_len = 1
            
            if curr_max_len > max_len:
                max_len = curr_max_len
        return max_len

# SOLUTION 2 : SET
# TC: O(n), SC: O(n)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        numset = set(nums)
        
        for n in nums:
            if n-1 not in numset:
                curr_max_len = 1
                curr_num = n
                
                while curr_num + 1 in numset:
                    curr_num += 1
                    curr_max_len += 1
                
                if curr_max_len > max_len:
                    max_len = curr_max_len
                
        return max_len
