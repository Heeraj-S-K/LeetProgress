class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        
        # Slide the window across the haystack
        # We only need to go up to n - m + 1
        for i in range(n - m + 1):
            # Check if the substring starting at i matches needle
            if haystack[i : i + m] == needle:
                return i
        
        # If no match is found
        return -1

