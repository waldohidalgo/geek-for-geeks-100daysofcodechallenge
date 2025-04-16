class Solution:

    def insertInterval(self, intervals, newInterval):
        n=len(intervals)
        res=[]
        start,end=newInterval[0],newInterval[1]
        i=0
        while i<n and intervals[i][1]<start:
            res.append(intervals[i])
            i+=1
        while i<n and intervals[i][0]<=end:
            start=min(start,intervals[i][0])
            end=max(end,intervals[i][1])
            i+=1
        res.append([start,end])
        while i<n:
            res.append(intervals[i])
            i+=1
        return res

    def insertInterval2(self, intervals, newInterval):
        # Code here
        n=len(intervals)

        start,end=newInterval[0],newInterval[1]
        i=0
        while i<n and intervals[i][1]<start:
            i+=1
        while i<n and intervals[i][0]<=end:
            start=min(start,intervals[i][0])
            end=max(end,intervals[i][1])
            intervals.pop(i)
            n-=1
        intervals.insert(i,[start,end])

        return intervals

# intervals = [[1,3], [10,15], [20,30]]
# newInterval = [5,6]
# intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
# newInterval = [4,9]
# intervals=[[0,40]]
# newInterval=[82,97]

intervals=[[0,137],[141,153],[157,207],[236,240]]
newInterval=[0,240]
obj = Solution()
print(obj.insertInterval(intervals, newInterval))