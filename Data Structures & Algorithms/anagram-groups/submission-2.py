class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create hashmaps grouped by character count
        dicty = {}

        result = []
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            check = tuple(count)

            if check in dicty:
                dicty[check].append(word)
            else:
                dicty[check] = [word]
        
        for val in dicty.values():
            result.append(val)

        return result
            
