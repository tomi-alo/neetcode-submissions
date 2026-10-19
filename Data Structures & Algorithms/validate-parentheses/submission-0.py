class Solution:
    def isValid(self, s: str) -> bool:
        closed_to_open = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        # keep note of what's in the stack right now
        stack = []
        for bracket in s:
            if bracket in closed_to_open:
                if not stack:
                    return False
                top = stack.pop()
                if closed_to_open[bracket] != top:
                    return False
            else:
                stack.append(bracket)

        if stack:
            return False
        else:
            return True