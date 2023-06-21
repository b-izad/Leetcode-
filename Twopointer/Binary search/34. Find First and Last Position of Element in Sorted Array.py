'''   34. Find First and Last Position of Element in Sorted Array


If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]       '''


def searchRange(self, nums, target):
      result = [-1, -1]

      result[0] = self.find(nums, target, True)
      result[1] = self.find(nums, target, False)

      return result
def find(self, nums, target,findFirst):
        start = 0
        end= len(nums)-1
        
        index = -1
        while start <= end:
            middle = start + (end - start) // 2
            
            if nums[middle] == target:
                index = middle
            
                if findFirst :
                    end = middle -1
                else: 
                    start = middle +1
            
            elif target < nums[middle]:
                end = middle - 1
            else:
                start = middle + 1
        
        return index
                    
                
        
