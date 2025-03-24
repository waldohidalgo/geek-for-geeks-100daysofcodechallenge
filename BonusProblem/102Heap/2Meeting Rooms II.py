class Solution:
    def minMeetingRooms(self, start, end):
        start.sort()
        end.sort()
        n=len(start)
        left,right=0,0
        max_count=float("-inf")
        count=0
        while left<n:
            if start[left]<end[right]:
                count+=1
                max_count=max(count,max_count)
                left+=1
            else:
                count-=1
                right+=1
        return max_count




start = [2, 9, 6]
end = [4, 12, 10]
sol=Solution()
print(sol.minMeetingRooms(start,end))