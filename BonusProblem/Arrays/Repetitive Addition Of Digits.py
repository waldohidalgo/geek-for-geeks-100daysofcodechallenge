class Solution:
    def singleDigit(self, n):
    	#code here 
        if n<10:
            return n
        if n%9==0:
            return 9
        return n%9
    
sol=Solution()
n=9
print(sol.singleDigit(n))