class Solution:
    # arr[] : the input array
    #Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self,arr):
        #code here
        values=set(arr)
        lcs=0
        for e in values:
            if e-1 not in values:
                start=e
                while start+1 in values:
                    start+=1
                lcs=max(lcs,start-e+1)
        return lcs


arr =[1, 3,8,10,12,15]
sol=Solution()
print(sol.longestConsecutive(arr))