class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append((val, val))
            return

        min_val = self.stack[-1][1]
        self.stack.append((val, min(min_val, val)))

    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


class MinStack1:
    def __init__(self):
        self.stack = []
        self.min_values = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(val)
            self.min_values.append([val, 1])
            return

        self.stack.append(val)
        if self.getMin() == val:
            self.min_values[-1][1] += 1
        elif self.getMin() > val:
            self.min_values.append([val, 1])

    def pop(self) -> None:
        val = self.stack.pop()
        if self.getMin() == val:
            self.min_values[-1][1] -= 1
            if self.min_values[-1][1] == 0:
                self.min_values.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_values[-1][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
