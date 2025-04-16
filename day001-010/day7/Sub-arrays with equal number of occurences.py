
from collections import defaultdict
class Solution:
    def sameOccurrence(self, arr, x, y):
        count_map = defaultdict(int)
        count_map[0] = 1
        diff = 0
        result = 0
        
        for num in arr:
            if num == x:
                diff += 1
            elif num == y:
                diff -= 1
            
            result += count_map[diff]
            count_map[diff] += 1
        
        return result
            
sol=Solution()
arr=[2,3,2,1,2,3,8]
#arr=[1,2,1]
print(sol.sameOccurrence(arr,1,8))