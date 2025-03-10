class Solution:
    def countPairs(self, arr, k):
    	# code here
        hs={}
        count=0
        for el in arr:
            count+=hs.get(el-k,0)
            count+=hs.get(el+k,0)
            hs[el]=hs.get(el,0)+1
        return count

arr= [1, 4, 1, 4, 5]
k = 3
print(Solution().countPairs(arr,k))
