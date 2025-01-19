class Solution:
    def addBinary(self, s1, s2):
		# code here
        n1=len(s1)
        n2=len(s2)
        res=""
        carry=0
        i=n1-1
        j=n2-1
        while i>=0 or j>=0:
            ipos=s1[i]if i>=0 else 0
            jpos=s2[j] if j>=0 else 0
            total=int(ipos)+int(jpos)+carry
            carry=total//2
            res+=str(total%2)
            i-=1
            j-=1
        if carry==1:
            res+="1"
        while res[-1]=='0':
            res=res[:-1]
        return res[::-1]


# s1 = "1101"
# s2 = "111"
s1 = "00100"
s2 = "010"
obj = Solution()
print(obj.addBinary(s1, s2))