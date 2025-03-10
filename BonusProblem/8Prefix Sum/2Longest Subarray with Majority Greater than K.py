class Solution:
    def longestSubarray(self, arr, k):
        # Code Here
        n=len(arr)
        acc=0
        hs={}
        
        for i in range(n):
            acc+=(1 if arr[i]>k else -1)
            if acc not in hs:
                hs[acc]=i

        min_index = float('inf')
        for el in range(-n-1, 1): 
            if el in hs:
                min_index = min(min_index, hs[el])
            hs[el] = min_index

        acc=0
        ct=0
        for i in range(n):
            acc+=(1 if arr[i]>k else -1)
            if acc>0:
                ct=i+1
            else:
                print(acc,i)
                ct=max(ct,i-hs[acc-1])
        return ct
    
sol=Solution()
#arr=[1, 2, 3, 4, 1]
#arr=[6, 5, 3, 4]
#k=2
arr=[55,53,91,99,82,54,50,76,64,12,86,96,63,81,61,29]
k=100
print(sol.longestSubarray(arr,k))