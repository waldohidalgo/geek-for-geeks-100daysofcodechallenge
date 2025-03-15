class Solution:
    def longestPalindrome(self, s):
        # code here

        def expand_from_center(s,i,j):
            while i>=0 and j<len(s) and s[i]==s[j]:
                i-=1
                j+=1
            return i+1,j
        
        n=len(s)
        start,end=0,0
        for i in range(n):
            left_one_center,right_one_center=expand_from_center(s,i,i)
            left_two_center,right_two_center=expand_from_center(s,i,i+1)

            if right_one_center-left_one_center>end-start:
                start,end=left_one_center,right_one_center

            if right_two_center-left_two_center>end-start:
                start,end=left_two_center,right_two_center
            
        return s[start:end]

sol=Solution()
s = "abc"
print(sol.longestPalindrome(s)) 