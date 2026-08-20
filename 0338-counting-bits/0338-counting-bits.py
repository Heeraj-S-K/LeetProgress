class Solution:
    def countBits(self, n: int) -> list[int]:
        # Initialize the DP array with zeros
        ans = [0] * (n + 1)
        
        # Populate the array using the relation: ans[i] = ans[i & (i - 1)] + 1
        for i in range(1, n + 1):
            ans[i] = ans[i & (i - 1)] + 1
            
        return ans
