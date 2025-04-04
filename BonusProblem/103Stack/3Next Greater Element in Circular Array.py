class Solution:

    def nextLargerElement(self, arr):
        #code here 
        stack=[]
        n=len(arr)
        for i in range(n-1,-1,-1):
            if not stack:
                stack.append(arr[i])
            else:
                while stack and stack[-1]<=arr[i]:
                    stack.pop()
                stack.append(arr[i])
        res=[-1]*n
        for i in range(n-1,-1,-1):
            while stack and stack[-1]<=arr[i]:
                stack.pop()
            if stack:
                res[i]=stack[-1]
            stack.append(arr[i])
        return res
    
sol=Solution()
arr= [0,2,3,1,1]
print(sol.nextLargerElement(arr))
                    