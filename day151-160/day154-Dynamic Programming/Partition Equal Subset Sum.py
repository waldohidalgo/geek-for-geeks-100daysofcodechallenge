class Solution:
    def equalPartition(self, arr):
        # code here
        all_sum=sum(arr)
        n=len(arr)
        if all_sum%2!=0:
            return False
        k=all_sum//2
        # buscar si existe una suma de elementos igual
        # a sum(arr)/2
        dp=[[False]*(k+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,k+1):
                if j==arr[i-1]:
                    dp[i][j]=True
                elif j<arr[i-1]:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]]
        return dp[n][k]
    

    def equalPartition2(self, arr):
        # code here
        all_sum=sum(arr)
        n=len(arr)
        if all_sum%2!=0:
            return False
        k=all_sum//2
        # buscar si existe una suma de elementos igual
        # a sum(arr)/2
        dp=[False]*(k+1)
        for i in range(1,n+1):
            for j in range(k,0,-1):
                if j==arr[i-1]:
                    dp[j]=True
                elif j>arr[i-1]:
                    dp[j]=dp[j] or dp[j-arr[i-1]]
        return dp[k]
    
sol=Solution()
arr = [1, 5, 11, 5]
print(sol.equalPartition2(arr))

