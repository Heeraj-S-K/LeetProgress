class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        # 'k' is the index where we place the next unique element
        k = 1
        
        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # If current element is different from the last unique one
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
                
        return k

