class Solution:
    def multiplyStrings(self, s1:str, s2:str):
        # code here
        negative = False
        if s1[0] == '-':
            negative = not negative
            s1 = s1[1:]
        if s2[0] == '-':
            negative = not negative
            s2 = s2[1:]
        
        
        s1 = s1.lstrip('0')
        s2 = s2.lstrip('0')
        
        
        if not s1 or not s2:
            return "0"
        
        n, m = len(s1), len(s2)
        res = [0] * (n + m) 
        
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                mul = (ord(s1[i]) - ord('0')) * (ord(s2[j]) - ord('0'))
                p1 = i + j
                p2 = i + j + 1
                sum = mul + res[p2]
                
                res[p2] = sum % 10
                res[p1] += sum // 10
        
        result = ''.join(map(str, res))
        
        result = result.lstrip('0')
        
        if negative:
            result = '-' + result
        
        return result