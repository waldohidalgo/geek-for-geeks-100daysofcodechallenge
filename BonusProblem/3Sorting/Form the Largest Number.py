from functools import cmp_to_key

class Solution:

    def findLargest(self,arr):
	    # code here
        nums = list(map(str, arr))
        nums.sort(key=cmp_to_key(lambda x,y: -1 if str(x)+str(y) > str(y)+str(x) else 1))
        res="".join(nums)
        return  "0" if res[0] == "0" else res
    
arr=[3, 30, 34, 5, 9,0]
obj = Solution()
print(obj.findLargest(arr))