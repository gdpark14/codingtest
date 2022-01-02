import sys
import collections
from collections import deque

n=int(input())
people=collections.defaultdict(list)
for i in range(n):
    temp=list(map(int,sys.stdin.readline().split()))
    temp.pop()
    people[i+1]=temp

rumor_num=int(input())
rumor_start=list(map(int,sys.stdin.readline().split()))

def check(index):
    neighbor_num=len(people[index])
    count=0
    for i in people[index]:
        if time[i]!=-1:
            count+=1
    
    if count>=neighbor_num/2:
        return True
    else:
        return False

time=[-1]*(n+1)
for i in rumor_start:
    time[i]=0
start=deque(rumor_start)
que=deque()

while start:
    index=start.popleft()
    temp=people[index]
    for i in temp:
        if time[i]!=-1:
            continue
        if check(i)==True:
            que.append(i)
    if not start:
        while que:
            update_index=que.popleft()
            time[update_index]=time[index]+1
            start.append(update_index)
time.remove(time[0])
print(*time)
