'''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if not nums:
            return -1

        pivot = self.find_pivot(nums)
        if nums[pivot] == target:
            return pivot
        if nums[0] <= target:  # target is in the left part
            return self.binary_search(nums, 0, pivot-1, target)
        else:  # target is in the right part
            return self.binary_search(nums, pivot+1, len(nums)-1, target)
    
    def find_pivot(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:  # pivot point is in second half
                left = mid +1
            else:  # pivot point is in first half or mid point
                right = mid
        return left
    
    def binary_search(self, nums, left, right, target):
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
