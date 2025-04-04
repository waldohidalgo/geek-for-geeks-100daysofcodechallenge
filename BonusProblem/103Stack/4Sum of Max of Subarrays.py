class Solution:
    def sumOfMax(self, arr):
        # code here
        n=len(arr)
        left=[0]*n
    
        stack=[]
        for i in range(n):
            while stack and arr[stack[-1]]<arr[i]:
                stack.pop()
            left[i]=i-stack[-1] if stack else i+1
            stack.append(i)

        stack.clear()
        right=[0]*n
        # aca considero los iguales pero arriba no ya que ya fueron considerados
        for i in range(n-1,-1,-1):
            while stack and arr[stack[-1]]<=arr[i]:
                stack.pop()
            right[i]=stack[-1]-i  if stack else n-i
            stack.append(i)
        
        count=0
        for i in range(n):
            count+=arr[i]*left[i]*right[i]

        return count


arr = [1, 3, 2]
#arr=[3,1]
#arr=[8,0,1]
sol=Solution()
print(sol.sumOfMax(arr))