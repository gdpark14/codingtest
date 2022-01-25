import sys
import collections
from collections import deque
M,N,H=map(int,sys.stdin.readline().split())
boxes=[]
for i in range(H):
    cur_box=[]
    for j in range(N):
        temp=list(map(int,sys.stdin.readline().split()))
        cur_box.append(temp)
    boxes.append(cur_box)

# dx=[-1,0,1,0,0,0]
# dy=[0,1,0,-1,0,0]
# dk=[0,0,0,0,1,-1]

dk=[0,0,0,0,1,-1]
dj=[-1,0,1,0,0,0]
di=[0,-1,0,1,0,0]

max_count=-1

def bfs(count):
    global max_count

    queue=deque()
    for k in range(H):
        for i in range(N):
            for j in range(M):
                if boxes[k][i][j]==1:
                    queue.append([k,i,j,count])
    while queue:
        temp=queue.popleft()
        cur_k=temp[0]
        cur_i=temp[1]
        cur_j=temp[2]
        cur_count=temp[3]
        
        max_count=max(max_count,cur_count)


        if boxes[cur_k][cur_i][cur_j]==1:
            boxes[cur_k][cur_i][cur_j]=2

        for index in range(6):
            next_k=cur_k+dk[index]
            next_i=cur_i+di[index]
            next_j=cur_j+dj[index]
            next_count=cur_count+1

            if 0<=next_k<H and 0<=next_i<N and 0<=next_j<M:
                if boxes[next_k][next_i][next_j]==0:
                    boxes[next_k][next_i][next_j]=1
                    queue.append([next_k,next_i,next_j,next_count])

bfs(0)
for cur_box in boxes:
    for garo in cur_box:
        if 0 in garo:
            max_count=-1
            break
print(max_count)