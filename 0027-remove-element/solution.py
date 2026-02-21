class Solution:
    def removeElement(self, nums, val):
        # 'k' is the write pointer for elements not equal to 'val'
        k = 0
        
        # Iterate through every element in the array
        for i in range(len(nums)):
            # If the current element is NOT the value we want to remove
            if nums[i] != val:
                # Move it to the 'k' position and increment 'k'
                nums[k] = nums[i]
                k += 1
                
        # k represents the number of elements kept
        return k

