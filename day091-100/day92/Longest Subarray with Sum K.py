class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        n=len(arr)
        pf={0:-1}
        acc=0
        length_subarray=0
        for i in range(n):
            acc+=arr[i]
            if acc-k in pf:
                length_subarray=max(length_subarray,i-pf[acc-k])
            if acc not in pf:
                pf[acc]=i
        return length_subarray
            
    

sol=Solution()
arr=[10, 5, 2, 7, 1, -10]
k = 15
print(sol.longestSubarray(arr,k))