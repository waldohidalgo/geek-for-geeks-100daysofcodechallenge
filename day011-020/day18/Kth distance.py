from collections import deque

class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        # your code
        uniques = deque()
        for i in range(len(arr)):
            if len(uniques) < k+1:
                if arr[i] in uniques:
                    return True
            else:
                uniques.popleft()
                if arr[i] in uniques:
                    return True
            uniques.append(arr[i])         
        return False
    
sol=Solution()
arr=[6, 8, 4, 1, 8, 5, 7]
k=3
print(sol.checkDuplicatesWithinK(arr,k))