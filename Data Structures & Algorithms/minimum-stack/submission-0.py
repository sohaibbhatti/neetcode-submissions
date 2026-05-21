class MinStack:

    def __init__(self):
        self.store = []
        self.min = []
        

    def push(self, val: int) -> None:
        self.store.append(val)
        if not self.min:
            self.min.append(val)
        else:
            self.min.append(min(self.min[-1], val))
       

    def pop(self) -> None:
        self.store.pop()
        self.min.pop()
        

    def top(self) -> int:
        return self.store[-1]
        

    def getMin(self) -> int:
        return self.min[-1]
        
