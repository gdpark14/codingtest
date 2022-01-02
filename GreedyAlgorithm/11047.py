import sys

n,k=map(int,sys.stdin.readline().split())
money=[]

for i in range(n):
    temp=int(sys.stdin.readline())
    money.append(temp)

count=0
index=len(money)-1
while(True):
    if(money[index]>k):
        index-=1
        continue
    temp=k//money[index]
    k=k%money[index]
    count+=temp
    if k==0:
        break
print(count)