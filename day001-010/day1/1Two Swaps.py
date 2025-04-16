class Solution:
    def checkSorted(self, arr):
        #code here
        count=0
        for i in range(len(arr)-1):
            if arr[i]==i+1:
                continue
            while arr[i]!=i+1:                
                arr[arr[i]-1],arr[i]=arr[i],arr[arr[i]-1]
                count+=1
                if count>2:
                    return False
        
        if count==0 or count==2:
            return True
        else:
            return False   
                


sol=Solution()
arr=[4,3,2,1]
print(sol.checkSorted(arr))