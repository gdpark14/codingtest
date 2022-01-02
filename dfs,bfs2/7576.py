import sys
import collections
from collections import deque

n,m=map(int,sys.stdin.readline().split())
tomatoes=[]
start=deque()

for i in range(m):
    temp=list(map(int,sys.stdin.readline().split()))
    for j in range(len(temp)):
        if temp[j]==1:
            start.append([i,j])
    tomatoes.append(temp)
global ans
ans=-1

def length(a,b):
    if a>=0 and a<m and b>=0 and b<n:
        return True
    else:
        return False

next=deque()
while start:
    index=start.popleft()

    i=index[0]
    j=index[1]


    if length(i,j-1) and tomatoes[i][j-1]==0:
        tomatoes[i][j-1]=1
        next.append([i,j-1])

    if length(i,j+1) and tomatoes[i][j+1]==0:
        tomatoes[i][j+1]=1
        next.append([i,j+1])

    if length(i-1,j) and tomatoes[i-1][j]==0:
        tomatoes[i-1][j]=1
        next.append([i-1,j])

    if length(i+1,j) and tomatoes[i+1][j]==0:
        tomatoes[i+1][j]=1
        next.append([i+1,j])
        
    if not start:
        ans+=1
        start=next
        next=deque()


for tomato_list in tomatoes:
    if 0 in tomato_list:
        ans=-1

print(ans)