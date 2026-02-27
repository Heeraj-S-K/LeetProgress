class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0
        
        # Process from right to left, excluding the first character ('1')
        # This is because we stop when the string is reduced to "1"
        for i in range(len(s) - 1, 0, -1):
            # Calculate the value at current position including carry
            digit = int(s[i]) + carry
            
            if digit == 1:
                # Number is odd: 1 step to add 1, 1 step to divide by 2
                steps += 2
                carry = 1
            else:
                # Number is even: 1 step to divide by 2
                steps += 1
                # carry remains the same (0 if 0+0, 1 if 1+1)
                
        # If there's a final carry at the first position, it adds one more division
        return steps + carry

