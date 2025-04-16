class Solution:
    def mergeOverlap(self, arr):
        #Code here
        arr.sort(key=lambda x: x[0])
        i=0
        while i<len(arr)-1:
            if arr[i][1]>=arr[i+1][0]:
                arr[i][1]=max(arr[i][1],arr[i+1][1])
                arr.pop(i+1)
            else:
                i+=1
        return arr
    
arr=[[6,8],[1,9],[2,4],[4,7]]

obj=Solution()
print(obj.mergeOverlap(arr))