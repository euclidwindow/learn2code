# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# You must write an algorithm that runs in O(n) time and without using the division operation.

# SOLUTION 1
# TC: O(n), SC: O(n)

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    left = [1] * n
    for i in range(1, n):
      left[i] = left[i-1] * nums[i-1]
    
    right = [1] * n
    for i in range(n-2, -1, -1):
      right[i] = right[i+1] * nums[i+1]

    
    output = []
    for i in range(n):
      output.append(left[i] * right[i])
    return output
      
