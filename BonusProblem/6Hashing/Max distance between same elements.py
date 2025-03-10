class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr):
        # Code here
        hs={}
        md=0
        for i,val in enumerate(arr):
            if val not in hs:
                hs[val]=i
            else:
                md=max(md,i-hs[val])
        return md
    
arr=[1, 1, 2, 2, 2, 1]
print(Solution().maxDistance(arr))