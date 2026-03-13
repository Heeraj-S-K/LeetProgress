class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort() # Now it's [1, 1, 2, 2, 4]
        
        # Step by 2 to check pairs
        for i in range(0, len(nums) - 1, 2):
            if nums[i] != nums[i + 1]:
                return nums[i]
        
        # If no single number found in pairs, it must be the last one
        return nums[-1]

