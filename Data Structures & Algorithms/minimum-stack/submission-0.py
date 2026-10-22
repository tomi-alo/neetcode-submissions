class MinStack:

    def __init__(self):
        self.min_stack = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)

        else:
            minimum = min(self.min_stack[-1], val)
            self.min_stack.append(minimum)


    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        latest = self.stack[-1]
        return latest

    def getMin(self) -> int:
        latest = self.min_stack[-1]
        return latest
