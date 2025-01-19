class Solution:
    def countgroup(self,arr): 
        xor_total=0
        for i in arr:
            xor_total=xor_total^i
        if xor_total!=0:
                return 0
        MOD = 10**9 + 7
        n=len(arr)
        res= (pow(2,n - 1,MOD)-1)%MOD
        return res

			