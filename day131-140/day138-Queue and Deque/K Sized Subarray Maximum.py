from collections import deque
class Solution:
    def maxOfSubarrays(self, arr, k):
        # code here
        n=len(arr)
        res=[]
        window=deque()
    
        for i in range(n):
            
            while window and window[0] < i - k + 1:
                window.popleft()

            while window and arr[window[-1]] < arr[i]:
                window.pop()    

            window.append(i)            
            #print(window)
            if i >= k - 1:
                res.append(arr[window[0]])

        return res

sol=Solution()
arr= [1, 2, 3, 1, 4, 5, 2, 3, 6]
k=3
print(sol.maxOfSubarrays(arr,k))