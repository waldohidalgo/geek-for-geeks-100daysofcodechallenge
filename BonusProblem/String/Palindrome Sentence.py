class Solution:
    def sentencePalindrome(self, s):
        # your code here
        result = ''.join(char.lower() for char in s if char.isalnum())
        return result == result[::-1]
    
s = "Abc 012..## 10cbA"

print(Solution().sentencePalindrome(s))