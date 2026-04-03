class Solution:
    def isValid(self, s: str) -> bool:

        ## create a dictionary of opening 
        ## and corresponding close brackets 
        ## iterate through the string 
        ## if you dont see a closing bracket, add it to the stack
        ## if you see a closing bracket, compare it to stack..pop
        ## until you don't have anything else in the stack 

        validParanth = {"}": "{", ")":"(", "]":"["}
        stack = []
        for i in range(len(s)):
            if s[i] in validParanth:
                if stack:
                    curr = stack.pop()
                    if curr != validParanth[s[i]]:
                        return False
                else:
                    return False
            else:
                stack.append(s[i])
        return not stack
