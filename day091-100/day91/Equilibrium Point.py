class Solution:
    #Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        # code here
        rest=sum(arr)
        acc=0
        for i in range(len(arr)):
            rest-=arr[i]
            if acc==rest:
                return i
            acc+=arr[i]
        return -1
    
sol=Solution()
arr=[-7, 1, 5, 2, -4, 3, 0]
print(sol.findEquilibrium(arr))