import sys
import collections
from collections import deque
N=int(input())
cards=deque()
for i in range(N):
    cards.append(i+1)
flag=0
while len(cards)!=1:
    if flag==0:
        cards.popleft()
        flag=1
    if flag==1:
        temp=cards.popleft()
        cards.append(temp)
        flag=0
print(cards[0])