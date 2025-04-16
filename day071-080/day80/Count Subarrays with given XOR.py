class Solution:
    def subarrayXor(self, arr, k):
        # code here
        last=0
        pf={0:1}
        count=0
        for el in arr:
            curr=el^last
            if curr^k in pf:
                count+=pf[curr^k] 
            pf[curr]=pf.get(curr,0)+1
            last=curr
        return count  
arr=[5, 6, 7, 8, 9]
k=5
print(Solution().subarrayXor(arr,k))      