import heapq
class Solution:
    def nearlySorted(self, arr, k):
        #code
        heap=[]
        n=len(arr)
        for i in range(k+1):
            heapq.heappush(heap,arr[i])
        for i in range(n):
            arr[i]=heapq.heappop(heap)
            if i+k+1<n:
                heapq.heappush(heap,arr[i+k+1])
        return arr

sol=Solution()

arr = [1, 4, 5, 2, 3, 6, 7, 8, 9, 10]
k = 2

print(sol.nearlySorted(arr,k))
        