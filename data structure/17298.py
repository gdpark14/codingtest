import sys
import collections

N=int(input())
nums=list(map(int,sys.stdin.readline().split()))

temp=[]
ans=[]
for i in range(N):
    ans.append(-1)
for i in range(N):
    if not temp:
        temp.append([i,nums[i]])
    else:
        while temp[-1][1]<nums[i]:
            delete=temp.pop()
            delete_index=delete[0]
            ans[delete_index]=nums[i]
            if not temp:
                break
        
        temp.append([i,nums[i]])
print(*ans)