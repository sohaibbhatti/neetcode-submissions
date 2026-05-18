class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq_mapping = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for num, freq in count.items():
            freq_mapping[freq].append(num)

        result = []
        for i in range(len(freq_mapping) - 1, -1, -1):
            for num in freq_mapping[i]:
                result.append(num)
                if len(result) == k:
                    return result



        

        