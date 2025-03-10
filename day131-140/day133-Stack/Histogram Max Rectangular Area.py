class Solution:
    def getMaxArea(self,arr):
        
        stack=[]
        max_area=0
        n=len(arr)
        for i,value in enumerate(arr):
            if not stack:
                stack.append(i)
            else:
                while stack and arr[stack[-1]]>value:
                    top=stack.pop()
                    if stack:
                        max_area=max(max_area,arr[top]*(i-stack[-1]-1))
                    else:
                        # fondo
                        max_area=max(max_area,arr[top]*(i))
                stack.append(i)
        # cabezas fondo mayores        
        while stack:
            top=stack.pop()
            if stack:
                max_area=max(max_area,arr[top]*(n-1-stack[-1]))
            else:
                # cabeza fondo fondo
                max_area=max(max_area,arr[top]*n)

        return max_area
    

    def getMaxArea2(self,arr):
        n = len(arr)
                
        left = [0] * n
        right = [0] * n
        
        left[0] = -1  
        for i in range(1, n):
            prev = i - 1
            while prev >= 0 and arr[prev] >= arr[i]:
                prev = left[prev]  
            left[i] = prev
                
        right[n-1] = n  
        for i in range(n-2, -1, -1):
            next_ = i + 1
            while next_ < n and arr[next_] >= arr[i]:
                next_ = right[next_]  
            right[i] = next_
                
        max_area = 0
        for i in range(n):
            width = right[i] - left[i] - 1
            max_area = max(max_area, arr[i] * width)
        
        return max_area




sol=Solution()
arr=[60, 20, 50, 40, 10, 50, 60]
print(sol.getMaxArea(arr))

