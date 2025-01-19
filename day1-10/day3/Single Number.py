class Solution:
    def getSingle(self,arr):
        # code here
        result=0
        for i in arr:
            result=result^i
        return result

        
sol=Solution()
arr=[8, 8, 7, 7, 6, 6,1,1, 1]
print(sol.getSingle(arr))   

