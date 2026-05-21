class Solution:
    def isValid(self, s: str) -> bool:
        store = []
        for char in s:
            if char in {"(", "{", "["}:
                store.append(char)
            elif char in { ")", "}", "]"}:
                if len(store) <= 0:
                    return False

                res = store.pop()
                if char == ")" and res != "(":
                    return False

                if char == "}" and res != "{":
                    return False

                if char == "]" and res != "[":
                    return False

        return len(store) == 0
        
            

        