from collections import Counter
import heapq

class Solution:
	def topKFrequent(self, arr, k):
		# your code here
		ctr=Counter(arr)
		heap=[]
		for key in ctr:
			heapq.heappush(heap,(-ctr[key],-key))
			
		return [-heapq.heappop(heap)[1] for _ in range(k)]
	
sol=Solution()
arr=[7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9]
k=4
print(sol.topKFrequent(arr,k))