import sys
import collections

sero,garo=map(int,sys.stdin.readline().split())
path=[]
for i in range(sero):
    temp=list(map(int,input()))
    path.append(temp)

dx=[-1,1,0,0]
dy=[0,0,-1,1]
check=[[0]*garo for i in range(sero)]
check[0][0]=1

def bfs(path,check):
    queue=collections.deque()
    queue.append([0,0])

    while queue:
        temp=queue.popleft()
        if temp[0]==garo-1 and temp[1]==sero-1:
            break

        for i in range(4):
            new_x=temp[1]+dx[i]
            new_y=temp[0]+dy[i]

            if 0<=new_x<garo and 0<=new_y<sero:
                if check[new_y][new_x]==0 and path[new_y][new_x]==1:
                    queue.append([new_y,new_x])
                    check[new_y][new_x]=check[temp[0]][temp[1]]+1


bfs(path,check)
print(check[sero-1][garo-1])

