class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # Convert string to list since Python strings are immutable
        chars = list(s)
        n = len(chars)
        
        # Loop through the string, jumping 2k steps each time
        for i in range(0, n, 2 * k):
            # The range to reverse is from i up to i + k (capped at string end)
            left = i
            right = min(i + k - 1, n - 1)
            
            # Reverse the selected k characters in place
            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
                
        return "".join(chars)
