class Solution:
    def subarraySum(self, arr, target):
        # code here
        n=len(arr)
        s,cur=0,0
        for e in range(n):
            cur+=arr[e]
            while cur>target and s<=e:
                cur-=arr[s]
                s+=1
            if cur==target:
                return [s+1,e+1]
        return [-1]
    
sol=Solution()
arr=[15, 2, 4, 8, 9, 5, 10, 23]
target=23
print(sol.subarraySum(arr,target))