'''215. Kth Largest Element in an Array
Medium

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4'''


from heapq import *
class Solution:
    def findKthLargest(self, nums, k):
        minHeap = []
        
        for i in range(k):
            heappush(minHeap,nums[i])
       
       
        for i in range(k,len(nums)):
            if nums[i]>minHeap[0]:
                heappop(minHeap)
                heappush(minHeap, nums[i])
       
        return minHeap[0]
         