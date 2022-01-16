import sys
import collections
from collections import deque

N=int(input())
graph=[]
start_i=0
start_j=0
for _ in range(N):
    temp=list(map(int,sys.stdin.readline().split()))
    graph.append(temp)
    if 9 in temp:
        start_i=_
        start_j=temp.index(9)
graph[start_i][start_j]=0
size=2
eat=0

def bfs(i,j,size):
    queue=deque()
    queue.append([i,j,0])
    visited=[[False]*N for _ in range(N)]
    visited[i][j]=True
    fish=[]

    dx=[-1,0,1,0]
    dy=[0,1,0,-1]

    while queue:
        x,y,count=queue.popleft()
        for k in range(4):
            next_x=x+dx[k]
            next_y=y+dy[k]
            if 0<=next_x<N and 0<=next_y<N and visited[next_x][next_y]==False:
                visited[next_x][next_y]=True
                if graph[next_x][next_y]!=0 and graph[next_x][next_y]<size:
                    fish.append([count+1,next_x,next_y])
                    queue.append([next_x,next_y,count+1])
                elif graph[next_x][next_y]==0 or graph[next_x][next_y]==size:
                    queue.append([next_x,next_y,count+1])

    fish.sort()
    if fish:
        return [fish[0][1],fish[0][2],fish[0][0]]
    else:
        return []
answer=0
while True:
    fish_eat=bfs(start_i,start_j,size)
    if fish_eat:
        x,y,move=fish_eat
        graph[x][y]=0
        eat+=1
        answer+=move
        if eat==size:
            size+=1
            eat=0
        start_i,start_j=x,y
    else:
        break
print(answer)
