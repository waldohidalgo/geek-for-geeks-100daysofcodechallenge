class Solution:
    def _verifyValidity(self,lv,rv,res,ms,target):
        curr=lv+rv
        diff = abs(target - curr)
        if diff < ms:
            return (lv, rv), diff

        elif diff == ms and abs(lv - rv) > abs(res[0] - res[1]):
            return (lv, rv), ms

        return res, ms
    
    def sumClosest(self, arr, target):
        # code here
        arr.sort()
        res = (None, None)
        ms = float('inf') 
        l, r = 0, len(arr) - 1
        
        while l < r:
            curr = arr[l] + arr[r]
            res, ms = self._verifyValidity(arr[l], arr[r], res, ms, target)
            if curr >= target:
                r -= 1
            else:
                l += 1
        
        return [] if res == (None, None) else list(res)
        
sol=Solution()
arr= [10, 30, 20, 5]
target = 25
print(sol.sumClosest(arr,target)) 
