class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def hours_taken_with_velocity(array, velocity):
            turns = 0
            for num in array:
                turns += num // velocity
                if num % velocity > 0:
                    turns += 1

            return turns


        low = 1
        high = max(piles)

        while low < high:
            middle = low + ((high - low) // 2)

            middle_result = hours_taken_with_velocity(piles, middle)
            if middle_result > h:
                low = middle + 1
            else:
                high = middle

        return low



            
        