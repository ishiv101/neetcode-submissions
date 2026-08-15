class Solution:
    def hammingWeight(self, n: int) -> int: #n is already a unsigned int
        count = 0
        while n: #auto stops when n == 0
            n = n & (n-1)
            count += 1

        
        return count