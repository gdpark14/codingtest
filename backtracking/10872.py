import sys
import collections

num=int(input())

if num==0:
    print(1)

else:
    temp=1
    while num!=0:
        temp=temp*num
        num-=1
    print(temp)