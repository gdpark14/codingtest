import sys
import collections
from collections import deque

def bfs(i,j):
    queue=deque()
    queue.append([i,j,0])
    visited[i][j]=1

    while queue:
        temp=queue.popleft()
        a=temp[0]
        b=temp[1]
        count=temp[2]

        if a==end_i and b==end_j:
            print(count)
            return

        garo=[-2,-1,1,2,-2,-1,1,2]
        sero=[1,2,2,1,-1,-2,-2,-1]

        for i in range(8):
            add_a=garo[i]
            add_b=sero[i]

            if a+add_a>=0 and a+add_a<length and b+add_b>=0 and b+add_b<length and visited[a+add_a][b+add_b]==0:
                    queue.append([a+add_a,b+add_b,count+1])
                    visited[a+add_a][b+add_b]=1

number=int(input())

for _ in range(number):
    length=int(input())
    cur_i,cur_j=map(int,sys.stdin.readline().split())
    end_i,end_j=map(int,sys.stdin.readline().split())
    visited=[[0]*length for _ in range(length)]
    bfs(cur_i,cur_j)


