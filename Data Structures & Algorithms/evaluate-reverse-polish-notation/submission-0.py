class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for s in tokens:
            if s not in ["+", "-", "/", "*"]:
                nums.append(int(s))
            else:
                b = nums.pop()
                a = nums.pop()

                if s == "+":
                    val = a + b
                elif s == "-":
                    val = a - b
                elif s == "/":
                    val = int(a/b)
                else:
                    val = a * b

                nums.append(val)
        return nums[-1]
            
