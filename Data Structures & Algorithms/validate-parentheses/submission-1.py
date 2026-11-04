class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        #closing brackets are the key, the value is the opening bracket 
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        #iterating through string
        for c in s:
            #check if the current bracket is a closing bracket
            if c in closeToOpen:
                #if the stack is not empty AND the previous element is equal to the corresponding bracket, 
                #pop it off and do not add the closing bracket to the stack
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            #if the current element is not a closing bracket, add it to the stack
            else:
                stack.append(c)

        return True if not stack else False