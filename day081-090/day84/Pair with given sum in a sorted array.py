class Solution:
    def countPairs (self, arr, target) : 
        #Complete the function
        ct=0
        l,r=0,len(arr)-1
        while l<r:
            val=arr[l]+arr[r]
            if val>target:
                r-=1
            elif val<target:
                l+=1
            else:
                ctl,ctr=0,0
                lv,rv=arr[l],arr[r]
                while l<=r and arr[l]==lv:
                    l+=1
                    ctl+=1
                while l<=r and arr[r]==rv:
                    r-=1
                    ctr+=1
                if lv==rv:
                    ct+=(ctl)*(ctl-1)//2
                else:
                    ct+=ctl*ctr
        return ct


arr=[-1, 10, 10, 12, 15]
target=125
print(Solution().countPairs(arr,target))