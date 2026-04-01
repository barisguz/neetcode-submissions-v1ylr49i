class Solution:
    def isValid(self, s: str) -> bool:
        ## if it is opening one, add to stack, if closing ,pop from stack and compare 
        stack = deque()
        closeToOpen = { "}": "{", "]":"[", ")" : "("}

        for i in s:
            if i in closeToOpen:
                if stack and closeToOpen[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
