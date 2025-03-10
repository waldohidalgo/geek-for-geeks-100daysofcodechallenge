
class Solution:
    def minRemovals(self, arr, k):
        # code here
        n=len(arr)
        total=sum(arr)
        target=total-k
        l=0
        max_length=float('-inf')
        acc=0
        for r in range(n):
            acc+=arr[r]
            while l<=r and acc>target:
                acc-=arr[l]
                l+=1
            if acc==target:
                max_length=max(max_length,r-l+1)
    
        return -1 if max_length==float('-inf') else n-max_length

sol=Solution()
# arr=[1, 1, 3, 1, 2]
# k=4
# arr=[3, 4, 1, 3, 2] #13
# k=5
# arr=[5, 3, 4, 6, 2]
# k=6
arr=[8828,9581,49,98181,9974,9869,9991,10000, 10000, 10000, 9999, 9993, 9904, 8819, 1231, 6309]
k=134365
print(sol.minRemovals(arr,k))


