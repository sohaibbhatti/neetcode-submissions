class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = []

        for index, temp in enumerate(temperatures):
            if not stack:
                stack.append((temp, index))
            else:
                head = stack[-1]

                while head and temp > head[0]:
                    match = head[1]
                    res[match] = index - match
                    stack.pop()
                    head = stack[-1] if len(stack) > 0 else None

                stack.append((temp, index))

        return res
        