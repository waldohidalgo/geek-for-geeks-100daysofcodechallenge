class Solution:
    def activitySelection(self, start, finish):
        # greedy: siempre elegir el intervalo que finaliza 
        # más temprano
        n = len(start)
    
        activities = sorted(zip(start, finish), key=lambda x: x[1])
        
        count = 1  
        last_end_time = activities[0][1]  

        for i in range(1, n):
            if activities[i][0] > last_end_time:  
                count += 1
                last_end_time = activities[i][1]  

        return count
    
# start = [1, 3, 0, 5, 8, 5]
# finish = [2, 4, 6, 7, 9, 9]
start=[2,2,2,2]
finish=[2,2,2,2]
sol=Solution()
print(sol.activitySelection(start,finish))