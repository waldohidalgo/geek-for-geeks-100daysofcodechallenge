class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        max_element=max(arr)
        second_max=-1
        for i in arr:
            if i>second_max and i<max_element:
                second_max=i
        return second_max
sol=Solution()
arr=[10, 5, 10]
print(sol.getSecondLargest(arr))
