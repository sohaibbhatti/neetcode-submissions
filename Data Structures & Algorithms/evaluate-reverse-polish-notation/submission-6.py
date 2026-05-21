class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            try:
                value = int(token)
                stack.append(value)
            except ValueError:
                
                num2 = stack.pop()
                num1 = stack.pop()

                if token == "+":
                    ans = num1 + num2
                elif token == "-":
                    ans = num1 - num2
                elif token == "/":
                    ans = int(float(num1) / num2)
                elif token == "*":
                    ans = num1 * num2
                
                stack.append(ans)

        return stack.pop()
        