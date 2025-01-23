class Solution:
    
    def findSplit(self, arr):
        # Return an array of possible answer, driver code will judge and return true or false based on
        n=len(arr)
        total=sum(arr)
        part_sum=total//3
        if total%3!=0:
            return [-1,-1]
        sum_left=0
        sum_right=0
        ipos=None
        jpos=None
        for i in range(n):
            sum_left+=arr[i]
            if sum_left==part_sum:
                ipos=i
                break
        if ipos is None:
            return [-1,-1]
        for i in range(ipos+1,n):
            sum_right+=arr[i]
            if sum_right==part_sum:
                jpos=i
                break
        if ipos is not None and jpos is not None:
            return [ipos,jpos]
        return [-1,-1]


arr= [0, 1, 1]
obj = Solution()
print(obj.findSplit(arr))