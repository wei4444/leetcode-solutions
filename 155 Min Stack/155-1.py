class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.val = []
        self.minIdx = []

    def push(self, x: int) -> None:
        if(len(self.minIdx) == 0):
            self.minIdx.append(len(self.val))
        elif(self.val[self.minIdx[-1]] > x):
            self.minIdx.append(len(self.val))
        self.val.append(x)

    def pop(self) -> None:
        if(len(self.val)-1 == self.minIdx[-1]):
            self.minIdx.pop()
        self.val.pop()

    def top(self) -> int:
        return self.val[-1]

    def getMin(self) -> int:
        return self.val[self.minIdx[-1]]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()