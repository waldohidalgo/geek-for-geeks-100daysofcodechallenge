class Solution:
    def getLastMoment(self, n, left, right):
        #code here
        return max(max(left) if left else 0,n-min(right) if right else 0)
    

sol=Solution()
n=3
left=[0]
right= [3]

print(sol.getLastMoment(n,left,right))