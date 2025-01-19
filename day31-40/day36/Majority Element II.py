class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        n=len(arr)
        elem1,elem2=None,None
        count1,count2=0,0
        for i in range(n):
            if elem1==arr[i]:
                count1+=1
            elif elem2==arr[i]:
                count2+=1
            elif count1==0:
                elem1=arr[i]
                count1=1
            elif count2==0:
                elem2=arr[i]
                count2=1
            else:
                count1-=1
                count2-=1
        count1=0
        count2=0
        for i in range(n):
            if arr[i]==elem1:
                count1+=1
            elif arr[i]==elem2:
                count2+=1
        res=[]
        if count1>n//3:
            res.append(elem1)
        if count2>n//3:
            res.append(elem2)
        res.sort()
        return res
    
arr=[2,1,6,6,6,6,6,5,5,5,5]
print(Solution().findMajority(arr))