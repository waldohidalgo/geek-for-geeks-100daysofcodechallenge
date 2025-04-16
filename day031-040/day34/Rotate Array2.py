from math import gcd
class Solution:


    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        #Your code here
        n=len(arr)
        factor=d%n
        if factor==0:
            return arr
        gcd_val=gcd(n,factor)
        for i in range(gcd_val):
            temp=arr[i]
            j=i
            while True:
                k=(j+factor)%n
                arr[j]=arr[k]
                j=k
                if j==i:
                    break
            arr[j]=temp
        return arr

    
sol=Solution()
arr=  [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
d=3
print(sol.rotateArr(arr,d))
    