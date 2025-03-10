from collections import deque
class Solution:
    def longestSubarray(self, arr, x):
        n=len(arr)
        best_start=0
        left=0
        max_len=0
        max_queu=deque()
        min_queu=deque()
        for right in range(n):
            while max_queu and arr[max_queu[-1]]<arr[right]:
                max_queu.pop()
            max_queu.append(right)

            while min_queu and arr[min_queu[-1]]>arr[right]:
                min_queu.pop()
            min_queu.append(right)

            while arr[max_queu[0]]-arr[min_queu[0]]>x:
                left+=1
                while max_queu and max_queu[0]<left:
                    max_queu.popleft()
                while min_queu and min_queu[0]<left:
                    min_queu.popleft()

            if right-left>max_len:
                max_len=right-left
                best_start=left

        return arr[best_start:best_start+max_len+1]
    

sol=Solution()
arr= [15, 10, 1, 2, 4, 7, 2]
x=5
print(sol.longestSubarray(arr,x))