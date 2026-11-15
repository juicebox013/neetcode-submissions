class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #maybe have a stack for the numbers
        #loop through the array and every time we hit an operand, pull the top 
        #two numbers on the stack and use the operand on it. then add it to the top of the stack.
        #continue till we reach the end of the original array.
        numbers = []
        for num in tokens:
            if num == "+":
                b = numbers.pop()
                a = numbers.pop()
                numbers.append(a + b)
            elif num == "-":
                b = numbers.pop()
                a = numbers.pop()
                numbers.append(a - b)
            elif num == "*":
                b = numbers.pop()
                a = numbers.pop()
                numbers.append(a*b)
            elif num == "/":
                b = numbers.pop()
                a = float(numbers.pop())
                numbers.append(int(a/b))
            else:
                numbers.append(int(num))
        return int(numbers[-1])
                
