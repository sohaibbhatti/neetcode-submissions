class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [] 
        suffix = []

        i = 0
        total = 1
        while i < len(nums):
            
            if len(prefix) == 0:
                prefix.append(total)
            else:
                idx = i - 1
                total = total * nums[idx]
                prefix.append(total)
            i += 1

        i = len(nums) - 1
        total = 1
        while i >= 0:
            if len(suffix) == 0:
                suffix.insert(0, total)
            else:
                idx = i + 1
                total = total * nums[idx]
                suffix.insert(0, total)
            i -= 1

        
        i = 0
        while i < len(prefix):
            prefix[i] = prefix[i] * suffix[i]
            i += 1

        return prefix

        