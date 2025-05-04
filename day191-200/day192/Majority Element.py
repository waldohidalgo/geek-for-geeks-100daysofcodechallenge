class Solution:
    # Moore’s Voting Algorithm
    def majorityElement(self, arr):
        #code here
        n=len(arr)
        limit=((n//2)) if n%2==0 else n//2
        count,elem=0,-1
        for num in arr:
            if elem==num:
                count+=1
            else:
                if count==0:
                    elem=num
                    count=1
                else:
                    count-=1
        ct=0
        for num in arr:
            if num==elem:
                ct+=1
        return elem if ct>limit else -1


sol=Solution()
arr=[2]
print(sol.majorityElement(arr))