class Solution(object):
    def countPrimeSetBits(self, left, right):
        # Primes up to 20 (since 2^20 > 10^6)
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        ans = 0
        
        for i in range(left, right + 1):
            # Using bin().count('1') for maximum compatibility across Python versions
            if bin(i).count('1') in primes:
                ans += 1
                
        return ans

