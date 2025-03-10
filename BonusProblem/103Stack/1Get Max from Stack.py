class Solution:
    # solucion sin memoria adicional para almacenar referencias a maximos previos
    # se utiliza una caracterizacion matematica para aquello
    def __init__(self):
        # code here
        self.stack=[]
        self.max_elem=None
        
    # Add an element to the top of Stack
    def push(self, x):
        # code here
        stack=self.stack
        if not stack:
            stack.append(x)
            self.max_elem=x
        else:
            if x>self.max_elem:
                self.stack.append(2*x-self.max_elem) # anterior maximo
                self.max_elem=x
            else:
                self.stack.append(x)
        
    # Remove the top element from the Stack
    def pop(self):
        # code here
        if self.stack:
            if self.stack[-1]>self.max_elem:
                self.max_elem=2*self.max_elem-self.stack.pop()
            else:
                self.stack.pop()
                

    # Returns top element of Stack
    def peek(self):
        # code here
        if self.stack:
            if self.stack[-1]>self.max_elem:
                return self.max_elem
            else:
                return self.stack[-1]

        else:
            return -1
    
    # Finds minimum element of Stack
    def getMax(self):
        # code here
        if self.stack:
            return self.max_elem
        else:
            return -1


sol=Solution()
queries =  [[1, 10], [4], [1, 5], [4], [2]]
for i in range(len(queries)):
    if len(queries[i])>1:
        sol.push(queries[i][1])
    else:
        command=queries[i][0]
        if command==2:
            sol.pop()
        elif command==3:
            print(sol.peek())
        elif command==4:
            print(sol.getMax())

