class Solution:
    def findMaxSum(self,arr,i,j):
        # code here
        n=j-i+1
        if n<3:
            return max(arr)
        prev2=arr[i]
        prev1=max(arr[i],arr[i+1])
        for t in range(i+2,j+1):
            curr=max(prev1,arr[t]+prev2)
            prev2=prev1
            prev1=curr

        return curr
    def maxValue(self, arr):
        # code here
        n=len(arr)
        if n<4:
            return max(arr)
        # n mayor a 3        
        left_split=self.findMaxSum(arr,1,n-1)
        right_split=self.findMaxSum(arr,0,n-2)

        return max(left_split,right_split)
    
sol=Solution()
arr=[4,9,1,6,2,2,7,2,2,6]
print(sol.maxValue(arr))