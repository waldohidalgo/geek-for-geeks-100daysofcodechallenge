import heapq

class Solution:
    # prim algorithm
    def minCost(self, houses):
      # code here
        n = len(houses)
        visited = [False] * n
        minHeap = [(0, 0)]  # (coste, índice de la casa)
        result = 0
        edgesUsed = 0
        while edgesUsed<n:
            cost,i=heapq.heappop(minHeap)
            if visited[i]:
                continue
            visited[i]=True
            result+=cost
            edgesUsed+=1
            for j in range(n):
                if not visited[j]:
                    x_i,y_i=houses[i]
                    x_j,y_j=houses[j]
                    distance=abs(x_i-x_j)+abs(y_i-y_j)    
                    heapq.heappush(minHeap,(distance,j))
        return result
    

sol=Solution()

houses =[[0, 0], [1, 1], [1, 3], [3, 0]]
print(sol.minCost(houses))