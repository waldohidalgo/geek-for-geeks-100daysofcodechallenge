class Solution:
    def countPairsWithDiffK(self,arr, k):
        # code here
        hash_map={}
        for elem in arr:
            hash_map[elem+k]=hash_map.get(elem+k,0)+1

        ans=0
        for elem in arr:
            if elem in hash_map:
                ans+=hash_map[elem]
        return ans
    
sol=Solution()
arr=[8, 12, 16, 4, 0, 20]
k=4
print(sol.countPairsWithDiffK(arr,k))
       