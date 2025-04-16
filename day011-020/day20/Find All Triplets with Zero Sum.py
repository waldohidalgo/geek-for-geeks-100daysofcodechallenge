from collections import defaultdict
import copy 

class Solution:
    def findTriplets(self, arr):
        # Your code here
        n=len(arr)
        triplets=[]
        for i in range(n-2):
            for j in range(i+1,n-1):
                val=arr[i]+arr[j]                              
                for k in range(j+1,n):
                    if val+arr[k]==0:
                        triplets.append([i,j,k])
        return triplets
    def findTriplets2(self, arr):
        n=len(arr)
        triplets = []
        occurrences = {}
        occurrences[arr[n-1]]=[n-1]
        for i in range(n-2,0,-1):
            for j in range(i-1,-1,-1):
                complement=-(arr[i]+arr[j])
                if complement in occurrences:
                    for k in occurrences[complement]:
                        triplets.append([j,i,k])
            if arr[i] not in occurrences:
                occurrences[arr[i]]=[i]
            else:
                occurrences[arr[i]].append(i)
        return triplets
        







sol=Solution()
arr=[2, 3, 1, 0, 5]
#arr=[1, -2, 1, 0, 5]
#arr=[0, -1, 2, -3, 1]
print(sol.findTriplets2(arr))