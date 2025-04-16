class Solution:
    def countTriplets(self, arr, target):
        # code here
        count=0
        n=len(arr)
        for i in range(n-2):
            l=i+1
            r=n-1
            while l<r:
                if arr[i]+arr[l]+arr[r]==target:
                    cl,cr=0,0
                    lv,rv=arr[l],arr[r]
                    while l<=r and arr[l]==lv:
                        l+=1
                        cl+=1
                    while l<=r and arr[r]==rv:
                        r-=1
                        cr+=1
                        
                    if lv==rv:
                        count+=cl*(cl-1)//2
                    else:
                        count+=cl*cr

                elif arr[i]+arr[l]+arr[r]<target:
                    l+=1
                else:
                    r-=1
        return count
    
# arr= [-20,-15,-10,-9,-3,-2,0,10,10,12,15]
# target=5
arr=[1,1,1,1,1,1]
target=3
print(Solution().countTriplets(arr,target))