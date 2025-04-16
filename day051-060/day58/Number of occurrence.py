

class Solution:

    def bisect_left(self, arr, target):
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
    def bisect_right(self, arr, target):
        n=len(arr)
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if mid+1<n and arr[mid]==target and arr[mid+1]==target:
                left=mid+1
            elif mid+1<n and arr[mid]==target and arr[mid+1]>target or mid==n-1 and arr[mid]==target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
    def countFreq(self, arr, target):
        #code here
        if target>arr[-1] or target<arr[0]:return 0

        left=self.bisect_left(arr,target)
        right=self.bisect_right(arr,target)
        if(arr[left]!=target or arr[right]!=target):return 0

        return right-left+1
    
arr=  [8, 9, 10, 12, 12, 12]
target=11
obj = Solution()
print(obj.countFreq(arr, target))
print(obj.bisect_left(arr, target))
print(obj.bisect_right(arr, target))