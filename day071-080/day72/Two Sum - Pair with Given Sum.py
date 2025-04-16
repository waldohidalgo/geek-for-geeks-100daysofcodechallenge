class Solution:
	def twoSum(self, arr, target):
		# code here
		seen={}
		seen[arr[0]]=1
		n=len(arr)
		for i in range(1,n):
			current=arr[i]
			if seen.get(target-current,0):
				return True
			seen[current]=seen.get(current,1)
		return False
	
sol=Solution()
arr=[1, 2, 4, 3, 6]
target=11
print(sol.twoSum(arr,target))
			