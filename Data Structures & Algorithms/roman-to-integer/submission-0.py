class Solution:
    def romanToInt(self, s: str) -> int:
        ref = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        
        for i in range(len(s) - 1):
            # If the current value is less than the next, it's a subtractive case
            if ref[s[i]] < ref[s[i + 1]]:
                result -= ref[s[i]]
            else:
                result += ref[s[i]]
                
        # Always add the very last character
        result += ref[s[-1]]
        return result
