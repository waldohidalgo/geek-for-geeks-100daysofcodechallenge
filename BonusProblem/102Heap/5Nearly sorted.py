import heapq

class Solution:
    def nearlySorted(self, arr, k):
        #code
        heap=[]
        n=len(arr)
        for i in range(k+1):
            heapq.heappush(heap,arr[i])

        for i in range(0,n):
            if i>0 and i+k<n:
                heapq.heappush(heap,arr[i+k])
            
            arr[i]=heapq.heappop(heap)
           
        return arr
    
sol=Solution()
arr=[6, 5, 3, 2, 8, 10, 9]
k=3
print(sol.nearlySorted(arr,k))


        
