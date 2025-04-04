import heapq

class Solution:
    def jobSequencing(self, deadline, profit):
        # ordenacion por profit de mayor a menor para luego
        # asignar mayores profit, al mayor deadline disponible
        jobs = sorted(zip(deadline, profit), key=lambda x: -x[1])
        n=len(deadline)
        slots = [-1] *(n+1)

        max_profit = 0
        count_jobs = 0

        for d, p in jobs:
            for t in range(min(d,n), 0, -1):
                if slots[t] == -1: 
                    slots[t] = p 
                    max_profit += p
                    count_jobs += 1
                    break 
        
        return [count_jobs, max_profit]
    
    def jobSequencing2(self, deadline, profit):
        jobs = sorted(zip(deadline, profit))
        heap=[]

        for job in jobs:
            if job[0]>len(heap):
                heapq.heappush(heap,job[1])
            elif heap[0]<job[1]:
                heapq.heappop(heap)
                heapq.heappush(heap,job[1])

        return [len(heap),sum(heap)]
    

# deadline=[3, 1, 2, 2]
# profit= [50, 10, 20, 30]
# deadline = [4, 1, 1, 1]
# profit = [20, 10, 40, 30]
deadline= [2, 1, 2, 1, 1]
profit = [100, 19, 27, 25, 15]
sol=Solution()
print(sol.jobSequencing2(deadline,profit))