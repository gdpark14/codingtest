import sys
import collections



number,length=map(int,sys.stdin.readline().split())
ants=[]
for i in range(number):
    temp=int(input())
    if temp<0:
        temp=[-temp,'L']
    else:
        temp=[temp,'D']
    ants.append(temp)
