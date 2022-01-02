import sys
import collections
import heapq

num=int(sys.stdin.readline())
classes=[]
for i in range(num):
    temp=list(map(int,sys.stdin.readline().split()))
    classes.append(temp)

classes=sorted(classes,key=lambda x:x[0])

ans=[]
heapq.heappush(ans,classes[0][1])

for temp in classes[1:]:
    if temp[0]>=ans[0]:
        heapq.heappop(ans)
        heapq.heappush(ans,temp[1])
    else:
        heapq.heappush(ans,temp[1])
print(len(ans))