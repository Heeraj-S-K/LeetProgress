class Solution(object):
    def longestCommonPrefix(self, strs):
        # If the list is empty, return an empty string
        if not strs:
            return ""
        
        # Sort the strings alphabetically
        strs.sort()
        
        # Take the first and the last strings
        first = strs[0]
        last = strs[-1]
        
        result = ""
        # Compare the first and last string character by character
        for i in range(len(first)):
            # If characters match and we haven't exceeded 'last' length
            if i < len(last) and first[i] == last[i]:
                result += first[i]
            else:
                # Break at the first mismatch
                break
                
        return result

