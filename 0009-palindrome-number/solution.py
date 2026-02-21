class Solution(object):
    def isPalindrome(self, x):
        # Handle negatives and numbers ending in 0 (except 0 itself)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
            
        res = 0
        original = x
        while x > 0:
            res = (res * 10) + (x % 10)
            x //= 10
            
        return res == original

