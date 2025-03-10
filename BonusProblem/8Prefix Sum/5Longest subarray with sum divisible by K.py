class Solution:
    def longestSubarrayDivK(self, arr, k):
		#Complete the function
        n=len(arr)
        acc=0
        max_length=0
        hs={0:-1}        
        for i in range(n):
            acc=(acc+arr[i])%k
            if acc in hs:
                max_length=max(max_length,i-hs[acc])
            else:
                hs[acc]=i
        return max_length

arr=[1, 2, -2]
k=2
sol=Solution()
print(sol.longestSubarrayDivK(arr,k))