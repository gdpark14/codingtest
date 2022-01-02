import sys
import heapq

num_testcase=int(sys.stdin.readline())

for i in range(num_testcase):
    num_readline,num_xor=map(int,sys.stdin.readline().split())
    heap=[]

    value=0
    for i in range(num_readline):

        comd=sys.stdin.readline().rstrip()

        if comd[0]=='i':
            y=int(comd.split()[1])
            heapq.heappush(heap,y)

            value=value^y

            if len(heap)>num_xor:
                x=heapq.heappop(heap)
                value=value^x

        elif comd[0]=='p':
            print(value)

