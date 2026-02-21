class Solution:
    def countBinarySubstrings(self, s):
        # Step 1: Count consecutive groups
        groups = []
        if not s:
            return 0
        
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                groups.append(count)
                count = 1
        groups.append(count) # Don't forget the last group
        
        # Step 2: Sum the minimum of adjacent groups
        total_substrings = 0
        for i in range(1, len(groups)):
            total_substrings += min(groups[i-1], groups[i])
            
        return total_substrings

