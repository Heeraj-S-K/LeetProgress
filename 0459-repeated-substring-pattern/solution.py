class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # 1. Create a doubled version of the string
        doubled_s = s + s
        
        # 2. Remove the first and last character
        # This prevents the original s at the start and end from being matched
        trimmed_s = doubled_s[1:-1]
        
        # 3. If s is in the trimmed string, it's a repeated pattern
        return s in trimmed_s

