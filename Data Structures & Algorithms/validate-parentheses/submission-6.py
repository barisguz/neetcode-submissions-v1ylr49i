class Solution:
    def isValid(self, s: str) -> bool:
        ## if it is opening one, add to stack, if closing ,pop from stack and compare 
        stack = deque()

        for i in s:
            if(i == '[' or i == '{' or i =='('):
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False

                if (i == '}' and stack.pop() != '{'):
                    return False
                elif(i == ')' and stack.pop() != '('):
                    return False
                elif(i == ']' and stack.pop() != '['):
                    return False

        if len(stack) == 0:
            return True
        return False
