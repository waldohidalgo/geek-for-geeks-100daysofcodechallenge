class Solution:
    def startStation(self, gas, cost):
        # Your code here
        n=len(gas)
        if sum(gas)<sum(cost):
            return -1
        tank=0
        start_tank=0
        for i in range(n):
            tank+=gas[i]-cost[i]
            if tank<0:
                tank=0
                start_tank=i+1
        return start_tank%n



