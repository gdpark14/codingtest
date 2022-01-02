import sys
import collections
import heapq

n=int(sys.stdin.readline())
left_heap=[]
right_heap=[]

for i in range(n):
    temp=int(sys.stdin.readline())
    if len(left_heap)==len(right_heap):
        heapq.heappush(left_heap,(-temp,temp))
        if i==0:
            print(left_heap[0][1])
            continue
    else:
        heapq.heappush(right_heap,(temp,temp))

    if left_heap[0][1]>right_heap[0][1]:
        a=heapq.heappop(left_heap)
        b=heapq.heappop(right_heap)

        heapq.heappush(right_heap,(-a[0],a[1]))
        heapq.heappush(left_heap,(-b[0],b[1]))
    
    print(left_heap[0][1])