class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        #this is pushing the actual values into a stack
        self.stack.append(val)
        #this is pushing ONLY the minimum element we have encountered SO FAR to the min stack.
        #we update val to be the minimum between the val, OR the top element of the minstack
        #this ONLY HAPPENS WHEN there is something in the minstack, otherwise, just use the same val
        val = min(val, self.minStack[-1] if self.minStack else val)
        #adds that minimum value to the minstack
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
            
        
