class Solution:
    def decodedString2(self,s):
        stack=[]
        num=0
        curr=""
        for i,v in enumerate(s):
            if  v.isdigit():
                num=10*num+int(v)
            elif v=="[":
                stack.append((curr,num))
                num=0
                curr=""
            elif v=="]":
                [last,n]=stack.pop()
                curr=last+n*curr
            else:
                curr+=v
        return curr




    
sol=Solution()
s= "3[a3[b]1[ab]]"
print(sol.decodedString(s))
print(sol.decodedString2(s))
            

            

            


        
