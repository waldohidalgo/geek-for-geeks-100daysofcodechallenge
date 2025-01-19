class Solution:
    def maxSum(self,arr):
        # code here
        arr.sort()
        i=0
        j=len(arr)-1
        max_sum=0
        last_element=arr[0]
        while i<=j:
            max_sum+=abs(arr[i]-last_element)
            last_element=arr[i]
            i+=1
            if i>j:
                break
            max_sum+=abs(arr[j]-last_element)
            last_element=arr[j]
            j-=1   
        max_sum+=abs(arr[0]-last_element)
        return max_sum
    
sol=Solution()
arr = [10,12]

print(sol.maxSum(arr))