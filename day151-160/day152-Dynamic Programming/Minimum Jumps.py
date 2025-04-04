class Solution:
    def minJumps(self, arr):
        # code here
        if arr[0]==0:
            return -1
        n=len(arr)
        dp=[-1]*(n+1) 
        dp[1]=0
        for i in range(2,n+1):
            for j in range(1,i):
                if arr[j-1]>=i-j and dp[j]!=-1:
                    # j>=i-arr[j-1]
                    dp[i]=dp[j]+1
                    break
        return dp[n]

    def minJumps2(self,arr):
        n=len(arr)
        
        longest=0
        ct=0
        max_jump_index=0

        for i in range(n-1):
            longest=max(longest,i+arr[i])
            if longest==i:
                return -1
            if  i==max_jump_index:
                max_jump_index=longest
                ct+=1
                if max_jump_index>=n-1:
                    return ct
		
sol=Solution()
#arr=[5,6]
arr=[1, 3, 5, 8, 1, 2, 6, 7, 6, 8, 9,8,4,5]
#arr=[1, 4, 3, 2, 6, 7]
#arr=[1,1,2,1,1,5,5,1]
print(sol.minJumps(arr))
print(sol.minJumps2(arr))
				
			