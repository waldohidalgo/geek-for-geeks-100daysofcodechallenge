class Solution:
    def myAtoi(self, s):
        # Code here
        ulimit=(1<<31)-1
        llimit=-(1<<31)
        num=0
        sign=1
        i=0
        while i<len(s):
            if s[i]==' ':
                i+=1
            else:
                break
        if i==len(s):
            return 0
        if s[i]=='-':
            sign=-1
            i+=1
        elif s[i]=='+':
            i+=1
        if i==len(s):
            return 0
        while i<len(s):
            if s[i].isdigit():
                num=num*10+int(s[i])
                if num*sign>ulimit:
                    return ulimit
                elif num*sign<llimit:
                    return llimit
                i+=1
            else:
                break
        
        return num*sign
    
sol=Solution()
# s = "-999999999999"
# s = "      -"
s = " 1231231231311133"
print(sol.myAtoi(s))
print()
