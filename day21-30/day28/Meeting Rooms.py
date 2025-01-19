class Solution:
    def canAttend(self,arr):
        # Your Code Here
        arr.sort()
        for i in range(1,len(arr)):
            if arr[i][0]<arr[i-1][1]:
                return False
        return True
    
arr= [[2, 4], [9, 12], [6, 10]]
print(Solution().canAttend(arr))