class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        # Iterate from the last digit back to the first
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If digit is 9, it becomes 0 and carry continues
            digits[i] = 0
        
        # If we reach here, the number was all 9s (e.g., [9, 9] -> [1, 0, 0])
        return [1] + [0] * n

