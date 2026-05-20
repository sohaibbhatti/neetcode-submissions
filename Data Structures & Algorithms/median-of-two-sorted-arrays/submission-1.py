class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            a = nums2
            b = nums1
        else:
            a = nums1
            b = nums2

        m = len(a)
        n = len(b)


        size_of_left = (m + n) // 2
        if (m + n) % 2 == 1:
            size_of_left += 1

        low = 0
        hi = m

        while low <= hi:
            mid = (low + hi) // 2

            cut_a = mid
            cut_b = size_of_left - cut_a
            
            left_a = a[cut_a - 1] if cut_a > 0 else float('-inf')
            right_a = a[cut_a] if cut_a < m else float('inf')

            
            left_b = b[cut_b - 1] if cut_b > 0 else float('-inf')
            right_b = b[cut_b] if cut_b < n else float('inf')

            if left_a <= right_b and left_b <= right_a:
                if (m + n) % 2 == 1:
                    return max(left_a, left_b)

                else:
                    return (max(left_a, left_b) + min(right_a, right_b)) / 2.0
            elif left_a > right_b:
                hi = mid - 1
            else:
                low = mid + 1


        