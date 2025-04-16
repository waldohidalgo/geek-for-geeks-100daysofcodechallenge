
class Solution:
    
    #Function to check if two strings are rotations of each other or not.
    def areRotations(self,s1,s2):
        #code here
        if len(s1)!=len(s2):
            return False
        return (s1+s1).find(s2)!=-1
    
sol=Solution()
s1 = "abcd"
s2 = "acbd"
print(sol.areRotations(s1,s2))