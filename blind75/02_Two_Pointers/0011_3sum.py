"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""

# SOLUTION 1 - BRUTE FORCE (Time Limit Exceeded error)
# TC: O(n^3), SC:O(1)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if i != j and i !=k and j != k and nums[i] + nums[j] + nums[k] == 0:
                        triplet = sorted([nums[i],nums[j],nums[k]])
                        if triplet not in output:
                            output.append(triplet)
        return output


# SOLUTION 2 - TWO POINTER
# TC: O(n^2), SC:O(1)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSum(nums, i, output)
        
        return output
    
    def twoSum(self, nums: List[int], i: int, output: List[List[int]]):
        lo = i + 1
        hi = len(nums) - 1
        while lo < hi:
            triplet = nums[i] + nums[lo] + nums[hi]
            if triplet < 0:
                lo += 1
            elif triplet > 0:
                hi -= 1
            else:
                output.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1

# SOLUTION 3 - SET
# TC: O(n^2), SC:O(n)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        dups = set()
        seen = {}
        
        for i, n1 in enumerate(nums):
            if n1 not in dups:
                dups.add(n1)
                for j, n2 in enumerate(nums[i+1:]):
                    complement = -n1 - n2
                    if complement in seen and seen[complement] == i:
                        triplet = sorted([n1, n2, complement])
                        if triplet not in output:
                            output.append(triplet)
                    seen[n2] = i
        return output
                
                
