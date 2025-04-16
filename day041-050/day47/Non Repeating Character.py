from string import ascii_lowercase

class Solution:
    
    #Function to find the first non-repeating character in a string.
    def nonRepeatingChar(self,s):
        #code here
        chars={}
        for char in s:
            chars[char]=chars.get(char,0)+1
        for char in s:
            if chars[char]==1:
                return char
        return '$'
    
s = "aabbccce"
obj = Solution()
ans = obj.nonRepeatingChar(s)
print(ans)