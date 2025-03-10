class Solution:

    def __init__(self):
        # code here
        self.stack=[]
        self.minimun=[] # minimos ordenados
        
    # Add an element to the top of Stack
    def push(self, x):
        # code here
        self.stack.append(x)
        if not self.minimun:
            self.minimun.append(x)
        else:
            if self.minimun[-1]>=x:
                self.minimun.append(x)


    # Remove the top element from the Stack
    def pop(self):
        # code here
        if self.stack:
            elem=self.stack.pop()
            if elem==self.minimun[-1]:
                self.minimun.pop()

    # Returns top element of Stack
    def peek(self):
        # code here
        return self.stack[-1] if self.stack else -1

    # Finds minimum element of Stack
    def getMin(self):
        # code here
        return self.minimun[-1] if self.minimun else -1


sol=Solution()
queries =[[1, 10], [4], [1, 5], [4], [2]]
for par in queries:
    n=len(par)
    if n!=1:
        sol.push(par[1])
    elif par[0]==2:
        sol.pop()
    elif par[0]==3:
        print(sol.peek())
    else:
        print(sol.getMin())