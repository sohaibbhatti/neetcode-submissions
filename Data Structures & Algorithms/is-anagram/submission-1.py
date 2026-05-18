class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        character_mappings = {}

        for char in s:
            character_mappings[char] = character_mappings.get(char, 0) + 1

        for char in t:
            if char not in character_mappings:
                return False
            else:
                character_mappings[char] = character_mappings[char] - 1


        for x in character_mappings.values():
            if x !=0:
                return False

        return True
        