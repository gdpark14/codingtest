import sys
import collections
import copy

N,M=map(int,sys.stdin.readline().split())
graph_copy=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

safe_region=0

def dfs(x,y,sel_wall):
    sel_wall[x][y]=2

    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<N and 0<=ny<M:
            if sel_wall[nx][ny]==0:
                dfs(nx,ny,sel_wall)


def select_wall(start,count,graph):
    global safe_region
    if count==3:
        for i in range(N):
            for j in range(M):
                if graph[i][j]==2:
                    dfs(i,j,graph)
        safe_count=sum(_.count(0) for _ in graph)
        safe_region=max(safe_count,safe_region)

        return
    else:
        for i in range(start,N*M):
            row=i//M
            col=i%M
            new_graph=copy.deepcopy(graph)
            if new_graph[row][col]==0:
                new_graph[row][col]=1
                select_wall(i,count+1,new_graph)

select_wall(0,0,graph_copy)
print(safe_region)