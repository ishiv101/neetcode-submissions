class Solution:
    from collections import defaultdict
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        counter: dict[str, int] = defaultdict(int) # our window is basically counter
        for right in range(len(s)):
            counter[s[right]] += 1
            while counter[s[right]] > 1:
                counter[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest
            




        