class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        hi = len(nums) - 1

        while low <= hi:
            middle = low + ((hi - low) // 2)

            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                low = middle + 1
            else:
                hi = middle - 1

        return -1


        