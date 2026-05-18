class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        longest = 0

        for num in store:
            if (num - 1) in store:
                continue

            length = 1
            while (num + length) in store:
                length += 1
            longest = max(length, longest)

        return longest

        