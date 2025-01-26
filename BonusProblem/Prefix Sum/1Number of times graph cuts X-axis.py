class Solution:
    def touchedXaxis(self, arr):
        # code here
        ct=1
        acc=0
        for el in arr:
            if acc<0<=acc+el or acc>0>=acc+el:
                ct+=1
            acc+=el
        return ct-1

#arr=[2, 5, -9, 4]
#arr= [4, -6, 2, 8, -2, 3, -12]
arr=[6,-6]
print(Solution().touchedXaxis(arr))