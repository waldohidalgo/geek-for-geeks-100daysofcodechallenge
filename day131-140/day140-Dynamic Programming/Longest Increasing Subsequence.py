
class Solution:
    def lis(self, arr):
        # time complexity n*n
        # code here
        n=len(arr)
        max_len=0
        dp=[1]*n
        for i in range(n):
            mx=float("-inf")
            for j in range(i):
                if arr[j]<arr[i]:
                    mx=max(mx,dp[j])
            dp[i]=max(1,1+mx)
            max_len=max(max_len,dp[i])
        return max_len

    def lis1(self,arr):
        # time complexity n*log(n)
        n=len(arr)
        bucket=[]
        max_len=1
        for i in range(n):
            if not bucket:
                bucket.append(arr[i])
            else:
                if arr[i]>bucket[-1]:
                    bucket.append(arr[i])
                else:
                    l,r=0,len(bucket)-1
                    while l<r:
                        mid=(l+r)//2
                        if bucket[mid]>=arr[i]:
                            r=mid
                        else:
                            l=mid+1
                    bucket[l]=arr[i]
                
        return len(bucket)




sol=Solution()
#arr= [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
arr=[3, 10, 2, 1, 20]
print(sol.lis(arr))
print(sol.lis1(arr))