import sys
import collections
import heapq

length,delete=map(int,sys.stdin.readline().split())
temp_delete=delete
num=sys.stdin.readline()

ans=[]
count=0

for i in range(len(num)-1):
    while delete>0 and ans:
        if int(ans[-1])<int(num[i]):
            ans.pop()
            delete-=1
        else:
            break
    ans.append(num[i])

print(''.join(ans[:length-temp_delete]))