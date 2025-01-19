class Solution:
    def minRemoval(self, intervals):
        # Code here
        intervals.sort(key=lambda x: x[1])
        n=len(intervals)
        count=0
        last_end=intervals[0][1]
        for i in range(1,n):
            if intervals[i][0]<last_end:
                count+=1
            else:
                last_end=intervals[i][1]
        return count
               
sol=Solution()
#intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
#intervals = [[1, 3], [1, 3], [1, 3]]
intervals=[[1, 2], [5, 10], [18, 35], [40, 45]]
print(sol.minRemoval(intervals))