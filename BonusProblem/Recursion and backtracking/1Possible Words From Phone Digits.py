class Solution:
    def possibleWords(self, numbers):
        #code here
        asoc={2:"abc",
                3:"def",
                    4:"ghi",
                        5:"jkl",
                            6:"mno",
                                7:"pqrs",
                                    8:"tuv",
                                        9:"wxyz"}
        n=len(numbers)
        res=[]
        def bck(asoc,word,k):
            if k==n:
                res.append(word)
                return
            pattern=asoc[numbers[k]]
            m=len(pattern)
            for i in range(m):
                bck(asoc,word+pattern[i],k+1)
        bck(asoc,"",0)
        return res
    
sol=Solution()
arr=[2]
print(sol.possibleWords(arr))