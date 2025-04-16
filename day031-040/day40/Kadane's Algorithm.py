class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        ##Your code here
        n=len(arr)
        max_sum=arr[0]
        curr_sum=arr[0]
        for i in range(1,n):
            curr_sum=max(arr[i],curr_sum+arr[i])
            max_sum=max(curr_sum,max_sum)
        return max_sum

sol=Solution()
#arr=[5, 4, 1, 7, 8]
#arr=[10,20,-30,40,-50,60]
arr=[-7,-8,-16,-4,-8,-5,-7,-11,-10,-12,-4,-6,-4,-1]
print(sol.maxSubArraySum(arr))