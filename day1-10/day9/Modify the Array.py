class Solution:
    def modifyAndRearrangeArr (self, arr) : 
        #Complete the function
        n=len(arr)
        if n==1:
            return arr

        index = 0
        for i in range(n - 1):
            if arr[i] == arr[i + 1] and arr[i] != 0:
                arr[index] = arr[i] * 2
                arr[i + 1] = 0
                index += 1
            elif arr[i] != 0:
                arr[index] = arr[i]
                index += 1
        
        if n>1 and arr[n - 1] != 0:
            arr[index] = arr[n - 1]
            index += 1

        for i in range(index, n):
            arr[i] = 0
            
        return arr 
    

sol=Solution()
arr=[14, 13, 13, 20, 20, 13, 19, 11, 18, 17, 17, 11, 17, 15, 13, 13, 10, 12, 19]
print(sol.modifyAndRearrangeArr(arr))