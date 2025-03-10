class Solution:
    # k is the maximum number of zeros allowed to flip
    def maxOnes(self, arr, k):
        # code here
        n=len(arr)
        zero_count=0
        left=0
        right=0
        max_ones=0
        while right<n:
            if arr[right]==0:
                zero_count+=1
            while zero_count>k:
                if arr[left]==0:
                    zero_count-=1
                left+=1
            max_ones=max(max_ones,right-left+1)
            right+=1

        return max_ones
    
sol=Solution()
arr= [1, 1]
k=2
print(sol.maxOnes(arr,k))