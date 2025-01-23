class Solution:

    def __init__(self):
        self.words=["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        self.tens=["Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
    def convertToWords(self, n):
        # code here
        if n==0:
            return "Zero"
        res=""
        while n>0:
            if n>=10**9:
                res+=self.convertToWords(n//10**9)+" Billion"+(" " if n%10**9 else "")
                n=n%10**9
            elif n>=10**6:
                res+=self.convertToWords(n//10**6)+" Million"+(" " if n%10**6 else "")
                n=n%10**6
            elif n>=10**3:
                res+=self.convertToWords(n//10**3)+" Thousand"+(" " if n%10**3 else "")
                n=n%10**3
            elif n>=100:
                res+=self.convertToWords(n//100)+" Hundred"+(" " if n%100 else "")
                n=n%100
            elif n>=20:
                res+=self.tens[n//10 - 2]+(" " if n%10 else "")
                n=n%10
            else:
                res+=self.words[n]
                n=0
        return res
    
sol=Solution()
n=1000000000
print(sol.convertToWords(n))