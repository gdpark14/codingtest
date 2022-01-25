import sys
import collections
from collections import deque
import copy
N,M=map(int,sys.stdin.readline().split())

houses=[]
chickens=[]
city=[]
for i in range(N):
    temp=list(map(int,sys.stdin.readline().split()))
    city.append(temp)
    for j in range(len(temp)):
        if temp[j]==1:
            houses.append([i,j])
        if temp[j]==2:
            chickens.append([i,j])

def distance(chickens,houses):
    chicken_distance=0
    for house in houses:
        min_distance=1000000
        for chicken in chickens:
            distance=abs(chicken[0]-house[0])+abs(chicken[1]-house[1])
            min_distance=min(min_distance,distance)
        chicken_distance+=min_distance
    return chicken_distance
ans_min=1000000
def bfs(cur,candidate,number):
    global ans_min

    queue=deque()
    queue.append([cur,candidate])
    while queue:
        temp=queue.popleft()
        cur_temp=temp[0]
        cur_candidate=temp[1]

        if len(cur_temp)==number:
            chicken_distance=distance(cur_temp,houses)
            ans_min=min(ans_min,chicken_distance)
        
        if len(cur_temp)>number:
            break

        for index in range(len(cur_candidate)):
            next_temp=copy.deepcopy(cur_temp)

            next_temp.append(cur_candidate[index])
            next_candidate=cur_candidate[index+1:]
            
            queue.append([next_temp,next_candidate])
            
bfs([],chickens,M)
print(ans_min)
# chicken_distance=0
# for house in houses:
#     house_distance=distance(chicken,house)
#     chicken_distane+=house_distance

