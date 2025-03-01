
class Solution:
    def isBalanced(self, s):
        # code here
        stack = []
        hsO={'{':'}','[':']','(':')'}
        hsC={'}':'{',']':'[',')':'('}
        for i in s:
            if not stack or i in hsO:
                stack.append(i)
            else:
                ch=hsC.get(i)
                if stack[-1]==ch:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
    
sol=Solution()
s="([{]})"
print(sol.isBalanced(s))