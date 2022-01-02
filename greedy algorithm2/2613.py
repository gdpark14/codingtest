import sys
import collections

num,group=map(int,sys.stdin.readline().split())
marble=list(map(int,sys.stdin.readline().split()))

left=max(marble)
right=sum(marble)

def possible(goal):
    group_sum=0
    group_cnt=0
    for i in range(len(marble)):
        group_sum+=marble[i]
        if group_sum>goal:
            group_sum=marble[i]
            group_cnt+=1
    group_cnt+=1

    if group_cnt<=group:
        return True
    else:
        return False

while left<=right:
    mid=(left+right)//2
    if possible(mid):
        right=mid-1
    else:
        left=mid+1

ans=[]
def answer(goal,group_check):
    group_sum=0
    cnt=0
    for i in range(len(marble)):
        group_sum+=marble[i]
        if group_sum>goal:
            ans.append(cnt)
            group_sum=marble[i]
            group_check-=1
            print(cnt,end=' ')
            cnt=0
        cnt+=1
        
        if num-i==group_check:
            break
    
    while group_check:
        print(cnt,end=' ')
        cnt=1
        group_check-=1
    
    



print(left)
answer(left,group)

