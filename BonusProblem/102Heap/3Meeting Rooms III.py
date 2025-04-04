import heapq

#User function Template for python3
class Solution:
    def mostBooked(self, n, meetings):
        #code here
        # solucion ineficiente
        room=[0]*n
        m=len(meetings)
        meetings.sort()
        

        # rooms_ends almacena las horas de termino de cada reunion asignada
        # a cada sala y el numero de la sala
        room_ends=[]
        for j in range(n):
            heapq.heappush(room_ends,(0,j))

        # delayed_meets almacena la tupla de meet de cada
        # reunión atrasada
        delayed_meets=[]

        for i in range(m):

            current_meet=meetings[i]
            current_time=current_meet[0]
 
            while delayed_meets and room_ends[0][0]<=current_time:
                delayed_start_time,delayed_end_time=heapq.heappop(delayed_meets)
                end_time,room_number=heapq.heappop(room_ends)
                room[room_number]+=1
                heapq.heappush(room_ends,(end_time+(delayed_end_time-delayed_start_time),room_number))

            availables_rooms=[]
            while room_ends and room_ends[0][0]<=current_time:
                end_time,room_number=heapq.heappop(room_ends)
                heapq.heappush(availables_rooms,(room_number,end_time))

            if availables_rooms:
                room_number,end_time=heapq.heappop(availables_rooms)
                room[room_number]+=1
                heapq.heappush(room_ends, (current_meet[1], room_number))
                while availables_rooms:
                    room_number,end_time=heapq.heappop(availables_rooms)
                    heapq.heappush(room_ends,(end_time,room_number))
            else:
                heapq.heappush(delayed_meets,(current_meet[0],current_meet[1]))

        
        while delayed_meets:
            end_time,roomNumber=heapq.heappop(room_ends)
            room[roomNumber]+=1
            delayed_start_time,delayed_end_time=heapq.heappop(delayed_meets)
            heapq.heappush(room_ends,(end_time+(delayed_end_time-delayed_start_time),roomNumber))

        
        return room
    
    def mostBooked2(self, n, meetings):
        available_rooms = list(range(n))
        busy_rooms = []
        meeting_count = [0] * n
        meetings.sort()
        for start, end in meetings:
            while busy_rooms and busy_rooms[0][0] <= start:
                end_time, room_number = heapq.heappop(busy_rooms)
                heapq.heappush(available_rooms, room_number)    

            if available_rooms:
                room_number = heapq.heappop(available_rooms)
                heapq.heappush(busy_rooms, (end, room_number))
            else:
                # esta parte del codigo hace varios pasos de mi codigo anterior
                # en un solo paso
                earliest_end, room_number = heapq.heappop(busy_rooms)
                new_end = earliest_end + (end - start)
                heapq.heappush(busy_rooms, (new_end, room_number))

            meeting_count[room_number] += 1
        max_meetings = max(meeting_count)
        return meeting_count.index(max_meetings)


sol=Solution()
n = 2
meetings= [[0, 6], [2, 3], [3, 7], [4, 8], [6, 8]]
# n = 4
# meetings = [[0, 8], [1, 4], [3, 4], [2, 3]]
print(sol.mostBooked(n,meetings))