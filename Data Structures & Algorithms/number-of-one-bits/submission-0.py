class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for digit in bin(n):
            if digit == "1":
                count += 1
        
        return count