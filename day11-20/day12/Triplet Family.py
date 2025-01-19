class Solution:
    def findTriplet(self, arr):
        arr.sort()
        n = len(arr)
        for i in range(n-1, -1, -1):
            l=0
            r=i-1
            while l<r:
                if arr[l]+arr[r]==arr[i]:
                    return True
                elif arr[l]+arr[r]<arr[i]:
                    l+=1
                else:
                    r-=1
        return False
    
sol=Solution()
arr = [
    16631, 12900, 25647, 13894, 23690, 23381, 29854, 26746, 
    2992, 11228, 23393, 21603, 27546, 5233, 12004, 16213, 
    21146, 24373, 27029, 28559, 3391, 2178, 12336, 26993, 
    30402, 1479, 19776, 3305, 28832, 28307, 1507, 10031, 
    32137, 15343
]

print(sol.findTriplet(arr))