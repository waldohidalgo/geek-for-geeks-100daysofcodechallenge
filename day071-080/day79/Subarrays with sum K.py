class Solution:
    def countSubarrays(self, arr, k):
        # code here
        last=0
        pf={0:1}
        count=0
        for el in arr:
            curr=el+last
            if curr-k in pf:
                count+=pf[curr-k] 
            pf[curr]=pf.get(curr,0)+1
            last=curr
        return count
    
sol=Solution()
arr =[1, 3, 5]
k=0
print(sol.countSubarrays(arr,k))

