class Solution:
    def maxLen(self, arr):
        # code here
        n=len(arr)
        ls=0
        hs={0:-1}
        acc=0
        for i in range(n):
            acc+=(1 if arr[i]==1 else -1)
            if acc in hs:
                ls=max(ls,i-hs[acc])
            else:
                hs[acc]=i
        return ls
    
sol=Solution()
arr=[0, 0, 1, 1, 0]
print(sol.maxLen(arr))
