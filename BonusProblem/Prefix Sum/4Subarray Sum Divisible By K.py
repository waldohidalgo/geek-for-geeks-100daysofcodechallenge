class Solution:
    # Function to count the number of subarrays with a sum that is divisible by K
    def subCount(self, arr, k):
        # Your code goes here
        hs={0:1}
        n=len(arr)
        acc=0
        ct=0
        for i in range(n):
            acc=(acc+arr[i])%k
            if acc in hs:
                ct+=hs[acc]
                hs[acc]+=1
            else:
                hs[acc]=1
        return ct
    
arr=[-1, -3, 2]
k=5
sol=Solution()
print(sol.subCount(arr,k))
