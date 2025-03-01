import heapq
class Heaps:
    def __init__(self):
        self.min_heap=[]
        self.max_heap=[]
        heapq.heapify(self.min_heap)
        heapq.heapify(self.max_heap)
        
    def push_max_heap(self,x):
        heapq.heappush(self.max_heap,-x)
    def push_min_heap(self,x):
        heapq.heappush(self.min_heap,x)
        
    def balance_heaps(self):
        len_max_heap=len(self.max_heap)
        len_min_heap=len(self.min_heap)
        if len_max_heap-len_min_heap>1:
            heapq.heappush(self.min_heap,-heapq.heappop(self.max_heap))
        elif len_min_heap-len_max_heap>1:
            heapq.heappush(self.max_heap,-heapq.heappop(self.min_heap))

    def push(self,x):
        if len(self.max_heap)==0:
            self.push_max_heap(x)
            return
        if x<=(-self.max_heap[0]):
            self.push_max_heap(x)
        else:
            self.push_min_heap(x)
        self.balance_heaps()
        
    def get_median(self):
        len_max_heap=len(self.max_heap)
        len_min_heap=len(self.min_heap)      
        if len_max_heap>len_min_heap:
            return -self.max_heap[0]
        elif len_min_heap>len_max_heap:
            return self.min_heap[0]
        else:
            return (self.min_heap[0]-self.max_heap[0])/2
        
class Solution:
    def getMedian(self, arr):
        res=[]
        md=Heaps()
        for i in arr:
            md.push(i)
            res.append(md.get_median())
        return res
    
sol=Solution()
arr=[2, 2, 2, 2]
print(sol.getMedian(arr))