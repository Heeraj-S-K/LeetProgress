class Solution:

    def thirdMax(self, nums: list[int]) -> int:
        # Initialize three pointers with negative infinity
        first = second = third = float("-inf")

        for num in nums:
            # Skip duplicate numbers to ensure distinct values
            if num in (first, second, third):
                continue

            # Update pointers based on the value of num
            if num > first:
                first, second, third = num, first, second
            elif num > second:
                second, third = num, second
            elif num > third:
                third = num

        # If third maximum does not exist, return the first maximum
        return third if third != float("-inf") else first
