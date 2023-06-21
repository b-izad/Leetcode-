'''Finding the peak:'''
def find_peak(self, nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:  # peak point is in the second half
            left = mid + 1
        else:  # peak point is in the first half or at mid point
            right = mid
    return left


'''finding the Pivot point in rotated array:'''
def find_pivot(self, nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:  # pivot point is in second half
            left = mid + 1
        else:  # pivot point is in first half or mid point
            right = mid
    return left
