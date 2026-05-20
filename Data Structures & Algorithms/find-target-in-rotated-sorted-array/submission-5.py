class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        hi = len(nums) - 1

        while low < hi:
            middle = low + ((hi - low) // 2)

            if nums[middle] > nums[hi]:
                low = middle + 1
            else:
                hi = middle
            
        pivot = low

        print(pivot)


        def binary_search(nums, low, hi, target):
            print("i am in here")
            while low <= hi:
                middle = low + ((hi - low) // 2)

                if nums[middle] == target:
                    return middle
                elif nums[middle] < target:
                    low = middle + 1
                else:
                    hi = middle - 1

            return -1

      
        left_search = binary_search(nums, 0, pivot - 1, target)
        if left_search >= 0:
            return left_search

        right_search = binary_search(nums, pivot, len(nums) - 1, target)
        return right_search
        
        