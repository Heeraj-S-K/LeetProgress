class Solution:
    def searchInsert(self, nums, target):
        # Initialize the search range
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            # Calculate the middle index
            mid = (left + right) // 2
            
            if nums[mid] == target:
                # Target found, return its index
                return mid
            elif nums[mid] < target:
                # Target is in the right half
                left = mid + 1
            else:
                # Target is in the left half
                right = mid - 1
        
        # If target is not found, 'left' points to the correct insertion index
        return left

