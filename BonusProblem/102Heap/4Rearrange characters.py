import heapq
from collections import Counter
class Solution :
    def rearrangeString(self, s):
        #code here
        ctr=Counter(s)
        heap=[]
        for key in ctr:
            heapq.heappush(heap,(-ctr[key],key))
        res=""
        last_elem=None
        last_freq=0
        while heap:
            max_freq_tuple=heapq.heappop(heap)
            max_freq,max_elem=-max_freq_tuple[0],max_freq_tuple[1]

            res+=max_elem
            max_freq-=1

            if last_elem and last_freq>0:
                heapq.heappush(heap,(-last_freq,last_elem))   
            last_elem,last_freq=max_elem,max_freq

        if last_freq>0:
            return ""
        return res




    
sol=Solution()
s = "aba"
#s= "aaabb"
#s = "aaaabc"
print(sol.rearrangeString(s))
            

