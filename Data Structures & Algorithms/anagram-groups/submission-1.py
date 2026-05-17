class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for str in strs:
            mapping = [0] * 26

            for char in str:
                numerical_val = ord(char) - ord('a')
                mapping[numerical_val] = mapping[numerical_val] + 1

            key = tuple(mapping)

            if key in dict:
                dict[key].append(str)
            else:
                dict[key] = [str]


        return list(dict.values())
