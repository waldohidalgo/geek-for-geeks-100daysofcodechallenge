class Solution:
    # Function to find if there exists a triplet in the array arr[] which sums up to target.
    def hasTripletSum(self, arr, target):
        # Your Code Here
        arr.sort()
        n=len(arr)
        for i in range(2,n):
            l,r=0,i-1
            while l<r:
                val=arr[l]+arr[r]+arr[i]
                if val<target:
                    l+=1
                elif val>target:
                    r-=1
                else:
                    return True
        return False
sol=Solution()
arr = [40, 20, 10, 3, 6, 7]
target = 24
print(sol.hasTripletSum(arr,target))
        
            