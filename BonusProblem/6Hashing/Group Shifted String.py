class Solution:

    def setHash(self,strg):
        n=len(strg)
        if n==1:
            return 'a'
        hs=[]
        for i in range(1,n):
            curr=ord(strg[i])
            prev=ord(strg[i-1])
            hs.append(str(curr-prev+(0 if prev<=curr else 26)))
        return '$'.join(hs)

        
    def groupShiftedString(self, arr):
        #code here
        hs={}
        for el in arr:
            ch=self.setHash(el)
            if ch not in hs:
                hs[ch]=[el]
            else:
                hs[ch].append(el)
        return [v for v in hs.values()]
                
sol=Solution()
print(sol.groupShiftedString(["acd", "dfg", "wyz", "yab", "mop", "bdfh", "a", "x", "moqs"]))