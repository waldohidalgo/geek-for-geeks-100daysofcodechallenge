from string import ascii_lowercase

class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def areAnagrams(self, s1, s2):
        #code here
        if len(s1)!=len(s2):
            return False
        arr=[0]*26
        for i in s1:
            arr[ord(i)-97]+=1
        for i in s2:
            arr[ord(i)-97]-=1
        return all(i==0 for i in arr)


sol=Solution()
s1 = "a"
s2 = "g"
print(sol.areAnagrams(s1,s2))
    