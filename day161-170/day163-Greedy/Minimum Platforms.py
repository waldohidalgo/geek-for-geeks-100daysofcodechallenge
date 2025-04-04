class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,arr,dep):
        # code here
        n=len(arr)
        arr.sort()
        dep.sort()
        min_num=0
        count=0
        l,r=0,0
        while l<n:
            if arr[l]<dep[r]:
                count+=1
                min_num=max(min_num,count)
                l+=1
            else:
                count-=1
                r+=1
        return min_num

# arr= [900, 940, 950, 1100, 1500, 1800]
# dep= [910, 1200, 1120, 1130, 1900, 2000]
# arr = [900, 1235, 1100]
# dep = [1000, 1240, 1200]
arr= [1000, 1000, 1100]
dep = [1200, 1240, 1130]
sol=Solution()
print(sol.minimumPlatform(arr,dep))