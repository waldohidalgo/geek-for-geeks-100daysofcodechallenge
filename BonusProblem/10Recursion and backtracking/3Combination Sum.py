class Solution:
    
    # Function to find all combinations of elements
    # in array arr that sum to target.
    def combinationSum(self, arr, target):
        # code here
        res=[]
        n=len(arr)
        arr.sort()
        def comb(acum,k,seen):
            if acum==target:
                res.append(seen[:])
                return
            if acum>target or k==n:
                return
            
            for i in range(k,n):
                # agregarlo
                seen.append(arr[i])
                # nueva comb
                comb(acum+arr[i],i,seen)
                # removerlo
                seen.pop()
        comb(0,0,[])
        return res
    
sol=Solution()
arr=[2, 7, 6, 5]
target=16
# arr=[2, 4, 6, 8]
# target=8
# arr=[6, 5, 7]
# target=8
print(sol.combinationSum(arr,target))