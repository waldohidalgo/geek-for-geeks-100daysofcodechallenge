import heapq

class Solution:
	def kLargest(self, arr, k):
		# Your code here
		n=len(arr)
		heap=[]
		heapq.heapify(heap)
		for i in range(k):
			heapq.heappush(heap,arr[i])
		for j in range(i+1,n):
			if heap[0]<arr[j]:
				heapq.heappop(heap)
				heapq.heappush(heap,arr[j])
		res=[]
		for i in range(k):
			res.append(heapq.heappop(heap))
		res.reverse()
		return res

	
arr=[6110,5340,30210,2271,12616,18751,28980,32632,306,31136]
k=6
sol=Solution()
print(sol.kLargest(arr,k))