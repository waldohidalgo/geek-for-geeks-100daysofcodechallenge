
class Solution:
    def singleNum(self, arr):
        # Code here
        xor=0
        for num in arr:
            xor^=num
        a=0
        b=0
        lsb=xor&-xor # paso clave, obtiene el menor digito significativo
        for num in arr:
            if num&lsb:
                a^=num
            else:
                b^=num
        return [min(a,b),max(a,b)]
    
    def singleNum2(self,arr):
        nums=set()
        for num in arr:
            if num in nums:
                nums.remove(num)
            else:
                nums.add(num)
        return list(sorted(nums))
                

    
sol=Solution()
arr=[1, 2, 3, 2, 1, 4]
print(sol.singleNum2(arr))