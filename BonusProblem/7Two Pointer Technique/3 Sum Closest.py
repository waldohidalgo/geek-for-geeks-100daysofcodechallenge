class Solution:
    def closest3Sum(self, arr, target):
        # code here
        arr.sort()
        closest=float('inf')
        num=None
        n=len(arr)
        for i in range(2,n):
            l,r=0,i-1
            while l<r:
                curr=arr[l]+arr[r]+arr[i]
                diff=abs(curr-target)
                if diff<closest:
                    closest=diff
                    num=curr
                elif diff==closest and curr>num:
                    num=curr
                
                if curr>target:
                    r-=1
                elif curr<target:
                    l+=1
                else:
                    return target
        return num
                

sol=Solution()
arr = [1, 10, 4, 5]
target = 10
print(sol.closest3Sum(arr=arr,target=target))

                

