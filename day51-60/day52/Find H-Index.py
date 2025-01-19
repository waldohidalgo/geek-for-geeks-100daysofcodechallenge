class Solution:
    # Function to find hIndex
    def hIndex(self, citations):
        #code here
        n=len(citations)
        count=[0]*(n+1)
        for i in range(n):
            if citations[i]>=n:
                count[n]+=1
            else:
                count[citations[i]]+=1
        
        if count[n]>=n:
            return n
        for i in range(n-1,-1,-1):
            count[i]+=count[i+1]
            if count[i]>=i:
                return i
            
sol=Solution()
citations=  [0, 0]
print(sol.hIndex(citations))
        