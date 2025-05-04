class Solution:

	def findMaximum(self, arr):
		# code here
		n=len(arr)
		l,r=0,n-1
		while l<r:
			mid=(l+r)//2
			if arr[mid]<arr[mid+1]:
				l=mid+1
			else:
				r=mid
		return arr[l]