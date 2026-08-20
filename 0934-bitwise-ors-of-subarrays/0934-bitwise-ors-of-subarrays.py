class Solution:
    def subarrayBitwiseORs(self, arr: list[int]) -> int:
        # Global set to store all unique bitwise OR results found so far
        ans = set()
        
        # Set to track bitwise OR results of subarrays ending at the current index
        current_or_set = set()
        
        for x in arr:
            # Generate new OR values ending at the current element x
            current_or_set = {val | x for val in current_or_set} | {x}
            
            # Merge these results into our global collection
            ans.update(current_or_set)
            
        return len(ans)
