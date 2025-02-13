class Solution:
    def _is_valid(self,part):
        if len(part)>1 and part[0]=="0":
            return False
        num=int(part)
        return num>=0 and num<=255

    def generateIp(self, st):
        # Code here
        res=[]
        def rec(s,ip,ct):
            if not s:
                return           
            if ct==3:
                if self._is_valid(s):
                    res.append(ip+str(s))
                return
            n=len(s)
            for i in range(1,n):
                part=s[0:i]
                if self._is_valid(part):
                    rec(s[i:],ip+str(part)+".",ct+1)
        rec(st,"",0)
        return res
    
    def generateIp2(self, s):
        # Code here
        res=[]
        def rec(start,ip,ct):
            if not s:
                return           
            if ct==3:
                final=s[start:]
                if self._is_valid(final):
                    res.append(ip+str(final))
                return
            # aca se hace uso estricto de que numeros no deben tener como prefijo 0
            for i in range(1,4):
                part=s[start:start+i]
                if self._is_valid(part):
                    rec(start+i,ip+str(part)+'.',ct+1)
        rec(0,"",0)
        return res    

#s="255678166"
#s="1234500"
#s="25505011535"
#s="5"
s="000001234"
sol=Solution()
print(sol.generateIp(s))
print(sol.generateIp2(s))