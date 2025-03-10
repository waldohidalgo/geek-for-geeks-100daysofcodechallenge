class Solution:
    def calculateSpan(self, arr):
        #write code here
        stack=[]
        n=len(arr)
        res=[1]*n
        for i,v in enumerate(arr):
            if not stack:
                stack.append((v,i))
            else:
                while stack and stack[-1][0]<=v:
                    stack.pop()
                if stack:
                    res[i]=i-stack[-1][1]
                else:
                    res[i]=i+1
                stack.append((v,i))                
        return res
    

sol=Solution()
arr=[100, 80, 60, 70, 60, 75, 85]
#arr=[10, 4, 5, 90, 120, 80]
print(sol.calculateSpan(arr))
