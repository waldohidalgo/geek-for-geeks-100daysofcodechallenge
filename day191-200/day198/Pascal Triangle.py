class Solution:

	def nthRowOfPascalTriangle(self, n):
	    # code here
		res=[1]*n
		def rec(m):
			if m==1:
				return [1]
			elif m==2:
				return [1,1]
			
			rec(m-1)
			for i in range(m-2,0,-1):
				res[i]=res[i-1]+res[i]
			

		rec(n)
		return res

	
sol=Solution()
print(sol.nthRowOfPascalTriangle(4))


