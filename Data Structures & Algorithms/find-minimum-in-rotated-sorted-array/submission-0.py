class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        hi = len(nums) - 1

        while low < hi:
            mid = low + ((hi - low) // 2)

            if nums[mid] < nums[hi]:
                hi = mid
            else:
                low = mid + 1

        return nums[hi]