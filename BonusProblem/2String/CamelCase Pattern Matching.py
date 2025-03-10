class Solution:
    def camelCase(self,arr,pat):
        #code here
        res=[]
        for word in arr:
            i=0
            j=0
            while i<len(word) and j<len(pat):
                if word[i].isupper() and word[i]==pat[j]:
                    i+=1
                    j+=1
                elif word[i].islower():
                    i+=1
                else:
                    break
            if j==len(pat):
                res.append(word)
        return res
    
sol=Solution()
arr=["Hi", "Hello", "HelloWorld", "HiTech", "HiGeek", "HiTechWorld", "HiTechCity", "HiTechLab"]
pat="HA"
print(sol.camelCase(arr,pat))