import sys
import collections
import copy
sys.setrecursionlimit(10000)
N=int(input())
picture=[]
for i in range(N):
    temp=sys.stdin.readline()
    temp=list(temp)
    picture.append(temp)
picture_spec=copy.deepcopy(picture)
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def dfs(i,j,color):
    if picture[i][j]==color:
        picture[i][j]='X'
        for k in range(4):
            next_i=i+dx[k]
            next_j=j+dy[k]
            if 0<=next_i<N and 0<=next_j<N:
                dfs(next_i,next_j,color)
        return True
    else:
        return False
def dfs_spec(i,j,color,color_spec):
    if picture_spec[i][j]==color or picture_spec[i][j]==color_spec:
        picture_spec[i][j]='X'
        for k in range(4):
            next_i=i+dx[k]
            next_j=j+dy[k]
            if 0<=next_i<N and 0<=next_j<N:
                dfs_spec(next_i,next_j,color,color_spec)
        return True
    else:
        return False

count=0
for i in range(N):
    for j in range(N):
        if dfs(i,j,'R')==True:
            count+=1
        if dfs(i,j,'B')==True:
            count+=1
        if dfs(i,j,'G')==True:
            count+=1

count_spec=0
for i in range(N):
    for j in range(N):
        if dfs_spec(i,j,'R','G')==True:
            count_spec+=1
        if dfs_spec(i,j,'B','B')==True:
            count_spec+=1

print(count,end=' ')
print(count_spec)
