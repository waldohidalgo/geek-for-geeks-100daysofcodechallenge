class Solution:
       
    #Function to count the number of possible triangles.
    def countTriangles(self, arr):
        # code here
        arr.sort()
        n=len(arr)
        k=2
        ct=0
        while k<n:
            i,j=0,k-1
            while i<j:
                if arr[i]+arr[j]>arr[k]:
                    ct+=(j-i)
                    j-=1
                else:
                    i+=1
            k+=1
        return ct
    
sol=Solution()
arr= [3,4,6,7,7,7]
print(sol.countTriangles(arr))

            
            

