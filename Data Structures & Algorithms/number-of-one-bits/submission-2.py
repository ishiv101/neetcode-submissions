class Solution:
    def hammingWeight(self, n: int) -> int: #n is already a unsigned int
        count = 0
        while n: #auto stops when n == 0
            count += n % 2 #n mod 2 returns 1 if last bit is 1 and 0 if last bit is 0
            n = n >> 1 # always shift one bit to the right
        
        return count