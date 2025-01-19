class Solution:
    def roundToNearest(self, strg: str) -> str:
        
        if int(strg[-1]) <= 5:
            return strg[:-1] + '0'
        
        
        nearest_reverse = '0' 
        carry = True  
        
       
        for i in range(len(strg) - 2, -1, -1):
            if carry:
                if strg[i] == '9':
                    nearest_reverse+='0'
                else:
                    nearest_reverse+=str(int(strg[i]) + 1)
                    carry = False
            else:
                nearest_reverse+=strg[i]
    
        if carry:
            return '1' + ''.join(nearest_reverse[::-1])
        else:
            return ''.join(nearest_reverse[::-1])

            


sol=Solution()
strg = "9"
print(sol.roundToNearest(strg))


