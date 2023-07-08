# check if there any duplicates in a given int array

####################################################################
# PYTHON3
# Solution 1 = SORTING ; TC: O(n log n), SC: O(1)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)):
            if i+1 < len(nums) and nums[i] == nums[i+1]:
                return True
        return False

# Solution 2 = USE SETS ; TC: O(n), SC : O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False


OR

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
