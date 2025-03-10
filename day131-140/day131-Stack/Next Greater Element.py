class Solution:
    # Function to find the next greater element for each element of the array.
    def nextLargerElement(self, arr):
        # code here
        stack=[]
        n=len(arr)
        res=[-1]*n
        for i in range(n-1,-1,-1):
            if not stack:
                stack.append(arr[i])
            else:
                while stack and stack[-1]<=arr[i]:
                    stack.pop()
                if stack:
                    res[i]=stack[-1]
                stack.append(arr[i])
        return res
    
sol=Solution()
arr=[41,88,58,69,93,42,44,25,12,47,41,88,58,69,93,42,44,25,12,47]
print(sol.nextLargerElement(arr))
                            
