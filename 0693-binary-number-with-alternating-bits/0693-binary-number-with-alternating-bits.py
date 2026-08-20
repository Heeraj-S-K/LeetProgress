class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # Shift and XOR to see if it creates a continuous block of 1s
        xor_result = n ^ (n >> 1)
        
        # Check if xor_result + 1 clears all bits when ANDed with xor_result
        return (xor_result & (xor_result + 1)) == 0
