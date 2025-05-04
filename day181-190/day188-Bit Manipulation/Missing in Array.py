class Solution:
    def missingNum(self, arr):
        # code here
        n=len(arr)+1
        xor_all=0
        xor_arr=0
        for i in range(n):
            xor_all^=i+1

        for i in arr:
            xor_arr^=i
        return xor_all^xor_arr
    

arr= [1]
sol=Solution()
print(sol.missingNum(arr))