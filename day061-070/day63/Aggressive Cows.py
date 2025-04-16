class Solution:
    def aggressiveCows(self, stalls, k):
        # Write your code here  
        stalls.sort()
        n=len(stalls)
        low=1
        high=stalls[n-1]-stalls[0]
        while low<=high:
            mid=(low+high)//2
            count=1
            prev=stalls[0]
            for i in range(1,n):
                if stalls[i]-prev>=mid:
                    count+=1
                    prev=stalls[i]
            if count>=k:
                low=mid+1
            else:
                high=mid-1
        return high

sol=Solution()
arr= [2, 12, 11, 3, 26, 7]
k=5
print(sol.aggressiveCows(arr,k))