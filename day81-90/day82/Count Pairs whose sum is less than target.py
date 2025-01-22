class Solution:
    #Complete the below function
    def countPairs(self, arr, target):
        #Your code here
        arr.sort()
        count = 0
        l,r=0,len(arr)-1
        while l<r:
            if arr[l]+arr[r]>=target:
                r-=1
            else:
                count+=(r-l)
                l+=1
        return count
sol = Solution()
arr=[2, 1, 8, 3, 4, 7, 6, 5]
target=7
print(sol.countPairs(arr,target))