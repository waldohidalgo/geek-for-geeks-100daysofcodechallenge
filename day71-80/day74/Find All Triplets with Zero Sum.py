from collections import defaultdict

class Solution:
    def findTriplets(self, arr):  
        n=len(arr)
        triplets=[]
        for i in range(2,n):
            target=-arr[i]
            seen={}
            seen[arr[0]]=[0]
            for j in range(1,i):
                indexes=seen.get(target-arr[j],[])
                if indexes:
                    for k in indexes:
                        triplets.append([k,j,i])
                if seen.get(arr[j],0):
                    seen[arr[j]].append(j)
                else:
                    seen[arr[j]]=[j]

        return triplets
    
    def findTriplets1(self,arr):
        n = len(arr)
        triplets = []

        for i in range(2, n):
            target = -arr[i]
            seen = defaultdict(list)  
            seen[arr[0]].append(0)  

            for j in range(1, i):
                complement = target - arr[j]
                if complement in seen:
                    for k in seen[complement]:
                        triplets.append([k, j, i])  
                seen[arr[j]].append(j)  

        return triplets
    
sol=Solution()
arr=[1, -2, 1, 0, 5]
print(sol.findTriplets1(arr))
                    

