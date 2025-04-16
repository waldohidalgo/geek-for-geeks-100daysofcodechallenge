class Solution:
    def findSplit(self, arr):
        # Return an array of possible answer, driver code will judge and return true or false based on
        n=len(arr)
        total=sum(arr)
        i=0
        j=n-1
        sum_left=arr[i]
        sum_right=arr[j]
        while i<j:
            medium_sum=total-sum_left-sum_right
            if sum_left==sum_right and sum_right==medium_sum:
                return [i,j-1]
            elif sum_left<sum_right:
                i+=1
                sum_left+=arr[i]
            else:
                j-=1
                sum_right+=arr[j]
        return [-1,-1]
    
sol=Solution()
arr=[1, 3, 4, 0, 4]
#arr=[0, 1, 1]
print(sol.findSplit(arr))