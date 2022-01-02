import sys
import collections
from typing import Counter

N=int(input())
cards=list(map(int,sys.stdin.readline().split()))
cards=sorted(cards)
M=int(input())
what=list(map(int,sys.stdin.readline().split()))


def search(lists,num,start,end):
    if start>end:
        return 0

    mid=(start+end)//2
    if num<lists[mid]:
        end=mid-1
        return search(lists,num,start,end)

    elif num>lists[mid]:
        start=mid+1
        return search(lists,num,start,end)
    else:
        temp=lists[start:end+1].count(num)
        return temp

check={}
for c in cards:
    start=0
    end=len(cards)-1

    if c not in check:
        check[c]=search(cards,c,start,end)
    
print(' '.join(str(check[x]) if x in check else '0' for x in what))