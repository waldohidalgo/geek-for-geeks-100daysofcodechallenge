from collections import defaultdict

class Solution:
    def fourSum(self, arr, target):
        # code here
        res=set()
        arr.sort()
        hs=defaultdict(list)
        n=len(arr)
        for i in range(n):
            for p in range(i-1):
                curr=arr[p]+arr[i-1]
                hs[curr].append((arr[p],arr[i-1]))
            for j in range(i+1,n):
                tps=hs[target-arr[i]-arr[j]]
                for t in tps:
                    a,b=t
                    if (a,b,arr[i],arr[j]) not in res:
                        res.add((a,b,arr[i],arr[j]))

        return [[t[0],t[1],t[2],t[3]] for t in res]
    
    def fourSum2(self, arr, target):
        arr.sort()
        n = len(arr)
        res = []
        
        for i in range(n - 3):
            if i > 0 and arr[i] == arr[i - 1]:
                continue  
            for j in range(i + 1, n - 2):
                if j > i + 1 and arr[j] == arr[j - 1]:
                    continue 
                left, right = j + 1, n - 1
                while left < right:
                    total = arr[i] + arr[j] + arr[left] + arr[right]
                    if total == target:
                        res.append([arr[i], arr[j], arr[left], arr[right]])
                        left += 1
                        while left < right and arr[left] == arr[left - 1]:
                            left += 1
                        right -= 1
                        while left < right and arr[right] == arr[right + 1]:
                            right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return res

sol=Solution()
arr =[0, 0, 2, 1, 1]
target = 2
print(sol.fourSum2(arr,target))