class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        n=len(arr)
        # code here
        count1=0
        for i in range(n):
            if arr[i]!=0:
                count1+=1
            else:
                arr[i],arr[i-count1]=arr[i-count1],arr[i]
        count2=0
        for i in range(n-count1,n):
            if arr[i]==2:
                count2+=1
            else:
                arr[i],arr[i-count2]=arr[i-count2],arr[i]