# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# SOLUTION 1 - USING HEAP
# TC: O(N+k), SC: O(n + k)
# FASTEST (98% faster)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # TC: O(1)
        if k == len(nums):
            return nums
        
        # build hashmap for each numbers and its frequency
        # TC: O(N)
        # SC: O(n)
        freqmap = {}
        for n in nums:
            if n in freqmap.keys():
                freqmap[n] += 1
            else:
                freqmap[n] = 1
        
        # build heap of top k frequent elements
        # and convert it to output array
        # TC: O(N log k)
        # SC: O(k)
        return heapq.nlargest(k, freqmap.keys(), key=freqmap.get)

# SOLUTION 2 - BUCKET SORT
# TC: O(N), SC: O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        bucket = []
        for _ in range(len(nums) + 1):
            bucket.append([])
        
        # make a frequency hahsmap
        freqmap = {}
        for n in nums:
            if n in freqmap.keys():
                freqmap[n] += 1
            else:
                freqmap[n] = 1
        
        # populate bucket
        for n, freq in freqmap.items():
            bucket[freq].append(n)
        
        # convert bucket to list
        flat_list = []
        for sublist in bucket:
            for n in sublist:
                flat_list.append(n)
        return flat_list[::-1][:k]
