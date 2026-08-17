class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #dont use sets because it disregrads duplicate letters
        #dont use character int values because different characters can add up to the same number

        dicty = {} #keys cannot be muttable
        # key = tuple, value = list

        result = []

        for word in strs:
            empty = []
            for char in word:
                empty.append(char)
            check = tuple(sorted(empty))
            if check in dicty:
                dicty[check].append(word)
            else:
                dicty[check] = [word]

        for val in dicty.values():
            result.append(val)
        
        return result