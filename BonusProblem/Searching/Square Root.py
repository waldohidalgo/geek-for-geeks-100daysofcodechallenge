class Solution:
    def floorSqrt(self, n): 
    #Your code here
        l,r=1,n
        while l<r:
            mid=-(-(r+l)//2)
            if mid*mid>n:
                r=mid-1
            else:
                l=mid
        return l
        
    
sol=Solution()
print(sol.floorSqrt(99))