import math
class Solution:
    def evaluate(self, arr):
        # code here
        stack=[]
        operators={"+","-","*","/"}
        for el in arr:
            if el not in operators:
                stack.append(int(el))
            else:
                op2=stack.pop()
                op1=stack.pop()
                if el=="+":
                    res=op1+op2
                elif el=="-":
                    res=op1-op2
                elif el=="*":
                    res=op1*op2
                else:
                    res=math.trunc(op1/op2)
                stack.append(res)
        return stack[-1]
    

sol=Solution()
arr =  ["-1","8","/"]
print(sol.evaluate(arr))