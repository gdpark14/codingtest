

import sys
import collections

N=int(input())
apart=[]
for _ in range(N):
    temp=input()
    temp=list(temp)
    apart.append(temp)

dx=[-1,0,1,0]
dy=[0,1,0,-1]



ans=[]
def dfs(i,j):
    if apart[i][j]=='1':
        apart[i][j]='0'

        global count
        count+=1

        for k in range(4):
            next_i=i+dx[k]
            next_j=j+dy[k]
            if 0<=next_i<N and 0<=next_j<N:
                if apart[next_i][next_j]=='1':
                    dfs(next_i,next_j)
        return True
    else:
        return False

apart_num=0
for i in range(N):
    for j in range(N):

        global count
        count=0
        
        result=dfs(i,j)
        
        if result==True:
            apart_num+=1
            ans.append(count)
print(apart_num)
ans.sort()
for temp in ans:
    print(temp)
