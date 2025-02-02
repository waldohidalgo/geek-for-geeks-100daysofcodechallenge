class Solution:
    def power(self, b: float, e: int) -> float:
        # Code Here
        if e<0:
            return 1/self.power(b,-e)
        if e==0:
            return 1
        factor=self.power(b,e//2)
        if e%2==0:
            return factor*factor
        else:
            return b*factor*factor
            
sol=Solution()
b=3
e=5
print(sol.power(b,e))