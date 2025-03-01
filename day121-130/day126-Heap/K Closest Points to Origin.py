from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Your code here
        heap=[]

        for point in points:
            dist=point[0]*point[0]+point[1]*point[1]
            heapq.heappush(heap,(dist,point))

        res=[]

        for i in range(k):
            dist,point=heapq.heappop(heap)
            res.append(point)

        return res
    
sol=Solution()
arr=[[2, 4], [-1, -1], [0, 0]]
k=1

print(sol.kClosest(arr,k))