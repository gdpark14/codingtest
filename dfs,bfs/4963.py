import sys
import collections

dx=[-1,0,1,0,-1,1,1,-1]
dy=[0,1,0,-1,1,1,-1,-1]
sys.setrecursionlimit(10000)
def dfs(i,j,h,w):
    if island[i][j]==1:
        island[i][j]=0
        for k in range(8):
            add_i=dx[k]
            add_j=dy[k]

            if 0<=i+add_i<h and 0<=j+add_j<w:
                if island[i+add_i][j+add_j]==1:
                    dfs(i+add_i,j+add_j,h,w)
        return True
    else:
        return False

while True:
    w,h=map(int,sys.stdin.readline().split())
    if w==0 and h==0:
        break
    island=[]
    for i in range(h):
        temp=list(map(int,sys.stdin.readline().split()))
        island.append(temp)
    count=0
    for i in range(h):
        for j in range(w):
            if dfs(i,j,h,w)==True:
                count+=1
    print(count)
    